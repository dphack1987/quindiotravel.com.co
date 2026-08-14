from PIL import Image
import os

# Imágenes grandes en alojamientos
alojamientos_images = [
    r"C:\Users\Gloria\Documents\www.quindiotravel.com\assets\images\alojamientos\cafetal.jpg",
    r"C:\Users\Gloria\Documents\www.quindiotravel.com\assets\images\alojamientos\hotel-campestre-cafe-cafe\IMG_0404-scaled.jpg",
    r"C:\Users\Gloria\Documents\www.quindiotravel.com\assets\images\alojamientos\hotel-campestre-cafe-cafe\IMG_5053-scaled.jpg",
    r"C:\Users\Gloria\Documents\www.quindiotravel.com\assets\images\alojamientos\hotel-campestre-la-tata\tata-anato-05-mp8qjeDV0DsVvyyX.webp"
]

def optimize_image(image_path, quality=85, max_width=1920):
    try:
        img = Image.open(image_path)
        original_size = os.path.getsize(image_path)
        width, height = img.size

        if img.mode != 'RGB':
            img = img.convert('RGB')

        if width > max_width:
            ratio = max_width / width
            new_height = int(height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Determinar formato de salida basado en extensión original
        ext = os.path.splitext(image_path)[1].lower()
        if ext == '.webp':
            temp_path = image_path + "_temp.webp"
            img.save(temp_path, "WEBP", quality=quality, optimize=True)
        else:
            temp_path = image_path + "_temp.jpg"
            img.save(temp_path, "JPEG", quality=quality, optimize=True)

        optimized_size = os.path.getsize(temp_path)
        reduction = (1 - optimized_size / original_size) * 100

        os.remove(image_path)
        os.rename(temp_path, image_path)

        return True, original_size, optimized_size, reduction

    except Exception as e:
        return False, 0, 0, 0

def main():
    success_count = 0
    failed_count = 0

    for image_path in alojamientos_images:
        if os.path.exists(image_path):
            success, orig, opt, red = optimize_image(image_path)
            if success:
                success_count += 1
                print(f"OK: {os.path.basename(image_path)} - {orig/(1024*1024):.1f}MB -> {opt/(1024*1024):.1f}MB ({red:.1f}%)")
            else:
                failed_count += 1
                print(f"FAIL: {os.path.basename(image_path)}")
        else:
            print(f"NOT FOUND: {image_path}")
            failed_count += 1

    print(f"\nSuccess: {success_count}, Failed: {failed_count}")

if __name__ == "__main__":
    main()