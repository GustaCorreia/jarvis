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

def test_history_is_stored():

    engine = ConversationEngine()

    engine.receive("Olá")

    assert len(engine.conversation) == 2


def test_history_order():

    engine = ConversationEngine()

    engine.receive("Olá")

    messages = engine.conversation.messages()

    assert messages[0].text == "Olá"
    assert messages[1].text == "Olá! Como posso ajudar?"
