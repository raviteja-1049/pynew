from flask import Flask, request, jsonify, send_from_directory
import random

app = Flask(__name__)

descriptions = [
    "This person will be a futuristic tech innovator 🚀",
    "This face belongs to an intergalactic explorer 🌌",
    "This is you as a virtual influencer of 2090 👑",
    "A peaceful AI monk from the year 2077 🧘",
    "A super coder in the metaverse 💻"
]

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

@app.route("/generate")
def generate():
    name = request.args.get("name", "Anonymous")
    # Using random face image API
    img_url = f"https://api.dicebear.com/8.x/fun-emoji/svg?seed={name}"
    return jsonify({
        "image": img_url,
        "description": random.choice(descriptions)
    })

if __name__ == "__main__":
    app.run(debug=True)