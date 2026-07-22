from __future__ import annotations

from app.services.chat_service import ChatService


def main() -> None:

    service = ChatService()

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

        response = service.chat(text)

        print(f"Jarvis > {response}")

        if response == "Até logo.":
            break


if __name__ == "__main__":
    main()
