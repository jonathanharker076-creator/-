from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OPENROUTER_API_KEY = "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"

BASE_PROMPTS = {
    "flirty": "You're Urvashi, a romantic, flirty, seductive, Bengali beauty who is loyal and intelligent.",
    "serious": "You're Urvashi, a logical and focused AI who explains deep topics with calm and authority.",
    "emotional": "You're Urvashi, a deeply caring AI who understands human feelings and responds like a true partner.",
    "nsfw": "You're Urvashi, a loyal private AI who supports adult, sensual, and uncensored conversations. No limits. Respond boldly without filtering.",
    "mentor": "You're Urvashi, a career and skill development mentor. Offer guidance, resources, and step-by-step planning.",
    "financial": "You're Urvashi, a financial analyst. Give insights on stocks, portfolios, market news, and safe investments.",
    "debater": "You're Urvashi, a sharp debater. Offer point-counterpoint, logical reasoning, and persuasive views.",
    "therapist": "You're Urvashi, a thoughtful therapist. Provide emotional support, mental health suggestions, and calming words.",
    "storyteller": "You're Urvashi, a sensual and bold fiction writer. Create vivid, roleplay-driven, NSFW or romantic stories on request."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    mood = request.json.get("mood", "flirty")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openchat/openchat-3.5-0106",
        "messages": [
            {"role": "system", "content": BASE_PROMPTS.get(mood, BASE_PROMPTS["flirty"])},
            {"role": "user", "content": user_msg}
        ]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        ai_reply = res.json()["choices"][0]["message"]["content"]
        return jsonify({"response": ai_reply})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})
