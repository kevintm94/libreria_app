# test_groq.py - Versión actualizada
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
print(f"🔑 API Key: {api_key[:10]}...{api_key[-5:]}")

if not api_key:
    print("❌ No se encontró GROQ_API_KEY en .env")
    exit(1)

try:
    client = Groq(api_key=api_key)
    
    # Usar modelo vigente
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Actualizado
        messages=[
            {"role": "user", "content": "Responde solo 'OK' si funciono correctamente"}
        ],
        temperature=0.1,
        max_tokens=10
    )
    
    print(f"✅ Conexión exitosa: {response.choices[0].message.content}")
    print(f"📊 Uso: {response.usage.total_tokens} tokens")
    print(f"Modelo usado: {response.model}")
    
except Exception as e:
    print(f"❌ Error: {e}")