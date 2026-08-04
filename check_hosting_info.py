"""
Script para identificar tipo de hosting de quindiotravel.com.co
"""

import subprocess
import re

def check_dns_info():
    """Verifica información DNS del dominio"""
    
    domain = "quindiotravel.com.co"
    
    print(f"Verificando información DNS para: {domain}")
    print("=" * 60)
    
    try:
        # Verificar registros A
        result = subprocess.run(['nslookup', domain], capture_output=True, text=True)
        print("Registros A:")
        print(result.stdout)
        
        # Verificar registros MX
        result_mx = subprocess.run(['nslookup', '-type=mx', domain], capture_output=True, text=True)
        print("\nRegistros MX:")
        print(result_mx.stdout)
        
        # Verificar WHOIS (si está disponible)
        try:
            result_whois = subprocess.run(['whois', domain], capture_output=True, text=True, timeout=10)
            print("\nInformación WHOIS:")
            # Extraer información relevante
            if 'Registrar:' in result_whois.stdout:
                registrar = re.search(r'Registrar:\s*(.+)', result_whois.stdout)
                if registrar:
                    print(f"Registrador: {registrar.group(1)}")
            if 'Name Server:' in result_whois.stdout:
                nameservers = re.findall(r'Name Server:\s*(.+)', result_whois.stdout)
                if nameservers:
                    print(f"Nameservers: {', '.join(nameservers)}")
        except:
            print("WHOIS no disponible en este sistema")
            
    except Exception as e:
        print(f"Error verificando DNS: {e}")

if __name__ == "__main__":
    check_dns_info()