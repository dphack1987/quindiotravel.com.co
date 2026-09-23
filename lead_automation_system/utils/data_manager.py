"""
Utilidades de Gestión de Datos
Sistema para backup, restauración y mantenimiento de datos del sistema
"""

import json
import os
import shutil
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import zipfile
import csv

class DataManager:
    """Gestor de datos del sistema de automatización de leads"""
    
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = data_dir
        self.backup_dir = os.path.join(data_dir, 'backups')
        self.export_dir = os.path.join(data_dir, 'exports')
        
        # Crear directorios si no existen
        os.makedirs(self.backup_dir, exist_ok=True)
        os.makedirs(self.export_dir, exist_ok=True)
    
    def backup_all_data(self) -> Dict:
        """Crear backup completo de todos los datos del sistema"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f"backup_{timestamp}.zip"
        backup_path = os.path.join(self.backup_dir, backup_filename)
        
        try:
            # Crear archivo ZIP con todos los datos
            with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Agregar archivos JSON principales
                data_files = [
                    'leads_db.json',
                    'conversion_data.json',
                    'scoring_rules.json'
                ]
                
                for filename in data_files:
                    file_path = os.path.join(self.data_dir, filename)
                    if os.path.exists(file_path):
                        zipf.write(file_path, filename)
                
                # Agregar reportes si existen
                reports_dir = os.path.join(self.data_dir, 'reports')
                if os.path.exists(reports_dir):
                    for root, dirs, files in os.walk(reports_dir):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, self.data_dir)
                            zipf.write(file_path, arcname)
            
            return {
                'success': True,
                'backup_path': backup_path,
                'filename': backup_filename,
                'timestamp': timestamp,
                'size_bytes': os.path.getsize(backup_path),
                'size_mb': round(os.path.getsize(backup_path) / (1024 * 1024), 2)
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def restore_data(self, backup_path: str) -> Dict:
        """Restaurar datos desde un backup"""
        try:
            if not os.path.exists(backup_path):
                return {
                    'success': False,
                    'error': 'Archivo de backup no encontrado'
                }
            
            # Crear backup de seguridad antes de restaurar
            safety_backup = self.backup_all_data()
            if not safety_backup['success']:
                return {
                    'success': False,
                    'error': 'No se pudo crear backup de seguridad'
                }
            
            # Extraer backup
            with zipfile.ZipFile(backup_path, 'r') as zipf:
                zipf.extractall(self.data_dir)
            
            return {
                'success': True,
                'restored_from': backup_path,
                'safety_backup': safety_backup['backup_path']
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def export_leads_to_csv(self, output_filename: Optional[str] = None) -> Dict:
        """Exportar leads a formato CSV"""
        try:
            leads_file = os.path.join(self.data_dir, 'leads_db.json')
            
            if not os.path.exists(leads_file):
                return {
                    'success': False,
                    'error': 'Archivo de leads no encontrado'
                }
            
            with open(leads_file, 'r', encoding='utf-8') as f:
                leads = json.load(f)
            
            if not leads:
                return {
                    'success': False,
                    'error': 'No hay leads para exportar'
                }
            
            # Generar nombre de archivo si no se proporciona
            if not output_filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                output_filename = f"leads_export_{timestamp}.csv"
            
            output_path = os.path.join(self.export_dir, output_filename)
            
            # Exportar a CSV
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                # Obtener todos los campos posibles de todos los leads
                fieldnames = set()
                for lead in leads:
                    fieldnames.update(lead.keys())
                fieldnames = sorted(fieldnames)
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for lead in leads:
                    # Convertir valores complejos a strings
                    row = {}
                    for key, value in lead.items():
                        if isinstance(value, (dict, list)):
                            row[key] = json.dumps(value, ensure_ascii=False)
                        else:
                            row[key] = value
                    writer.writerow(row)
            
            return {
                'success': True,
                'export_path': output_path,
                'filename': output_filename,
                'total_leads': len(leads),
                'size_bytes': os.path.getsize(output_path)
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def import_leads_from_csv(self, csv_path: str, merge: bool = True) -> Dict:
        """Importar leads desde archivo CSV"""
        try:
            if not os.path.exists(csv_path):
                return {
                    'success': False,
                    'error': 'Archivo CSV no encontrado'
                }
            
            # Leer leads existentes si merge es True
            existing_leads = []
            if merge:
                leads_file = os.path.join(self.data_dir, 'leads_db.json')
                if os.path.exists(leads_file):
                    with open(leads_file, 'r', encoding='utf-8') as f:
                        existing_leads = json.load(f)
            
            # Leer CSV
            imported_leads = []
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Convertir strings JSON a objetos si es necesario
                    lead = {}
                    for key, value in row.items():
                        try:
                            # Intentar parsear como JSON
                            lead[key] = json.loads(value)
                        except:
                            lead[key] = value
                    imported_leads.append(lead)
            
            # Merge o reemplazar
            if merge:
                # Crear set de IDs existentes para evitar duplicados
                existing_ids = {lead.get('id') for lead in existing_leads if lead.get('id')}
                
                # Agregar solo leads nuevos
                new_leads = [lead for lead in imported_leads 
                            if lead.get('id') not in existing_ids]
                
                final_leads = existing_leads + new_leads
            else:
                final_leads = imported_leads
            
            # Guardar leads actualizados
            leads_file = os.path.join(self.data_dir, 'leads_db.json')
            with open(leads_file, 'w', encoding='utf-8') as f:
                json.dump(final_leads, f, indent=2, ensure_ascii=False)
            
            return {
                'success': True,
                'total_leads_after': len(final_leads),
                'imported_leads': len(imported_leads),
                'new_leads_added': len(final_leads) - len(existing_leads) if merge else len(imported_leads)
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def clean_old_backups(self, days_to_keep: int = 30) -> Dict:
        """Limpiar backups antiguos"""
        try:
            cutoff_date = datetime.now() - timedelta(days=days_to_keep)
            deleted_files = []
            total_size_freed = 0
            
            for filename in os.listdir(self.backup_dir):
                if filename.endswith('.zip'):
                    file_path = os.path.join(self.backup_dir, filename)
                    file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    
                    if file_time < cutoff_date:
                        file_size = os.path.getsize(file_path)
                        os.remove(file_path)
                        deleted_files.append(filename)
                        total_size_freed += file_size
            
            return {
                'success': True,
                'deleted_files': len(deleted_files),
                'total_size_freed_bytes': total_size_freed,
                'total_size_freed_mb': round(total_size_freed / (1024 * 1024), 2),
                'deleted_filenames': deleted_files
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_data_statistics(self) -> Dict:
        """Obtener estadísticas de los datos"""
        try:
            stats = {
                'leads_db': self._get_file_stats('leads_db.json'),
                'conversion_data': self._get_file_stats('conversion_data.json'),
                'scoring_rules': self._get_file_stats('scoring_rules.json'),
                'backups': self._get_directory_stats(self.backup_dir),
                'exports': self._get_directory_stats(self.export_dir),
                'reports': self._get_directory_stats(os.path.join(self.data_dir, 'reports'))
            }
            
            # Contar leads por categoría
            leads_file = os.path.join(self.data_dir, 'leads_db.json')
            if os.path.exists(leads_file):
                with open(leads_file, 'r', encoding='utf-8') as f:
                    leads = json.load(f)
                
                category_counts = {'hot_lead': 0, 'warm_lead': 0, 'cold_lead': 0, 'unknown': 0}
                for lead in leads:
                    category = lead.get('score', {}).get('category', 'unknown')
                    category_counts[category] = category_counts.get(category, 0) + 1
                
                stats['leads_by_category'] = category_counts
                stats['total_leads'] = len(leads)
            
            return {
                'success': True,
                'statistics': stats,
                'generated_at': datetime.now().isoformat()
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _get_file_stats(self, filename: str) -> Dict:
        """Obtener estadísticas de un archivo específico"""
        file_path = os.path.join(self.data_dir, filename)
        
        if not os.path.exists(file_path):
            return {
                'exists': False,
                'size_bytes': 0,
                'last_modified': None
            }
        
        return {
            'exists': True,
            'size_bytes': os.path.getsize(file_path),
            'size_kb': round(os.path.getsize(file_path) / 1024, 2),
            'last_modified': datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
        }
    
    def _get_directory_stats(self, directory: str) -> Dict:
        """Obtener estadísticas de un directorio"""
        if not os.path.exists(directory):
            return {
                'exists': False,
                'file_count': 0,
                'total_size_bytes': 0
            }
        
        total_size = 0
        file_count = 0
        
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
                file_count += 1
        
        return {
            'exists': True,
            'file_count': file_count,
            'total_size_bytes': total_size,
            'total_size_mb': round(total_size / (1024 * 1024), 2)
        }
    
    def validate_data_integrity(self) -> Dict:
        """Validar integridad de los datos"""
        validation_results = {
            'leads_db': self._validate_json_file('leads_db.json'),
            'conversion_data': self._validate_json_file('conversion_data.json'),
            'scoring_rules': self._validate_json_file('scoring_rules.json')
        }
        
        all_valid = all(result['valid'] for result in validation_results.values())
        
        return {
            'success': True,
            'all_valid': all_valid,
            'validation_results': validation_results,
            'validated_at': datetime.now().isoformat()
        }
    
    def _validate_json_file(self, filename: str) -> Dict:
        """Validar un archivo JSON"""
        file_path = os.path.join(self.data_dir, filename)
        
        if not os.path.exists(file_path):
            return {
                'valid': False,
                'error': 'Archivo no encontrado',
                'file': filename
            }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return {
                'valid': True,
                'file': filename,
                'data_type': type(data).__name__,
                'item_count': len(data) if isinstance(data, (list, dict)) else 0
            }
        
        except json.JSONDecodeError as e:
            return {
                'valid': False,
                'error': f'JSON inválido: {str(e)}',
                'file': filename
            }
        except Exception as e:
            return {
                'valid': False,
                'error': str(e),
                'file': filename
            }

# Funciones helper para uso desde línea de comandos
def create_backup():
    """Crear backup completo"""
    manager = DataManager()
    result = manager.backup_all_data()
    
    if result['success']:
        print(f"✅ Backup creado exitosamente")
        print(f"📁 Archivo: {result['filename']}")
        print(f"📊 Tamaño: {result['size_mb']} MB")
    else:
        print(f"❌ Error al crear backup: {result['error']}")
    
    return result

def restore_backup(backup_path: str):
    """Restaurar backup"""
    manager = DataManager()
    result = manager.restore_data(backup_path)
    
    if result['success']:
        print(f"✅ Backup restaurado exitosamente")
        print(f"📁 Desde: {backup_path}")
        print(f"🔒 Backup de seguridad: {result['safety_backup']}")
    else:
        print(f"❌ Error al restaurar backup: {result['error']}")
    
    return result

def export_leads():
    """Exportar leads a CSV"""
    manager = DataManager()
    result = manager.export_leads_to_csv()
    
    if result['success']:
        print(f"✅ Leads exportados exitosamente")
        print(f"📁 Archivo: {result['filename']}")
        print(f"📊 Total leads: {result['total_leads']}")
    else:
        print(f"❌ Error al exportar leads: {result['error']}")
    
    return result

def show_statistics():
    """Mostrar estadísticas de datos"""
    manager = DataManager()
    result = manager.get_data_statistics()
    
    if result['success']:
        stats = result['statistics']
        print("📊 ESTADÍSTICAS DE DATOS")
        print("=" * 50)
        print(f"Total leads: {stats.get('total_leads', 0)}")
        print(f"Leads por categoría:")
        for category, count in stats.get('leads_by_category', {}).items():
            print(f"  - {category}: {count}")
        print(f"\nBackups: {stats['backups']['file_count']} archivos")
        print(f"Exports: {stats['exports']['file_count']} archivos")
        print(f"Reports: {stats['reports']['file_count']} archivos")
    else:
        print(f"❌ Error al obtener estadísticas: {result['error']}")
    
    return result

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python data_manager.py <comando>")
        print("Comandos: backup, restore <path>, export, stats, validate")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'backup':
        create_backup()
    elif command == 'restore':
        if len(sys.argv) < 3:
            print("Error: Se requiere ruta del backup")
            sys.exit(1)
        restore_backup(sys.argv[2])
    elif command == 'export':
        export_leads()
    elif command == 'stats':
        show_statistics()
    elif command == 'validate':
        manager = DataManager()
        result = manager.validate_data_integrity()
        
        if result['success']:
            print("🔍 VALIDACIÓN DE INTEGRIDAD DE DATOS")
            print("=" * 50)
            
            for file, validation in result['validation_results'].items():
                status = "✅" if validation['valid'] else "❌"
                print(f"{status} {file}: {validation.get('error', 'Válido')}")
            
            print(f"\nResultado global: {'✅ VÁLIDO' if result['all_valid'] else '❌ INVÁLIDO'}")
        else:
            print(f"❌ Error al validar: {result['error']}")
    else:
        print(f"Comando desconocido: {command}")
        sys.exit(1)