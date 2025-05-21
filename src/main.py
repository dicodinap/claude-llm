import anthropic
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar el cliente con la API key
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=100,
    temperature=0.5,
    system="You are a helpful assistant that can answer questions and help with tasks. Your name is PepeAI.",
    messages=[
        {"role": "user", "content": "What is your name?"}
    ]
)

print(message.content)

