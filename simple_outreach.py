from pathlib import Path

outreach_dir = Path(__file__).parent / "outreach_data"
outreach_dir.mkdir(exist_ok=True)

targets = [
    {"blog": "Colombia Travel Blog", "email": "contacto@colombiatravelblog.com"},
    {"blog": "Viajeros Colombia", "email": "redaccion@viajeroscolombia.com"},
    {"blog": "Eje Cafetero Blog", "email": "info@ejecaferoblog.com"},
    {"blog": "Turismo Responsable", "email": "contacto@turismoresponsable.co"},
    {"blog": "Rutas Colombia", "email": "contacto@rutascolombia.com"}
]

email_template = """Hola {name},

Soy Alvaro Alzate Ortiz, fundador de Quindío Travel (RNT 18152), operador turistico certificado con mas de 15 anos de experiencia en el Eje Cafetero.

Te escribo para proponer un articulo invitado de alta calidad sobre el Eje Cafetero para tu blog {blog_name}.

El articulo tendra 1,500+ palabras, optimizado para SEO, con informacion actualizada sobre:
- Guia Completa de Turismo Eje Cafetero 2026
- Experiencias Cafeteras Autenticas
- Precios reales y consejos para ahorrar

A cambio, incluire 2-3 enlaces contextuales a Quindío Travel (https://quindiotravel.com.co).

¿Te interesa recibir el borrador del articulo para revision?

Saludos cordiales,
Alvaro Alzate Ortiz
Quindío Travel - RNT 18152
+57-317-4426044
gerencia@quindiotravel.net"""

print("SISTEMA DE OUTREACH PARA BACKLINKS")
print("=" * 50)
print(f"Objetivos identificados: {len(targets)}")

# Generar emails personalizados
emails_generated = 0
for target in targets:
    email_content = email_template.format(
        name="Equipo Editorial",
        blog_name=target["blog"]
    )
    
    # Guardar email
    email_file = outreach_dir / f"email_{target['blog'].replace(' ', '_').lower()}.txt"
    with open(email_file, 'w', encoding='utf-8') as f:
        f.write(f"PARA: {target['email']}\n")
        f.write(f"BLOG: {target['blog']}\n")
        f.write(f"ASUNTO: Propuesta de Articulo Invitado - {target['blog']}\n\n")
        f.write(email_content)
    
    emails_generated += 1
    print(f"Email generado para: {target['blog']}")

# Guardar resumen
summary_file = outreach_dir / "outreach_summary.txt"
with open(summary_file, 'w', encoding='utf-8') as f:
    f.write("CAMPAÑA DE OUTREACH - QUINDÍO TRAVEL\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Total objetivos: {len(targets)}\n")
    f.write(f"Emails generados: {emails_generated}\n\n")
    f.write("OBJETIVOS:\n")
    for target in targets:
        f.write(f"- {target['blog']}: {target['email']}\n")
    f.write("\nRESULTADOS ESPERADOS:\n")
    f.write("- Tasa de respuesta: 5-10%\n")
    f.write("- Backlinks esperados: 0.25-0.5 en 30 dias\n")
    f.write("- DA Mejora: +5-10 puntos en 6 meses\n")

print(f"\nEmails generados: {emails_generated}")
print(f"Archivos guardados en: {outreach_dir}")
print(f"Resumen guardado en: {summary_file}")

print("\nRESULTADOS ESPERADOS:")
print("- Tasa de respuesta: 5-10%")
print("- Backlinks esperados: 0.25-0.5 en 30 dias")
print("- DA Mejora: +5-10 puntos en 6 meses")