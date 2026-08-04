from pathlib import Path

project_root = Path(__file__).parent

# Count generated pages
generated_pages = list(project_root.glob("generated-pages/**/*.html"))
print(f"Generated pages total: {len(generated_pages)}")

# Count by subdirectory
armenia_pages = list(project_root.glob("generated-pages/armenia/**/*.html"))
alojamiento_pages = list(project_root.glob("generated-pages/alojamiento/*.html"))

print(f"Armenia pages: {len(armenia_pages)}")
print(f"Alojamiento pages: {len(alojamiento_pages)}")

# Total expected
total_generated = len(generated_pages)
print(f"Total generated pages: {total_generated}")

# Previous count was 172, so expected new total
previous_total = 172
new_total = previous_total + total_generated
print(f"Previous total: {previous_total}")
print(f"New total with generated pages: {new_total}")