from flask import Flask, request

app = Flask(__name__)

app_secret = "Cobi14"  # must match Meta dashboard exactly
ACCESS_TOKEN = "EAAlHsOZCxr6gBPpHZC0ZAsDC2WV8ZA12FwPNDnBF29gNsMunbjh7QqqM0nzNbgjUgBxfsyQoOoAHYoy1Q5w3PXEZBYIczuVcQ3b4Y7ACNXm5BmIix0LP3L7eTikWPXZBq2BxVNsENoo12rye3KRlyswSyEryZABwbARxqWUCSwGHOXLemSieQndOKI7WB5b09NAG35PFXyDxv6Jvbbmw2Rtrq60WZAADv9iNZCWZC6kAWpO0ZCnoFG6q45aba1hpDmBF2VwPr8nhZB7oSl6mT32xuO0DdgZDZD"
PHONE_NUMBER_ID = "883020854886533"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # ✅ This is what Meta calls during verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == app_secret:
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
