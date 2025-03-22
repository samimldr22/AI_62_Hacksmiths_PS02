from flask import Flask, request, jsonify, render_template

app = Flask(__name__)  # ✅ Corrected Line

# Simple chatbot logic
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand.")

# API route for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    bot_reply = chatbot_response(user_message)
    return jsonify({"reply": bot_reply})

# Serve the frontend
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)