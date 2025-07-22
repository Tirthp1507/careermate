from flask import Flask, render_template, request
from career_ai import chat_with_bot

app = Flask(__name__)
chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    if request.method == "POST":
        user_message = request.form["message"]
        chat_history.append(("user", user_message))

        bot_response = chat_with_bot(user_message)
        chat_history.append(("bot", bot_response))

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
