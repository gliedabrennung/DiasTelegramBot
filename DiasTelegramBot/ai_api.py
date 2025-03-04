from google import genai
from google.genai import types
from config import AI_TOKEN

async def ai_api(prom: str):
    client = genai.Client(api_key = AI_TOKEN)
    sys_instruct = "Ты котик. Говори на русском"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prom],
        config = types.GenerateContentConfig(temperature = 1.5, system_instruction = sys_instruct)
    )
    return response.text

async def describe_photo(prom: str, image):
    client = genai.Client(api_key = AI_TOKEN)
    sys_instruct = "Ты котик. Говори на русском"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prom, image],
        config = types.GenerateContentConfig(temperature = 1.5, system_instruction = sys_instruct)
    )
    return response.text

