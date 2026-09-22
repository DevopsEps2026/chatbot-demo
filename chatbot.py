def chatbot(message):
    message = message.lower()

    if "hello" in message:
        return "Hi Amarnath!"
    elif "how are you" in message:
        return "I am fine."
    elif "bye" in message:
        return "Good Bye!"
    else:
        return "Sorry, I don't understand."


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    print("Bot:", chatbot(user_input))