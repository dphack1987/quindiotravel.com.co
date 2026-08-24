#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Optimización de WhatsApp Booking Internacional
Script para generar mensajes de WhatsApp optimizados por mercado
"""

def generate_whatsapp_message(market, language, tour_type):
    """Generar mensaje de WhatsApp optimizado por mercado"""
    
    messages = {
        'usa': {
            'en': {
                'general': "Hello Quindío Travel! I'm interested in booking a Coffee Triangle Colombia tour. I'm from the USA and would like to know about availability and prices in USD.",
                'coffee_tour': "Hello! I want to book a Coffee Triangle tour from the USA. Interested in authentic coffee experiences, Valle de Cocora, and Salento. Please quote in USD.",
                'salento': "Hi! I'm planning to visit Salento Colombia from the USA. Looking for tours, accommodation, and transport. Please provide information in English."
            },
            'es': {
                'general': "Hola Quindío Travel, estoy interesado en reservar un tour al Eje Cafetero desde Estados Unidos. Me gustaría conocer disponibilidad y precios en dólares.",
                'coffee_tour': "¡Hola! Quiero reservar un tour del Eje Cafetero desde EE.UU. Interesado en experiencias de café auténticas, Valle de Cocora y Salento. Por favor cotizar en USD.",
                'salento': "¡Hola! Estoy planeando visitar Salento Colombia desde EE.UU. Busco tours, alojamiento y transporte. Por favor proporcionar información en español."
            }
        },
        'uk': {
            'en': {
                'general': "Hello Quindío Travel! I'm from the UK and interested in booking a Colombia Coffee Region tour. Please provide information in GBP and English.",
                'coffee_tour': "Hi! I want to book a Coffee Triangle tour from the UK. Looking for authentic Colombian coffee experiences. Please quote in GBP.",
                'salento': "Hello! Planning to visit Salento Colombia from the UK. Need information about tours, hotels, and transport in English."
            },
            'es': {
                'general': "Hola Quindío Travel, soy del Reino Unido y estoy interesado en reservar un tour al Eje Cafetero. Por favor proporcionar información en libras esterlinas.",
                'coffee_tour': "¡Hola! Quiero reservar un tour del Triángulo del Café desde el Reino Unido. Busco experiencias de café colombiano auténticas. Por favor cotizar en GBP.",
                'salento': "¡Hola! Estoy planeando visitar Salento Colombia desde el Reino Unido. Necesito información sobre tours, hoteles y transporte."
            }
        },
        'europe': {
            'en': {
                'general': "Hello Quindío Travel! I'm from Europe and interested in Coffee Triangle Colombia tours. Please provide information in EUR and English.",
                'coffee_tour': "Hi! Want to book a Coffee Triangle tour from Europe. Interested in coffee experiences and Valle de Cocora. Please quote in EUR.",
                'salento': "Hello! Planning to visit Salento Colombia from Europe. Need tours, accommodation, and transport information in English."
            },
            'es': {
                'general': "Hola Quindío Travel, soy de Europa y estoy interesado en tours al Triángulo del Café. Por favor proporcionar información en euros.",
                'coffee_tour': "¡Hola! Quiero reservar un tour del Triángulo del Café desde Europa. Interesado en experiencias de café y Valle de Cocora. Por favor cotizar en EUR.",
                'salento': "¡Hola! Estoy planeando visitar Salento Colombia desde Europa. Necesito información sobre tours, alojamiento y transporte."
            },
            'fr': {
                'general': "Bonjour Quindío Travel! Je suis d'Europe et intéressé par les tours du Triangle du Café en Colombie. Veuillez fournir des informations en euros.",
                'coffee_tour': "Bonjour! Je veux réserver un tour du Triangle du Café depuis l'Europe. Intéressé par les expériences café. Veuillez citer en euros.",
                'salento': "Bonjour! Je prévois de visiter Salento Colombie depuis l'Europe. Besoin d'informations sur les tours et l'hébergement."
            },
            'de': {
                'general': "Hallo Quindío Travel! Ich bin aus Europa und interessiert an Kaffee-Dreieck Kolumbien Touren. Bitte Informationen in Euro bereitstellen.",
                'coffee_tour': "Hallo! Ich möchte eine Kaffee-Dreieck Tour aus Europa buchen. Interessiert an Kaffee-Erlebnissen. Bitte in Euro anbieten.",
                'salento': "Hallo! Ich plane, Salento Kolumbien aus Europa zu besuchen. Brauche Informationen über Touren und Unterkunft."
            }
        }
    }
    
    try:
        message = messages[market][language][tour_type]
        return message
    except KeyError:
        # Fallback to English general message
        return messages[market]['en']['general']

def generate_booking_url(market, language, tour_type='general'):
    """Generar URL de WhatsApp con mensaje optimizado"""
    
    base_url = "https://wa.me/573174426044?text="
    message = generate_whatsapp_message(market, language, tour_type)
    
    # Codificar mensaje para URL
    import urllib.parse
    encoded_message = urllib.parse.quote(message)
    
    return base_url + encoded_message

def main():
    print("Generación de URLs de WhatsApp Booking Internacional")
    print("="*60)
    
    markets = ['usa', 'uk', 'europe']
    languages = ['en', 'es']
    tour_types = ['general', 'coffee_tour', 'salento']
    
    booking_urls = {}
    
    for market in markets:
        for language in languages:
            for tour_type in tour_types:
                url = generate_booking_url(market, language, tour_type)
                key = f"{market}_{language}_{tour_type}"
                booking_urls[key] = url
                
                print(f"{key}:")
                print(f"  {url[:100]}...")
                print()
    
    # Guardar URLs en archivo para uso futuro
    with open('whatsapp_booking_urls.json', 'w', encoding='utf-8') as f:
        import json
        json.dump(booking_urls, f, indent=2, ensure_ascii=False)
    
    print("="*60)
    print(f"Total URLs generadas: {len(booking_urls)}")
    print("Guardadas en whatsapp_booking_urls.json")

if __name__ == '__main__':
    main()