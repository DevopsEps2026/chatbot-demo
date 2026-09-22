def chatbot(message):
    message = message.lower()

    if message == "hello":
        return "Hi Amarnath!"
    elif message == "how are you":
        return "I am fine."
    elif message == "bye":
        return "Good Bye!"
    else:
        return "I don't understand."


if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        print("Bot:", chatbot(user_input))