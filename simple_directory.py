from pathlib import Path

directories = [
    {"name": "Google My Business", "url": "https://business.google.com", "priority": "ALTA"},
    {"name": "TripAdvisor Colombia", "url": "https://www.tripadvisor.com.co", "priority": "ALTA"},
    {"name": "Ministerio de Turismo", "url": "https://www.mincit.gov.co", "priority": "ALTA"},
    {"name": "Turismo Quindío", "url": "https://www.quindio.gov.co", "priority": "ALTA"},
    {"name": "Bing Places", "url": "https://www.bingplaces.com", "priority": "MEDIA"},
    {"name": "Yelp Colombia", "url": "https://www.yelp.com.co", "priority": "MEDIA"},
    {"name": "Foursquare", "url": "https://foursquare.com", "priority": "MEDIA"},
    {"name": "Booking.com", "url": "https://www.booking.com", "priority": "BAJA"},
    {"name": "Expedia", "url": "https://www.expedia.com.co", "priority": "BAJA"},
    {"name": "Despegar", "url": "https://www.despegar.com.co", "priority": "BAJA"}
]

alta = [d for d in directories if d["priority"] == "ALTA"]
media = [d for d in directories if d["priority"] == "MEDIA"]
baja = [d for d in directories if d["priority"] == "BAJA"]

print("SISTEMA DE DIRECTORIOS GRATUITOS")
print("=" * 50)
print(f"Total directorios: {len(directories)}")
print(f"Prioridad ALTA: {len(alta)}")
print(f"Prioridad MEDIA: {len(media)}")
print(f"Prioridad BAJA: {len(baja)}")
print("\nPRIORIDAD ALTA (iniciar con estos):")
for d in alta:
    print(f"- {d['name']}: {d['url']}")

print("\nRESULTADOS ESPERADOS:")
print("- Backlinks: 10 enlaces gratuitos")
print("- DA Mejora: +15-25 puntos en 6 meses")
print("- Visibilidad Local: +200% en busquedas locales")

# Guardar reporte
report_dir = Path(__file__).parent / "directories_data"
report_dir.mkdir(exist_ok=True)

with open(report_dir / "directory_plan.txt", 'w', encoding='utf-8') as f:
    f.write("PLAN DE DIRECTORIOS GRATUITOS\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Total directorios: {len(directories)}\n\n")
    f.write("PRIORIDAD ALTA:\n")
    for d in alta:
        f.write(f"- {d['name']}: {d['url']}\n")
    f.write("\nPRIORIDAD MEDIA:\n")
    for d in media:
        f.write(f"- {d['name']}: {d['url']}\n")
    f.write("\nPRIORIDAD BAJA:\n")
    for d in baja:
        f.write(f"- {d['name']}: {d['url']}\n")

print("\nReporte guardado en directories_data/directory_plan.txt")