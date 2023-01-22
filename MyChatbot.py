# Test Cases
# Check want does bot want from this point
# Display projects or education or accompliments or work experience


responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thanks for asking!",
    "bye": "Goodbye!",
}

def chatbot():
    while True:
        user_input = input("You: ")
        if user_input.lower() in responses:
            print("Bot: " + responses[user_input])
        elif user_input.lower() == "bye":
            break
        else:
            print("Bot: I'm sorry, I didn't understand your input.")

chatbot()

