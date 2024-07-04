from flask import Flask, render_template, request
from config import *
from controllers.ai_utilities import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def chat_room():
    if request.method == "POST":
        usr_message = request.form.get("message")
        # response_msg = "Bot: "+get_system_response(usr_message) #Just to check with hardcoded
        response_msg = "Bot: " + "Hi, how are you?"
        return render_template("index.html", system_response=response_msg)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)  # using dev environment so debug=True
