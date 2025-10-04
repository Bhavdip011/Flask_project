from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SUGGESTIONS = [
    "Tell me about India",
    "Who are you?",
    "How are you?",
    "What is 2 + 2?",
    "Tell me about Germany"
]
# Suggestions to show when user clicks the placeholder for the first time
PLACEHOLDER_SUGGESTIONS = [
    "Hello",
    "Hi",
    "Hey",
    "How are you?",
    "Who are you?",
    "Where are you from?",
    "Tell me about India",
    "Tell me about Germany",
    "What is 2 + 2?"
]

def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # Simple greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input or "hlo" in user_input or "helo" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm functioning perfectly! 😊"
    elif "who are you" in user_input:
        return "I'm your friendly AI chatbot built with Python!"
    elif "where are you from" in user_input:
        return "I'm from the cloud ☁️😊!"

    # Country facts
    elif "india" in user_input:
        return "India is a country in South Asia known for its culture, spices, and IT sector. Capital: New Delhi."
    elif "america" in user_input or "usa" in user_input:
        return "The United States of America (USA) is a large country in North America. Capital: Washington, D.C."
    elif "canada" in user_input:
        return "Canada is the second-largest country by area. Known for maple syrup and polite people! Capital: Ottawa."
    elif "germany" in user_input:
        return "Germany is a European country known for its cars, engineering, and history. Capital: Berlin."

    # Math logic
    try:
        if any(op in user_input for op in ['+', '-', '*', '/', '**', '%']):
            result = str(eval(user_input))
            return f"The answer is {result}"
    except:
        return "I couldn't understand your math question."

    # Default fallback
    return "Sorry, I don't understand that yet. Ask me about math or countries!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('input', '')
    response = get_bot_response(user_input)
    return jsonify({
        'response': response,
        'suggestions': SUGGESTIONS,
        'placeholder_suggestions': PLACEHOLDER_SUGGESTIONS
    })

if __name__ == '__main__':
    app.run(debug=True)
