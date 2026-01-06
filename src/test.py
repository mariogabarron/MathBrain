'''
import os
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv

# Configuración de la API
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(base_dir, '.env'))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def process_math_notes(image_path):
    """
    Lee una imagen de apuntes y devuelve una estructura de grafo en JSON.
    """
    img = Image.open(image_path)
    
    # El "Prompt" es el secreto: le decimos exactamente cómo queremos los datos
    prompt = """
    Analiza esta imagen de apuntes de álgebra abstracta. 
    Identifica los teoremas, definiciones o conceptos clave y cómo se conectan entre sí.
    Devuelve exclusivamente un objeto JSON con esta estructura:
    {
      "nodes": [{"id": 1, "label": "Nombre", "theme": "Groups/Rings/Fields", "content": "Definición corta"}],
      "edges": [{"from": 1, "to": 2}]
    }
    """

    try:
        # Usamos el modelo que nos funcionó en el test
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=[prompt, img],
            config=types.GenerateContentConfig(
                response_mime_type="application/json" # Forzamos salida JSON
            )
        )
        
        # Devolvemos el JSON procesado
        import json
        return json.loads(response.text)
    
    except Exception as e:
        print(f"❌ Error procesando imagen: {e}")
        return None

# Pequeño test interno
if __name__ == "__main__":
    # Cambia 'apuntes.png' por el nombre de tu foto en la carpeta data
    test_path = os.path.join(base_dir, 'data', 'apuntes.png')
    if os.path.exists(test_path):
        result = process_math_notes(test_path)
        print(result)
    else:
        print(f"⚠️ No se encontró la imagen en {test_path}")
        '''