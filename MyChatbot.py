# Test Cases
# Check want does bot want from this point
# Choose from one of the following topics or type your question.
# Provide Hyperlink sections and redirect to the following sections
# Section as follows: Projects or Education or Accompliments or Work Experience

responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thanks for asking!",
    "bye": "Goodbye!",
    "resume": "<a href='https://harsamerveersingh.w3spaces.com/'>Resume</a>",
    "portfolio": "<a href='https://harsamerveersingh.w3spaces.com/'>Portfolio</a>",
    "help": "You can ask me about my resume or portfolio, or simply say hi or bye.",
    "stop": "Exiting chatbot."
}

def chatbot():
    print("Welcome to the chatbot. Type 'help' for a list of commands.")
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            if user_input == "stop":
                print("Bot: " + responses[user_input])
                break
            print("Bot: " + responses[user_input])
        else:
            print("Bot: I'm sorry, I didn't understand your input. Type 'help' for a list of commands.")

chatbot()

