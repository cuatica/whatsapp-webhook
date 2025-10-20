from flask import Flask, request
from pywa import WhatsApp

app = Flask(__name__)

wa = WhatsApp(
    phone_id="883020854886533",
    token="EAAlHsOZCxr6gBPgQnoscOJgvoqZA1AXxZA8dlCbjDkfeGxRNtSlta5n0NXEIUkM2ZAYdy6ZAOD1aRKKpXnKCBt4h74D1EWFdubHaOGcaV2E303xC7banQL0BfeEPZBtMPZCs6Tk951h62gZAknBMPpJor6YD1WYl0T2npLd6gfFkVwUr9OTTf7cHOt4tlGZBCbx3ZB3uqQIEC3ZARYhwrh93pZC2m5s465u8Uqyrae1yTpwn2jkZD",
    verify_token="Cobi14",
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
