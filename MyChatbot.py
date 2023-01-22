# Test Cases
# Check want does bot want from this point
# Choose from one of the following topics or type your question.
# Provide Hyperlink sections and redirect to the following sections
# Section as follows: Projects or Education or Accompliments or Work Experience

from flask import Flask, request, jsonify

app = Flask(__name__)

responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thanks for asking!",
    "bye": "Goodbye!",
    "resume": "<a href='https://harsamerveersingh.w3spaces.com/'>Resume</a>",
    "portfolio": "<a href='https://harsamerveersingh.w3spaces.com/'>Portfolio</a>",
    "help": "You can ask me about my resume or portfolio, or simply say hi or bye.",
    "stop": "Exiting chatbot."
}

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form['user_input'].lower()
        if user_input in responses:
            return jsonify({"response": responses[user_input]})
        else:
            return jsonify({"response": "I'm sorry, I didn't understand your input. Type 'help' for a list of commands."})
    return '''
        <form method="post">
            <input type="text" name="user_input">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
