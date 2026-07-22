from app.conversation.engine import ConversationEngine


def test_greeting():

    engine = ConversationEngine()

    response = engine.receive("Olá")

    assert response.text == "Olá! Como posso ajudar?"


def test_exit():

    engine = ConversationEngine()

    response = engine.receive("sair")

    assert response.text == "Até logo."


def test_default_response():

    engine = ConversationEngine()

    response = engine.receive("Meu cachorro chama Thor.")

    assert response.text == "Entendido."
