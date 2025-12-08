from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello customers! do you need anything one time"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
