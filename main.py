from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "Cobi14"  # must match Meta dashboard exactly

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # ✅ This is what Meta calls during verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification token mismatch", 403

    elif request.method == "POST":
        # ✅ Meta sends actual message notifications here
        print(request.json)
        return "OK", 200

@app.route("/")
def home():
    return "Webhook is running ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
