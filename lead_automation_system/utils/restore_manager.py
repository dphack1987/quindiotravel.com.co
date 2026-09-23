"""
Gestor de Restauración de Datos
Sistema para restaurar datos desde backups con opciones avanzadas
"""

import os
import json
import shutil
from datetime import datetime
from typing import Dict, List, Optional
from data_manager import DataManager

class RestoreManager:
    """Gestor de restauración de datos con validación y opciones"""
    
    def __init__(self, data_manager: DataManager = None):
        self.data_manager = data_manager or DataManager()
        self.restore_log_dir = os.path.join(self.data_manager.data_dir, 'restore_logs')
        os.makedirs(self.restore_log_dir, exist_ok=True)
    
    def list_available_backups(self) -> Dict:
        """Listar todos los backups disponibles"""
        try:
            backup_files = []
            
            for filename in os.listdir(self.data_manager.backup_dir):
                if filename.endswith('.zip'):
                    file_path = os.path.join(self.data_manager.backup_dir, filename)
                    file_stat = os.stat(file_path)
                    
                    backup_type = 'unknown'
                    if filename.startswith('backup_'):
                        backup_type = 'daily'
                    elif filename.startswith('weekly_backup_'):
                        backup_type = 'weekly'
                    elif filename.startswith('monthly_backup_'):
                        backup_type = 'monthly'
                    
                    backup_files.append({
                        'filename': filename,
                        'path': file_path,
                        'type': backup_type,
                        'size_bytes': file_stat.st_size,
                        'size_mb': round(file_stat.st_size / (1024 * 1024), 2),
                        'created': datetime.fromtimestamp(file_stat.st_ctime).isoformat(),
                        'modified': datetime.fromtimestamp(file_stat.st_mtime).isoformat()
                    })
            
            # Ordenar por fecha de modificación (más reciente primero)
            backup_files.sort(key=lambda x: x['modified'], reverse=True)
            
            return {
                'success': True,
                'total_backups': len(backup_files),
                'backups': backup_files
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def preview_backup_contents(self, backup_path: str) -> Dict:
        """Previsualizar contenido de un backup sin restaurar"""
        try:
            import zipfile
            
            if not os.path.exists(backup_path):
                return {
                    'success': False,
                    'error': 'Archivo de backup no encontrado'
                }
            
            contents = []
            
            with zipfile.ZipFile(backup_path, 'r') as zipf:
                for file_info in zipf.infolist():
                    if not file_info.is_dir():
                        file_size = file_info.file_size
                        file_size_kb = round(file_size / 1024, 2)
                        
                        contents.append({
                            'filename': file_info.filename,
                            'size_bytes': file_size,
                            'size_kb': file_size_kb,
                            'compressed_size': file_info.compress_size,
                            'date_time': datetime(*file_info.date_time).isoformat()
                        })
            
            return {
                'success': True,
                'backup_path': backup_path,
                'total_files': len(contents),
                'contents': contents
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def validate_backup_integrity(self, backup_path: str) -> Dict:
        """Validar integridad de un backup"""
        try:
            import zipfile
            
            if not os.path.exists(backup_path):
                return {
                    'success': False,
                    'error': 'Archivo de backup no encontrado'
                }
            
            # Intentar abrir el archivo ZIP
            try:
                with zipfile.ZipFile(backup_path, 'r') as zipf:
                    # Verificar que el archivo ZIP esté intacto
                    test_result = zipf.testzip()
                    
                    if test_result is not None:
                        return {
                            'success': False,
                            'error': f'Archivo ZIP corrupto: {test_result}'
                        }
                    
                    # Verificar archivos críticos
                    critical_files = ['leads_db.json', 'conversion_data.json', 'scoring_rules.json']
                    missing_files = []
                    
                    for critical_file in critical_files:
                        if critical_file not in zipf.namelist():
                            missing_files.append(critical_file)
                    
                    if missing_files:
                        return {
                            'success': False,
                            'error': f'Faltan archivos críticos: {", ".join(missing_files)}'
                        }
                    
                    return {
                        'success': True,
                        'integrity': 'valid',
                        'total_files': len(zipf.namelist()),
                        'critical_files_present': True
                    }
            
            except zipfile.BadZipFile:
                return {
                    'success': False,
                    'error': 'Archivo no es un ZIP válido'
                }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def restore_with_validation(self, backup_path: str, create_safety_backup: bool = True) -> Dict:
        """Restaurar backup con validación completa"""
        print(f"🔍 Iniciando restauración con validación...")
        print(f"📁 Backup: {backup_path}")
        
        # 1. Validar integridad del backup
        print("🔍 Paso 1: Validando integridad del backup...")
        validation_result = self.validate_backup_integrity(backup_path)
        
        if not validation_result['success']:
            print(f"❌ Validación falló: {validation_result['error']}")
            return validation_result
        
        print(f"✅ Integridad validada: {validation_result['total_files']} archivos")
        
        # 2. Crear backup de seguridad
        safety_backup_path = None
        if create_safety_backup:
            print("🔒 Paso 2: Creando backup de seguridad...")
            safety_result = self.data_manager.backup_all_data()
            
            if safety_result['success']:
                safety_backup_path = safety_result['backup_path']
                print(f"✅ Backup de seguridad creado: {safety_result['backup_filename']}")
            else:
                print(f"⚠️  No se pudo crear backup de seguridad: {safety_result['error']}")
                print("⚠️  Continuando sin backup de seguridad...")
        
        # 3. Restaurar backup
        print("🔄 Paso 3: Restaurando backup...")
        restore_result = self.data_manager.restore_data(backup_path)
        
        if not restore_result['success']:
            print(f"❌ Restauración falló: {restore_result['error']}")
            
            # Intentar restaurar desde backup de seguridad
            if safety_backup_path:
                print("🔄 Intentando restaurar desde backup de seguridad...")
                safety_restore = self.data_manager.restore_data(safety_backup_path)
                if safety_restore['success']:
                    print("✅ Restaurado desde backup de seguridad exitosamente")
                else:
                    print("❌ No se pudo restaurar desde backup de seguridad")
            
            return restore_result
        
        print(f"✅ Backup restaurado exitosamente")
        
        # 4. Validar datos restaurados
        print("🔍 Paso 4: Validando datos restaurados...")
        data_validation = self.data_manager.validate_data_integrity()
        
        if data_validation['success'] and data_validation['all_valid']:
            print("✅ Datos restaurados validados correctamente")
        else:
            print("⚠️  Advertencia: Validación de datos mostró problemas")
            for file, validation in data_validation['validation_results'].items():
                if not validation['valid']:
                    print(f"   ⚠️  {file}: {validation['error']}")
        
        # 5. Registrar restauración
        self._log_restore_operation(backup_path, safety_backup_path, restore_result, data_validation)
        
        return {
            'success': True,
            'backup_restored': backup_path,
            'safety_backup': safety_backup_path,
            'validation': data_validation,
            'restore_log': self._get_latest_restore_log()
        }
    
    def selective_restore(self, backup_path: str, files_to_restore: List[str]) -> Dict:
        """Restaurar solo archivos específicos del backup"""
        try:
            import zipfile
            
            if not os.path.exists(backup_path):
                return {
                    'success': False,
                    'error': 'Archivo de backup no encontrado'
                }
            
            print(f"🔄 Restauración selectiva de {len(files_to_restore)} archivos")
            
            # Crear backup de seguridad de archivos que serán reemplazados
            safety_backup = {}
            for filename in files_to_restore:
                file_path = os.path.join(self.data_manager.data_dir, filename)
                if os.path.exists(file_path):
                    safety_path = os.path.join(self.data_manager.data_dir, f"{filename}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
                    shutil.copy2(file_path, safety_path)
                    safety_backup[filename] = safety_path
            
            # Extraer solo archivos seleccionados
            with zipfile.ZipFile(backup_path, 'r') as zipf:
                for filename in files_to_restore:
                    if filename in zipf.namelist():
                        zipf.extract(filename, self.data_manager.data_dir)
                        print(f"✅ Restaurado: {filename}")
                    else:
                        print(f"⚠️  Archivo no encontrado en backup: {filename}")
            
            return {
                'success': True,
                'restored_files': files_to_restore,
                'safety_backups': safety_backup
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def rollback_restore(self, safety_backup_path: str) -> Dict:
        """Revertir una restauración usando el backup de seguridad"""
        try:
            if not os.path.exists(safety_backup_path):
                return {
                    'success': False,
                    'error': 'Backup de seguridad no encontrado'
                }
            
            print(f"🔄 Iniciando rollback desde backup de seguridad...")
            
            # Restaurar desde backup de seguridad
            restore_result = self.data_manager.restore_data(safety_backup_path)
            
            if restore_result['success']:
                print("✅ Rollback completado exitosamente")
            else:
                print(f"❌ Rollback falló: {restore_result['error']}")
            
            return restore_result
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _log_restore_operation(self, backup_path: str, safety_backup: str, 
                              restore_result: Dict, validation_result: Dict):
        """Registrar operación de restauración en log"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'backup_restored': backup_path,
            'safety_backup': safety_backup,
            'restore_success': restore_result['success'],
            'validation_success': validation_result.get('success', False),
            'validation_all_valid': validation_result.get('all_valid', False),
            'user': os.environ.get('USER', 'unknown')
        }
        
        log_filename = f"restore_log_{datetime.now().strftime('%Y%m%d')}.json"
        log_path = os.path.join(self.restore_log_dir, log_filename)
        
        # Leer logs existentes
        existing_logs = []
        if os.path.exists(log_path):
            with open(log_path, 'r', encoding='utf-8') as f:
                existing_logs = json.load(f)
        
        # Agregar nuevo log
        existing_logs.append(log_entry)
        
        # Guardar logs actualizados
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(existing_logs, f, indent=2, ensure_ascii=False)
    
    def _get_latest_restore_log(self) -> Dict:
        """Obtener el log de restauración más reciente"""
        try:
            log_files = [f for f in os.listdir(self.restore_log_dir) if f.startswith('restore_log_')]
            
            if not log_files:
                return {'latest_log': None}
            
            # Obtener el log más reciente
            latest_log_file = max(log_files)
            log_path = os.path.join(self.restore_log_dir, latest_log_file)
            
            with open(log_path, 'r', encoding='utf-8') as f:
                logs = json.load(f)
            
            return {
                'latest_log': logs[-1] if logs else None,
                'total_restore_operations': len(logs)
            }
        
        except Exception as e:
            return {
                'latest_log': None,
                'error': str(e)
            }
    
    def get_restore_history(self, limit: int = 10) -> Dict:
        """Obtener historial de operaciones de restauración"""
        try:
            all_logs = []
            
            for filename in os.listdir(self.restore_log_dir):
                if filename.startswith('restore_log_'):
                    log_path = os.path.join(self.restore_log_dir, filename)
                    with open(log_path, 'r', encoding='utf-8') as f:
                        logs = json.load(f)
                        all_logs.extend(logs)
            
            # Ordenar por timestamp (más reciente primero)
            all_logs.sort(key=lambda x: x['timestamp'], reverse=True)
            
            return {
                'success': True,
                'total_operations': len(all_logs),
                'recent_operations': all_logs[:limit]
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

def main():
    """Función principal para ejecutar desde línea de comandos"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Gestor de restauración de datos')
    parser.add_argument('--action', choices=['list', 'preview', 'validate', 'restore', 'selective', 'rollback', 'history'],
                       default='list', help='Acción a ejecutar')
    parser.add_argument('--backup', type=str, help='Ruta del archivo de backup')
    parser.add_argument('--files', type=str, nargs='+', help='Archivos específicos para restauración selectiva')
    parser.add_argument('--safety-backup', type=str, help='Ruta del backup de seguridad para rollback')
    parser.add_argument('--no-safety', action='store_true', help='No crear backup de seguridad')
    
    args = parser.parse_args()
    
    manager = RestoreManager()
    
    if args.action == 'list':
        result = manager.list_available_backups()
        if result['success']:
            print("📋 BACKUPS DISPONIBLES")
            print("=" * 60)
            print(f"Total: {result['total_backups']} backups\n")
            
            for backup in result['backups']:
                print(f"📁 {backup['filename']}")
                print(f"   Tipo: {backup['type']}")
                print(f"   Tamaño: {backup['size_mb']} MB")
                print(f"   Fecha: {backup['modified']}")
                print()
        else:
            print(f"❌ Error: {result['error']}")
    
    elif args.action == 'preview':
        if not args.backup:
            print("❌ Error: Se requiere --backup")
            return
        
        result = manager.preview_backup_contents(args.backup)
        if result['success']:
            print(f"📋 CONTENIDO DE BACKUP: {args.backup}")
            print("=" * 60)
            print(f"Total archivos: {result['total_files']}\n")
            
            for content in result['contents']:
                print(f"📄 {content['filename']}")
                print(f"   Tamaño: {content['size_kb']} KB")
                print(f"   Comprimido: {content['compressed_size']} bytes")
                print()
        else:
            print(f"❌ Error: {result['error']}")
    
    elif args.action == 'validate':
        if not args.backup:
            print("❌ Error: Se requiere --backup")
            return
        
        result = manager.validate_backup_integrity(args.backup)
        if result['success']:
            print(f"✅ BACKUP VÁLIDO: {args.backup}")
            print(f"   Archivos: {result['total_files']}")
            print(f"   Integridad: {result['integrity']}")
        else:
            print(f"❌ VALIDACIÓN FALLÓ: {result['error']}")
    
    elif args.action == 'restore':
        if not args.backup:
            print("❌ Error: Se requiere --backup")
            return
        
        create_safety = not args.no_safety
        result = manager.restore_with_validation(args.backup, create_safety)
        
        if result['success']:
            print("✅ RESTAURACIÓN COMPLETADA EXITOSAMENTE")
        else:
            print(f"❌ RESTAURACIÓN FALLÓ: {result.get('error', 'Desconocido')}")
    
    elif args.action == 'selective':
        if not args.backup or not args.files:
            print("❌ Error: Se requieren --backup y --files")
            return
        
        result = manager.selective_restore(args.backup, args.files)
        
        if result['success']:
            print(f"✅ RESTAURACIÓN SELECTIVA COMPLETADA")
            print(f"   Archivos restaurados: {len(result['restored_files'])}")
        else:
            print(f"❌ RESTAURACIÓN SELECTIVA FALLÓ: {result['error']}")
    
    elif args.action == 'rollback':
        if not args.safety_backup:
            print("❌ Error: Se requiere --safety-backup")
            return
        
        result = manager.rollback_restore(args.safety_backup)
        
        if result['success']:
            print("✅ ROLLBACK COMPLETADO EXITOSAMENTE")
        else:
            print(f"❌ ROLLBACK FALLÓ: {result['error']}")
    
    elif args.action == 'history':
        result = manager.get_restore_history()
        if result['success']:
            print("📋 HISTORIAL DE RESTAURACIONES")
            print("=" * 60)
            print(f"Total operaciones: {result['total_operations']}\n")
            
            for operation in result['recent_operations']:
                print(f"📅 {operation['timestamp']}")
                print(f"   Backup: {operation['backup_restored']}")
                print(f"   Safety backup: {operation['safety_backup']}")
                print(f"   Éxito: {'✅' if operation['restore_success'] else '❌'}")
                print(f"   Validación: {'✅' if operation['validation_success'] else '❌'}")
                print()

if __name__ == '__main__':
    main()