"""
Script de Instalación Fácil - Lead Automation System
Instalación automatizada del sistema con verificación de dependencias
"""

import sys
import os
import subprocess
from typing import Dict, List

class Installer:
    """Instalador automatizado del sistema"""
    
    def __init__(self):
        self.python_version = sys.version_info
        self.requirements_file = 'requirements.txt'
        self.verification_results = {}
    
    def check_python_version(self) -> Dict:
        """Verificar versión de Python"""
        print("🐍 Verificando versión de Python...")
        
        min_version = (3, 8)
        current_version = (self.python_version.major, self.python_version.minor)
        
        if current_version >= min_version:
            print(f"✅ Python {current_version[0]}.{current_version[1]} - Versión compatible")
            return {
                'success': True,
                'version': f"{current_version[0]}.{current_version[1]}",
                'compatible': True
            }
        else:
            print(f"❌ Python {current_version[0]}.{current_version[1]} - Versión incompatible")
            print(f"   Requerido: Python {min_version[0]}.{min_version[1]}+")
            return {
                'success': False,
                'version': f"{current_version[0]}.{current_version[1]}",
                'compatible': False,
                'required': f"{min_version[0]}.{min_version[1]}+"
            }
    
    def check_file_structure(self) -> Dict:
        """Verificar estructura de archivos del sistema"""
        print("📁 Verificando estructura de archivos...")
        
        required_files = [
            'main.py',
            'config.py',
            'requirements.txt',
            'README.md'
        ]
        
        required_dirs = [
            'modules',
            'data',
            'utils',
            'tests'
        ]
        
        missing_files = []
        missing_dirs = []
        
        for file in required_files:
            if not os.path.exists(file):
                missing_files.append(file)
        
        for dir in required_dirs:
            if not os.path.exists(dir):
                missing_dirs.append(dir)
        
        if not missing_files and not missing_dirs:
            print("✅ Estructura de archivos completa")
            return {
                'success': True,
                'missing_files': [],
                'missing_dirs': []
            }
        else:
            print("⚠️  Estructura de archivos incompleta:")
            if missing_files:
                print(f"   Archivos faltantes: {', '.join(missing_files)}")
            if missing_dirs:
                print(f"   Directorios faltantes: {', '.join(missing_dirs)}")
            
            return {
                'success': False,
                'missing_files': missing_files,
                'missing_dirs': missing_dirs
            }
    
    def install_dependencies(self) -> Dict:
        """Instalar dependencias desde requirements.txt"""
        print("📦 Instalando dependencias...")
        
        if not os.path.exists(self.requirements_file):
            print(f"❌ Archivo {self.requirements_file} no encontrado")
            return {
                'success': False,
                'error': 'requirements.txt no encontrado'
            }
        
        try:
            # Verificar si pip está disponible
            subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                         check=True, capture_output=True)
            
            # Instalar dependencias
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'install', '-r', self.requirements_file],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("✅ Dependencias instaladas exitosamente")
                return {
                    'success': True,
                    'output': result.stdout
                }
            else:
                print(f"❌ Error al instalar dependencias:")
                print(result.stderr)
                return {
                    'success': False,
                    'error': result.stderr
                }
        
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al verificar pip: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def create_data_structure(self) -> Dict:
        """Crear estructura de datos si no existe"""
        print("📂 Creando estructura de datos...")
        
        data_dirs = [
            'data',
            'data/backups',
            'data/exports',
            'data/reports',
            'utils'
        ]
        
        created_dirs = []
        
        for dir_path in data_dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                created_dirs.append(dir_path)
        
        # Crear archivos de datos base si no existen
        data_files = {
            'data/leads_db.json': '[]',
            'data/conversion_data.json': '[]',
            'data/scoring_rules.json': '''{
  "interest_signals": {
    "specific_plan_mentioned": 15,
    "date_range_provided": 12,
    "guest_count_provided": 10,
    "budget_mentioned": 12,
    "question_asked": 8,
    "whatsapp_clicked": 20
  },
  "quality_signals": {
    "complete_sentence": 5,
    "relevant_destination": 10,
    "reasonable_budget": 15,
    "realistic_dates": 10,
    "contact_provided": 8
  },
  "behavioral_signals": {
    "page_views": 2,
    "time_on_site": 3,
    "return_visitor": 15,
    "mobile_device": 5,
    "desktop_device": 7
  },
  "timing_signals": {
    "response_under_1hr": 10,
    "response_1_24hr": 5,
    "response_24_72hr": 2,
    "weekend_inquiry": 8,
    "holiday_season": 12
  }
}'''
        }
        
        created_files = []
        
        for file_path, content in data_files.items():
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                created_files.append(file_path)
        
        if created_dirs or created_files:
            print(f"✅ Estructura creada:")
            if created_dirs:
                print(f"   Directorios: {len(created_dirs)}")
            if created_files:
                print(f"   Archivos: {len(created_files)}")
            
            return {
                'success': True,
                'created_dirs': created_dirs,
                'created_files': created_files
            }
        else:
            print("✅ Estructura de datos ya existe")
            return {
                'success': True,
                'created_dirs': [],
                'created_files': []
            }
    
    def run_system_tests(self) -> Dict:
        """Ejecutar pruebas del sistema"""
        print("🧪 Ejecutando pruebas del sistema...")
        
        try:
            result = subprocess.run(
                [sys.executable, 'run_tests.py', '--quick'],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                print("✅ Pruebas del sistema pasadas")
                return {
                    'success': True,
                    'output': result.stdout
                }
            else:
                print("⚠️  Algunas pruebas fallaron:")
                print(result.stdout)
                print(result.stderr)
                return {
                    'success': False,
                    'output': result.stdout,
                    'error': result.stderr
                }
        
        except subprocess.TimeoutExpired:
            print("⚠️  Pruebas excedieron tiempo límite")
            return {
                'success': False,
                'error': 'Timeout'
            }
        except Exception as e:
            print(f"❌ Error al ejecutar pruebas: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def generate_env_file(self) -> Dict:
        """Generar archivo .env de ejemplo"""
        print("🔧 Generando archivo .env de ejemplo...")
        
        env_content = """# WhatsApp Business API Configuration
WHATSAPP_API_TOKEN=tu_token_aqui
WHATSAPP_BUSINESS_ID=tu_business_id_aqui

# Sistema Configuration
LEAD_AUTOMATION_MODE=interactive
LOG_LEVEL=INFO
DEBUG=False
"""
        
        env_example_path = '.env.example'
        
        with open(env_example_path, 'w', encoding='utf-8') as f:
            f.write(env_content)
        
        print(f"✅ Archivo {env_example_path} creado")
        print("   Configura tus tokens en .env basado en el ejemplo")
        
        return {
            'success': True,
            'env_file': env_example_path
        }
    
    def create_initial_backup(self) -> Dict:
        """Crear backup inicial del sistema"""
        print("💾 Creando backup inicial...")
        
        try:
            from utils.data_manager import DataManager
            manager = DataManager()
            result = manager.backup_all_data()
            
            if result['success']:
                print(f"✅ Backup inicial creado: {result['filename']}")
                return result
            else:
                print(f"⚠️  No se pudo crear backup inicial: {result['error']}")
                return result
        
        except Exception as e:
            print(f"⚠️  Error al crear backup inicial: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def run_full_installation(self) -> Dict:
        """Ejecutar instalación completa del sistema"""
        print("🚀 INICIANDO INSTALACIÓN COMPLETA")
        print("=" * 60)
        
        installation_results = {
            'python_version': self.check_python_version(),
            'file_structure': self.check_file_structure(),
            'data_structure': self.create_data_structure(),
            'dependencies': self.install_dependencies(),
            'env_file': self.generate_env_file(),
            'system_tests': self.run_system_tests(),
            'initial_backup': self.create_initial_backup()
        }
        
        print("\n" + "=" * 60)
        print("📊 RESUMEN DE INSTALACIÓN")
        print("=" * 60)
        
        # Mostrar resumen
        results_summary = []
        
        for step, result in installation_results.items():
            status = "✅" if result.get('success') else "❌"
            step_name = step.replace('_', ' ').title()
            results_summary.append(f"{status} {step_name}")
        
        for summary in results_summary:
            print(summary)
        
        # Verificar si instalación fue exitosa
        critical_success = all([
            installation_results['python_version']['success'],
            installation_results['file_structure']['success'],
            installation_results['dependencies']['success']
        ])
        
        if critical_success:
            print("\n🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!")
            print("\n📝 PRÓXIMOS PASOS:")
            print("1. Configurar archivo .env con tus tokens de WhatsApp")
            print("2. Ejecutar: python main.py")
            print("3. Seleccionar modo interactivo para primera prueba")
            print("4. Abrir dashboard.html para monitoreo")
            
            return {
                'success': True,
                'installation_results': installation_results
            }
        else:
            print("\n❌ INSTALACIÓN INCOMPLETA")
            print("Revisa los errores arriba y soluciona los problemas críticos")
            
            return {
                'success': False,
                'installation_results': installation_results
            }

def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Instalador del Sistema de Automatización de Leads')
    parser.add_argument('--step', choices=['check', 'deps', 'structure', 'tests', 'full'],
                       default='full', help='Paso específico de instalación')
    
    args = parser.parse_args()
    
    installer = Installer()
    
    if args.step == 'check':
        installer.check_python_version()
        installer.check_file_structure()
    elif args.step == 'deps':
        installer.install_dependencies()
    elif args.step == 'structure':
        installer.create_data_structure()
    elif args.step == 'tests':
        installer.run_system_tests()
    elif args.step == 'full':
        result = installer.run_full_installation()
        sys.exit(0 if result['success'] else 1)

if __name__ == '__main__':
    main()