from http import client
import types
from PIL import Image

def readJSON(response):
    import json
    try:
        return json.loads(response.text)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return None

def getImageText(image_path):
    img = Image.open(image_path)
        
    # Extract the text from the image (1st prompt)
    text_prompt = """extract the mathematical text from the image, preserving structure"""
    try:
        prompt_response = client.models.generate_content(
            model = "gemini-flash-latest",
            contents = [text_prompt, img],
            config = types.GenerateContentConfig(
                response_mime_type="text/plain"
            )
        )
        return prompt_response.text
    except Exception as e:
        print(f"Error extracting")
        return None

def process(text_prompt):

    group_list = [] # List of groups (classification of nodes)

    # Once we have the text, we classify the nodes (2nd prompt)
    classify_prompt = f"""First, I want you to extract all the possible themes related to the
    following mathematical text: {text_prompt}

    Classify the following mathematical text into understanding groups, e.g.,
    if we are talking about Isomorphism theorems, I want you to classify all the related definitions, lemmas,
    theorems, etc. in that group with the following format: 
    {"groups": [{"id": 1, "theme": "Theme1, Theme2, Theme3,...", "content": "<content>"}]}
    Not too many themes, just the main ones.
    """
    try:
        prompt_response = client.models.generate_content(
            model = "gemini-flash-latest",
            contents = [text_prompt],
            config = types.GenerateContentConfig(
                response_mime_type="text/plain"
            )
        )
    except Exception as e:
        print(f"Error extracting")
        return None
