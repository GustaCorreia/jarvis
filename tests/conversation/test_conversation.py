from app.conversation.conversation import Conversation
from app.conversation.roles import Role


def test_new_conversation_is_empty():

    conversation = Conversation()

    assert len(conversation) == 0


def test_add_user_message():

    conversation = Conversation()

    conversation.add_user_message("Olá")

    assert len(conversation) == 1

    message = conversation.last_message()

    assert message is not None
    assert message.role == Role.USER
    assert message.text == "Olá"


def test_add_assistant_message():

    conversation = Conversation()

    conversation.add_assistant_message("Olá!")

    message = conversation.last_message()

    assert message is not None
    assert message.role == Role.ASSISTANT
    assert message.text == "Olá!"


def test_messages_returns_tuple():

    conversation = Conversation()

    conversation.add_user_message("A")
    conversation.add_assistant_message("B")

    messages = conversation.messages()

    assert isinstance(messages, tuple)
    assert len(messages) == 2


def test_clear():

    conversation = Conversation()

    conversation.add_user_message("A")
    conversation.add_assistant_message("B")

    conversation.clear()

    assert len(conversation) == 0
    assert conversation.last_message() is None


def test_iteration():

    conversation = Conversation()

    conversation.add_user_message("A")
    conversation.add_assistant_message("B")

    texts = [message.text for message in conversation]

    assert texts == ["A", "B"]
