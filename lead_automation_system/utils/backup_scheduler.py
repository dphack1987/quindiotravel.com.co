"""
Programador de Backups Automatizados
Sistema para crear backups automáticos del sistema de leads
"""

import os
import sys
from datetime import datetime, timedelta
import schedule
import time
from data_manager import DataManager

class BackupScheduler:
    """Programador de backups automáticos"""
    
    def __init__(self, data_manager: DataManager = None):
        self.data_manager = data_manager or DataManager()
        self.backup_schedule = {
            'daily': {'time': '02:00', 'keep_days': 7},
            'weekly': {'day': 'sunday', 'time': '03:00', 'keep_weeks': 4},
            'monthly': {'day': 1, 'time': '04:00', 'keep_months': 6}
        }
    
    def create_daily_backup(self):
        """Crear backup diario"""
        print(f"🔄 Creando backup diario - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        result = self.data_manager.backup_all_data()
        
        if result['success']:
            print(f"✅ Backup diario creado: {result['filename']}")
            print(f"📊 Tamaño: {result['size_mb']} MB")
            
            # Limpiar backups antiguos (mantener 7 días)
            cleanup_result = self.data_manager.clean_old_backups(days_to_keep=7)
            if cleanup_result['success']:
                print(f"🗑️  Backups antiguos eliminados: {cleanup_result['deleted_files']} archivos")
                print(f"💾 Espacio liberado: {cleanup_result['total_size_freed_mb']} MB")
        else:
            print(f"❌ Error al crear backup diario: {result['error']}")
        
        return result
    
    def create_weekly_backup(self):
        """Crear backup semanal"""
        print(f"🔄 Creando backup semanal - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        result = self.data_manager.backup_all_data()
        
        if result['success']:
            # Renombrar para indicar que es semanal
            original_path = result['backup_path']
            weekly_filename = f"weekly_backup_{datetime.now().strftime('%Y%m%d')}.zip"
            weekly_path = os.path.join(self.data_manager.backup_dir, weekly_filename)
            
            try:
                os.rename(original_path, weekly_path)
                print(f"✅ Backup semanal creado: {weekly_filename}")
                print(f"📊 Tamaño: {result['size_mb']} MB")
                
                # Limpiar backups semanales antiguos (mantener 4 semanas)
                self._clean_weekly_backups(keep_weeks=4)
            except Exception as e:
                print(f"❌ Error al renombrar backup semanal: {str(e)}")
        else:
            print(f"❌ Error al crear backup semanal: {result['error']}")
        
        return result
    
    def create_monthly_backup(self):
        """Crear backup mensual"""
        print(f"🔄 Creando backup mensual - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        result = self.data_manager.backup_all_data()
        
        if result['success']:
            # Renombrar para indicar que es mensual
            original_path = result['backup_path']
            monthly_filename = f"monthly_backup_{datetime.now().strftime('%Y%m')}.zip"
            monthly_path = os.path.join(self.data_manager.backup_dir, monthly_filename)
            
            try:
                os.rename(original_path, monthly_path)
                print(f"✅ Backup mensual creado: {monthly_filename}")
                print(f"📊 Tamaño: {result['size_mb']} MB")
                
                # Limpiar backups mensuales antiguos (mantener 6 meses)
                self._clean_monthly_backups(keep_months=6)
            except Exception as e:
                print(f"❌ Error al renombrar backup mensual: {str(e)}")
        else:
            print(f"❌ Error al crear backup mensual: {result['error']}")
        
        return result
    
    def _clean_weekly_backups(self, keep_weeks: int = 4):
        """Limpiar backups semanales antiguos"""
        cutoff_date = datetime.now() - timedelta(weeks=keep_weeks)
        deleted_files = []
        
        for filename in os.listdir(self.data_manager.backup_dir):
            if filename.startswith('weekly_backup_') and filename.endswith('.zip'):
                file_path = os.path.join(self.data_manager.backup_dir, filename)
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                if file_time < cutoff_date:
                    os.remove(file_path)
                    deleted_files.append(filename)
        
        if deleted_files:
            print(f"🗑️  Backups semanales antiguos eliminados: {len(deleted_files)} archivos")
    
    def _clean_monthly_backups(self, keep_months: int = 6):
        """Limpiar backups mensuales antiguos"""
        cutoff_date = datetime.now() - timedelta(days=keep_months * 30)
        deleted_files = []
        
        for filename in os.listdir(self.data_manager.backup_dir):
            if filename.startswith('monthly_backup_') and filename.endswith('.zip'):
                file_path = os.path.join(self.data_manager.backup_dir, filename)
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                if file_time < cutoff_date:
                    os.remove(file_path)
                    deleted_files.append(filename)
        
        if deleted_files:
            print(f"🗑️  Backups mensuales antiguos eliminados: {len(deleted_files)} archivos")
    
    def schedule_all_backups(self):
        """Programar todos los tipos de backups"""
        print("🗓️  Programando sistema de backups automáticos")
        print("=" * 60)
        
        # Backup diario a las 2 AM
        schedule.every().day.at(self.backup_schedule['daily']['time']).do(self.create_daily_backup)
        print(f"📅 Backup diario programado: {self.backup_schedule['daily']['time']}")
        
        # Backup semanal los domingos a las 3 AM
        schedule.every().sunday.at(self.backup_schedule['weekly']['time']).do(self.create_weekly_backup)
        print(f"📅 Backup semanal programado: domingos a {self.backup_schedule['weekly']['time']}")
        
        # Backup mensual el día 1 a las 4 AM
        schedule.every().month.do(self.create_monthly_backup)
        print(f"📅 Backup mensual programado: día 1 a {self.backup_schedule['monthly']['time']}")
        
        print("=" * 60)
        print("🔄 Sistema de backups activo. Presiona Ctrl+C para detener.")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Verificar cada minuto
        except KeyboardInterrupt:
            print("\n👋 Sistema de backups detenido por el usuario")
    
    def run_immediate_backup(self, backup_type: str = 'daily'):
        """Ejecutar backup inmediato de un tipo específico"""
        print(f"🔄 Ejecutando backup inmediato: {backup_type}")
        
        if backup_type == 'daily':
            return self.create_daily_backup()
        elif backup_type == 'weekly':
            return self.create_weekly_backup()
        elif backup_type == 'monthly':
            return self.create_monthly_backup()
        else:
            print(f"❌ Tipo de backup desconocido: {backup_type}")
            return {'success': False, 'error': 'Tipo de backup desconocido'}
    
    def get_backup_status(self) -> dict:
        """Obtener estado actual de backups"""
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
                'backup_files': backup_files,
                'total_size_bytes': sum(f['size_bytes'] for f in backup_files),
                'total_size_mb': round(sum(f['size_bytes'] for f in backup_files) / (1024 * 1024), 2)
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

def main():
    """Función principal para ejecutar desde línea de comandos"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Sistema de backups automáticos')
    parser.add_argument('--mode', choices=['schedule', 'immediate', 'status'], 
                       default='immediate', help='Modo de ejecución')
    parser.add_argument('--type', choices=['daily', 'weekly', 'monthly'], 
                       default='daily', help='Tipo de backup')
    
    args = parser.parse_args()
    
    scheduler = BackupScheduler()
    
    if args.mode == 'schedule':
        scheduler.schedule_all_backups()
    elif args.mode == 'immediate':
        result = scheduler.run_immediate_backup(args.type)
        if result['success']:
            print(f"✅ Backup {args.type} completado exitosamente")
        else:
            print(f"❌ Error: {result.get('error', 'Desconocido')}")
    elif args.mode == 'status':
        status = scheduler.get_backup_status()
        if status['success']:
            print("📊 ESTADO DE BACKUPS")
            print("=" * 60)
            print(f"Total backups: {status['total_backups']}")
            print(f"Espacio total: {status['total_size_mb']} MB")
            print("\nBackups más recientes:")
            
            for backup in status['backup_files'][:10]:  # Mostrar los 10 más recientes
                print(f"  📁 {backup['filename']}")
                print(f"     Tipo: {backup['type']}")
                print(f"     Tamaño: {backup['size_mb']} MB")
                print(f"     Fecha: {backup['modified']}")
                print()
        else:
            print(f"❌ Error al obtener estado: {status['error']}")

if __name__ == '__main__':
    main()