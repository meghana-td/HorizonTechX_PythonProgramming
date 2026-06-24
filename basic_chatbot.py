def bot_responses(n):
    if n == "hello":
        return "Hi!"
    elif n == "how are you?":
        return "I'm fine, thanks!"
    elif n == "what is your name":
        return "I am a chatbot."
    elif n == "thank you":
        return "You're welcome!"
    elif n == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I am unable to understand that."

print("---Welcome to Chatbot---")

while True:
    n = input("You: ").lower()

    print("Bot: ", bot_responses(n))
    if n == "bye":
        break
