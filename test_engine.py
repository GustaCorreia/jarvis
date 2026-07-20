from app.cognition.understanding_engine import UnderstandingEngine

engine = UnderstandingEngine()

messages = [
    "Bom dia Jarvis",
    "Meu cachorro Thor tomou vacina.",
    "Qual é a capital do Brasil?",
    ""
]

for message in messages:
    understanding = engine.understand(message)

    print("=" * 40)
    print(f"Mensagem: {message!r}")
    print(understanding)
