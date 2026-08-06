#!/usr/bin/env python3
"""
Generador de Códigos QR para Quindío Travel
Genera QRs funcionales con branding y opciones de personalización
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import RadialGradientMask, SolidFillColorMask
from PIL import Image, ImageDraw, ImageFont
import os

# Configuración
SITE_URL = "https://quindiotravel.com.co"
OUTPUT_DIR = "assets/qr-codes"
BRAND_COLORS = {
    'primary': '#2E5A36',    # Verde café
    'secondary': '#8B4513',  # Marrón madera
    'accent': '#D4A574',     # Dorado café
    'white': '#FFFFFF',
    'black': '#000000'
}

def create_output_directory():
    """Crea el directorio de salida si no existe"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Directorio creado: {OUTPUT_DIR}")

def generate_basic_qr(url, filename="qr-basic.png"):
    """Genera un QR básico estándar"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"QR básico generado: {filename}")
    return img

def generate_branded_qr(url, filename="qr-branded.png"):
    """Genera un QR con colores de marca"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Usar colores de marca
    img = qr.make_image(
        fill_color=BRAND_COLORS['primary'],
        back_color="white"
    )
    img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"QR con marca generado: {filename}")
    return img

def generate_styled_qr(url, filename="qr-styled.png"):
    """Genera un QR con módulos redondeados y gradiente"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Crear QR con módulos redondeados
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradientMask(
            center_color=BRAND_COLORS['primary'],
            edge_color=BRAND_COLORS['secondary']
        )
    )
    img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"QR estilizado generado: {filename}")
    return img

def generate_qr_with_logo(url, logo_path, filename="qr-with-logo.png"):
    """Genera un QR con el logo de Quindío Travel en el centro"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=BRAND_COLORS['primary'], back_color="white")
    
    # Intentar agregar logo si existe
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        
        # Calcular tamaño del logo (aprox 20% del QR)
        qr_width, qr_height = img.size
        logo_size = min(qr_width, qr_height) // 5
        
        # Redimensionar logo
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Calcular posición central
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        
        # Pegar logo en el centro
        img.paste(logo, logo_pos, logo if logo.mode == 'RGBA' else None)
    
    img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"QR con logo generado: {filename}")
    return img

def generate_marketing_qr(url, filename="qr-marketing.png"):
    """Genera un QR listo para marketing con texto y branding"""
    # Generar QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color=BRAND_COLORS['primary'], back_color="white")
    
    # Crear imagen de marketing más grande
    marketing_img = Image.new('RGB', (400, 500), 'white')
    draw = ImageDraw.Draw(marketing_img)
    
    # Calcular posición del QR
    qr_width, qr_height = qr_img.size
    qr_x = (400 - qr_width) // 2
    qr_y = 50
    
    # Pegar QR
    marketing_img.paste(qr_img, (qr_x, qr_y))
    
    # Agregar texto "ESCANEA PARA PLANEAR TU VIAJE"
    try:
        # Intentar usar fuente del sistema
        font_large = ImageFont.truetype("arial.ttf", 24)
        font_small = ImageFont.truetype("arial.ttf", 16)
    except:
        # Fallback a fuente default
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Título
    title = "ESCANEA PARA PLANEAR"
    title_bbox = draw.textbbox((0, 0), title, font=font_large)
    title_x = (400 - (title_bbox[2] - title_bbox[0])) // 2
    draw.text((title_x, 20), title, fill=BRAND_COLORS['primary'], font=font_large)
    
    # Subtítulo
    subtitle = "Tu viaje al Eje Cafetero"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
    subtitle_x = (400 - (subtitle_bbox[2] - subtitle_bbox[0])) // 2
    draw.text((subtitle_x, qr_y + qr_height + 20), subtitle, fill=BRAND_COLORS['secondary'], font=font_small)
    
    # Nombre de la marca
    brand = "Quindío Travel"
    brand_bbox = draw.textbbox((0, 0), brand, font=font_large)
    brand_x = (400 - (brand_bbox[2] - brand_bbox[0])) // 2
    draw.text((brand_x, 450), brand, fill=BRAND_COLORS['primary'], font=font_large)
    
    marketing_img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"QR de marketing generado: {filename}")
    return marketing_img

def generate_social_media_qr(url, filename="qr-social.png"):
    """Genera un QR optimizado para redes sociales (cuadrado, compacto)"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=SolidFillColorMask(
            back_color=BRAND_COLORS['primary'],
            front_color=BRAND_COLORS['accent']
        )
    )
    
    # Crear cuadrado perfecto para redes sociales
    social_img = Image.new('RGB', (1080, 1080), 'white')
    draw = ImageDraw.Draw(social_img)
    
    # Centrar QR
    qr_width, qr_height = img.size
    qr_x = (1080 - qr_width) // 2
    qr_y = (1080 - qr_height) // 2
    
    social_img.paste(img, (qr_x, qr_y))
    
    # Agregar branding
    try:
        font_large = ImageFont.truetype("arial.ttf", 48)
        font_small = ImageFont.truetype("arial.ttf", 32)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Texto superior
    text = "Quindío Travel"
    text_bbox = draw.textbbox((0, 0), text, font=font_large)
    text_x = (1080 - (text_bbox[2] - text_bbox[0])) // 2
    draw.text((text_x, 50), text, fill=BRAND_COLORS['primary'], font=font_large)
    
    # Texto inferior
    subtext = "Eje Cafetero"
    subtext_bbox = draw.textbbox((0, 0), subtext, font=font_small)
    subtext_x = (1080 - (subtext_bbox[2] - subtext_bbox[0])) // 2
    draw.text((subtext_x, 950), subtext, fill=BRAND_COLORS['secondary'], font=font_small)
    
    social_img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"QR para redes sociales generado: {filename}")
    return social_img

def generate_svg_qr(url, filename="qr-basic.svg"):
    """Genera un QR en formato SVG para escalabilidad"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"QR SVG generado: {filename}")
    return img

def main():
    """Función principal que genera todos los tipos de QR"""
    print("🤠 Generando Códigos QR para Quindío Travel...")
    print(f"🌐 URL: {SITE_URL}")
    print(f"📁 Directorio: {OUTPUT_DIR}")
    print("-" * 50)
    
    # Crear directorio
    create_output_directory()
    
    # Generar diferentes tipos de QR
    try:
        # QR básico
        generate_basic_qr(SITE_URL)
        
        # QR con marca
        generate_branded_qr(SITE_URL)
        
        # QR estilizado
        generate_styled_qr(SITE_URL)
        
        # QR con logo (si existe)
        logo_path = "logo_quindio_travel.png"
        if os.path.exists(logo_path):
            generate_qr_with_logo(SITE_URL, logo_path)
        else:
            print("⚠️ Logo no encontrado, generando QR sin logo")
            generate_qr_with_logo(SITE_URL)
        
        # QR de marketing
        generate_marketing_qr(SITE_URL)
        
        # QR para redes sociales
        generate_social_media_qr(SITE_URL)
        
        # QR SVG
        generate_svg_qr(SITE_URL)
        
        print("-" * 50)
        print("✅ Todos los QRs generados exitosamente!")
        print(f"📁 Ubicación: {OUTPUT_DIR}/")
        
    except Exception as e:
        print(f"❌ Error generando QRs: {e}")
        print("💡 Asegúrate de tener instaladas las librerías:")
        print("   pip install qrcode[pil]")

if __name__ == "__main__":
    main()