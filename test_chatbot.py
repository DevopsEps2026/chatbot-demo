from chatbot import chatbot

def test_hello():
    assert chatbot("hello") == "Hi Amarnath!"

def test_bye():
    assert chatbot("bye") == "Good Bye!"

def test_how_are_you():
    assert chatbot("how are you") == "I am fine."

def test_unknown():
    assert chatbot("unknown") == "I don't understand."