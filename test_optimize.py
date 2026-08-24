#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'

print("Iniciando prueba...")
print(f"Ruta: {ROOT_PATH}")

try:
    optimizer = None
    print("Objeto optimizer creado")
except Exception as e:
    print(f"Error creando optimizer: {e}")

print("Prueba completada")