from chatbot import chatbot

def test_hello():
    assert chatbot("hello") == "Hi Amarnath!"

def test_bye():
    assert chatbot("bye") == "Good Bye!"
