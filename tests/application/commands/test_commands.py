from app.application.commands import (
    ExitCommand,
    GreetingCommand,
    UnknownCommand,
)

from app.conversation.models import Message
from app.conversation.roles import Role


def test_greeting_command():

    command = GreetingCommand()

    response = command.execute(
        Message(
            role=Role.USER,
            text="Olá",
        )
    )

    assert response.text == "Olá! Como posso ajudar?"


def test_exit_command():

    command = ExitCommand()

    response = command.execute(
        Message(
            role=Role.USER,
            text="sair",
        )
    )

    assert response.text == "Até logo."


def test_unknown_command():

    command = UnknownCommand()

    response = command.execute(
        Message(
            role=Role.USER,
            text="Thor",
        )
    )

    assert response.text == "Entendido."
