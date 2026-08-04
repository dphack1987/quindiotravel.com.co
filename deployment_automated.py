"""
Script de Despliegue Automatizado para Quindío Travel
Sube archivos críticos al servidor automáticamente
"""

import os
import sys
import getpass
from pathlib import Path
from ftplib import FTP, error_perm
import time
from datetime import datetime

class DeploymentAutomated:
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.files_to_upload = [
            "sitemap.xml",
            "llms.txt", 
            "robots.txt",
            "index.html"
        ]
        self.well_known_file = ".well-known/ai-metadata.json"
        self.remote_dir = None
        self.ftp = None
        self.log = []
        
    def log_message(self, message):
        """Agrega mensaje al log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.log.append(log_entry)
        print(log_entry)
        
    def get_credentials(self):
        """Obtiene credenciales FTP de variables de entorno o argumentos"""
        import os
        
        print("=" * 60)
        print("CREDENCIALES FTP/SFTP PARA DESPLIEGUE")
        print("=" * 60)
        
        # Intentar obtener de variables de entorno
        self.host = os.environ.get('FTP_HOST', '')
        self.username = os.environ.get('FTP_USER', '')
        self.password = os.environ.get('FTP_PASSWORD', '')
        self.port = os.environ.get('FTP_PORT', '21')
        self.remote_dir = os.environ.get('FTP_DIR', 'public_html')
        
        if not self.host or not self.username or not self.password:
            print("\nERROR: Credenciales no proporcionadas")
            print("Por favor configura las variables de entorno:")
            print("FTP_HOST=quindiotravel.com.co")
            print("FTP_USER=tu_usuario")
            print("FTP_PASSWORD=tu_contraseña")
            print("FTP_PORT=21 (opcional)")
            print("FTP_DIR=public_html (opcional)")
            print("\nEjemplo:")
            print("set FTP_HOST=quindiotravel.com.co")
            print("set FTP_USER=tu_usuario")
            print("set FTP_PASSWORD=tu_contraseña")
            print("python deployment_automated.py")
            return False
            
        if not self.port:
            self.port = 21
        else:
            self.port = int(self.port)
            
        print("\nVerificando credenciales...")
        print(f"Host: {self.host}")
        print(f"Usuario: {self.username}")
        print(f"Puerto: {self.port}")
        print(f"Directorio: {self.remote_dir}")
        
        return True
        
    def connect_ftp(self):
        """Conecta al servidor FTP"""
        try:
            self.log_message("Conectando al servidor FTP...")
            self.ftp = FTP()
            self.ftp.connect(self.host, self.port, timeout=30)
            self.ftp.login(self.username, self.password)
            self.log_message("Conexión FTP exitosa")
            return True
        except Exception as e:
            self.log_message(f"Error de conexión FTP: {e}")
            return False
            
    def navigate_to_directory(self):
        """Navega al directorio remoto correcto"""
        try:
            self.log_message(f"Navegando a directorio: {self.remote_dir}")
            self.ftp.cwd(self.remote_dir)
            self.log_message("Directorio remoto establecido")
            return True
        except error_perm as e:
            self.log_message(f"Error navegando al directorio: {e}")
            self.log_message("Intentando crear directorio...")
            try:
                self.ftp.mkd(self.remote_dir)
                self.ftp.cwd(self.remote_dir)
                self.log_message("Directorio creado y establecido")
                return True
            except Exception as e2:
                self.log_message(f"Error creando directorio: {e2}")
                return False
        except Exception as e:
            self.log_message(f"Error inesperado: {e}")
            return False
            
    def verify_local_files(self):
        """Verifica que los archivos locales existan"""
        self.log_message("Verificando archivos locales...")
        
        all_exist = True
        for file_name in self.files_to_upload:
            file_path = self.root_dir / file_name
            if file_path.exists():
                size = os.path.getsize(file_path)
                self.log_message(f"[OK] {file_name} ({size} bytes)")
            else:
                self.log_message(f"[X] {file_name} (NO EXISTE)")
                all_exist = False
                
        # Verificar archivo .well-known
        well_known_path = self.root_dir / ".well-known" / "ai-metadata.json"
        if well_known_path.exists():
            size = os.path.getsize(well_known_path)
            self.log_message(f"[OK] .well-known/ai-metadata.json ({size} bytes)")
        else:
            self.log_message(f"[X] .well-known/ai-metadata.json (NO EXISTE)")
            all_exist = False
            
        return all_exist
        
    def upload_file(self, local_path, remote_path):
        """Sube un archivo al servidor"""
        try:
            with open(local_path, 'rb') as f:
                self.ftp.storbinary(f'STOR {remote_path}', f)
            self.log_message(f"[OK] Subido: {remote_path}")
            return True
        except Exception as e:
            self.log_message(f"[X] Error subiendo {remote_path}: {e}")
            return False
            
    def create_well_known_directory(self):
        """Crea directorio .well-known si no existe"""
        try:
            self.log_message("Verificando directorio .well-known...")
            try:
                self.ftp.cwd('.well-known')
                self.ftp.cwd('..')  # Volver al directorio raíz
                self.log_message("Directorio .well-known ya existe")
                return True
            except error_perm:
                self.log_message("Creando directorio .well-known...")
                self.ftp.mkd('.well-known')
                self.log_message("Directorio .well-known creado")
                return True
        except Exception as e:
            self.log_message(f"Error creando .well-known: {e}")
            return False
            
    def upload_files(self):
        """Sube todos los archivos críticos"""
        self.log_message("Iniciando subida de archivos...")
        
        uploaded_count = 0
        failed_count = 0
        
        # Subir archivos principales
        for file_name in self.files_to_upload:
            local_path = self.root_dir / file_name
            if local_path.exists():
                success = self.upload_file(local_path, file_name)
                if success:
                    uploaded_count += 1
                else:
                    failed_count += 1
                    
        # Crear directorio .well-known y subir archivo
        if self.create_well_known_directory():
            well_known_path = self.root_dir / ".well-known" / "ai-metadata.json"
            if well_known_path.exists():
                success = self.upload_file(well_known_path, '.well-known/ai-metadata.json')
                if success:
                    uploaded_count += 1
                else:
                    failed_count += 1
            else:
                self.log_message("✗ .well-known/ai-metadata.json no existe localmente")
                failed_count += 1
        else:
            failed_count += 1
            
        self.log_message(f"\nResumen de subida: {uploaded_count} exitosos, {failed_count} fallidos")
        return failed_count == 0
        
    def verify_remote_files(self):
        """Verifica que los archivos existan en el servidor"""
        self.log_message("Verificando archivos en servidor...")
        
        try:
            files_on_server = self.ftp.nlst()
            
            # Verificar archivos principales
            for file_name in self.files_to_upload:
                if file_name in files_on_server:
                    self.log_message(f"[OK] {file_name} existe en servidor")
                else:
                    self.log_message(f"[X] {file_name} NO existe en servidor")
                    
            # Verificar .well-known
            try:
                self.ftp.cwd('.well-known')
                well_known_files = self.ftp.nlst()
                if 'ai-metadata.json' in well_known_files:
                    self.log_message("[OK] .well-known/ai-metadata.json existe en servidor")
                else:
                    self.log_message("[X] .well-known/ai-metadata.json NO existe en servidor")
                self.ftp.cwd('..')
            except:
                self.log_message("[X] Error verificando .well-known")
                
            return True
        except Exception as e:
            self.log_message(f"Error verificando archivos: {e}")
            return False
            
    def generate_report(self):
        """Genera reporte de despliegue"""
        report_file = self.root_dir / "deployment_report.txt"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("REPORTE DE DESPLIEGUE - Quindío Travel\n")
            f.write("=" * 60 + "\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Host: {self.host}\n")
            f.write(f"Directorio: {self.remote_dir}\n")
            f.write("\nLOG DE DESPLIEGUE:\n")
            f.write("=" * 60 + "\n")
            
            for log_entry in self.log:
                f.write(log_entry + "\n")
                
            f.write("\n" + "=" * 60 + "\n")
            f.write("ARCHIVOS SUBIDOS:\n")
            f.write("- sitemap.xml\n")
            f.write("- llms.txt\n")
            f.write("- robots.txt\n")
            f.write("- index.html\n")
            f.write("- .well-known/ai-metadata.json\n")
            f.write("\n" + "=" * 60 + "\n")
            f.write("VERIFICACIÓN POST-DESPLEGUE:\n")
            f.write("https://quindiotravel.com.co/sitemap.xml\n")
            f.write("https://quindiotravel.com.co/llms.txt\n")
            f.write("https://quindiotravel.com.co/robots.txt\n")
            f.write("https://quindiotravel.com.co/.well-known/ai-metadata.json\n")
            
        self.log_message(f"Reporte generado: {report_file}")
        
    def disconnect(self):
        """Desconecta del servidor FTP"""
        if self.ftp:
            try:
                self.ftp.quit()
                self.log_message("Desconexión FTP exitosa")
            except:
                self.ftp.close()
                self.log_message("Desconexión FTP forzada")
                
    def run(self):
        """Ejecuta el proceso completo de despliegue"""
        print("\n" + "=" * 60)
        print("SCRIPT DE DESPLIEGUE AUTOMATIZADO - Quindío Travel")
        print("=" * 60)
        
        try:
            # Paso 1: Obtener credenciales
            if not self.get_credentials():
                print("Error obteniendo credenciales")
                return False
                
            # Paso 2: Verificar archivos locales
            if not self.verify_local_files():
                print("Error: Algunos archivos locales faltan")
                return False
                
            # Paso 3: Conectar al servidor
            if not self.connect_ftp():
                print("Error conectando al servidor")
                return False
                
            # Paso 4: Navegar al directorio
            if not self.navigate_to_directory():
                print("Error navegando al directorio")
                self.disconnect()
                return False
                
            # Paso 5: Subir archivos
            if not self.upload_files():
                print("Error subiendo archivos")
                self.disconnect()
                return False
                
            # Paso 6: Verificar archivos en servidor
            self.verify_remote_files()
            
            # Paso 7: Generar reporte
            self.generate_report()
            
            # Paso 8: Desconectar
            self.disconnect()
            
            print("\n" + "=" * 60)
            print("DESPLIEGUE COMPLETADO EXITOSAMENTE")
            print("=" * 60)
            print("\nPRÓXIMO PASO:")
            print("1. Verificar URLs en navegador:")
            print("   https://quindiotravel.com.co/sitemap.xml")
            print("   https://quindiotravel.com.co/llms.txt")
            print("   https://quindiotravel.com.co/robots.txt")
            print("   https://quindiotravel.com.co/.well-known/ai-metadata.json")
            print("\n2. Someter sitemap a Google Search Console")
            print("3. Actualizar LinkedIn con credenciales")
            
            return True
            
        except KeyboardInterrupt:
            print("\nProceso interrumpido por usuario")
            self.disconnect()
            return False
        except Exception as e:
            print(f"\nError inesperado: {e}")
            self.disconnect()
            return False

if __name__ == "__main__":
    print("\n[!] IMPORTANTE: Este script requiere credenciales FTP del servidor")
    print("   Las credenciales son informacion sensible y no se guardaran")
    print("   Solo se usaran durante la ejecucion del script\n")
    
    deployer = DeploymentAutomated()
    success = deployer.run()
    
    if success:
        print("\n✓ Despliegue completado exitosamente")
        sys.exit(0)
    else:
        print("\n✗ Despliegue falló")
        sys.exit(1)