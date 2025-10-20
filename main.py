from flask import Flask, request
from pywa import WhatsApp

app = Flask(__name__)

wa = WhatsApp(
    phone_id="YOUR_PHONE_NUMBER_ID",
    token="YOUR_ACCESS_TOKEN",
    verify_token="my-secret",
    server=app
)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return wa.handle_verification(request)
    else:
        wa.handle_notification(request)
        return "OK", 200

@app.route("/")
def home():
    return "WhatsApp Webhook is running ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
