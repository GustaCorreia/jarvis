from __future__ import annotations

from app.conversation.engine import ConversationEngine


def main() -> None:
    engine = ConversationEngine()

    print()
    print("=" * 41)
    print("               JARVIS")
    print("=" * 41)
    print()
    print("Digite 'sair' para encerrar.")
    print()

    while True:
        text = input("Você > ").strip()

        if not text:
            continue

        response = engine.receive(text)

        print(f"Jarvis > {response.text}")

        if response.text == "Até logo.":
            break


if __name__ == "__main__":
    main()
