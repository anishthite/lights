import flask
from flask_cors import CORS 
import os
from dotenv import load_dotenv
from waitress import serve
from datetime import datetime

load_dotenv()

import logging

logger = logging.getLogger("waitress")
logger.setLevel(logging.DEBUG)

app = flask.Flask(__name__)

CORS(
    app=app,
    supports_credentials=True,
    origins=[
        "http://localhost:3000",
    ],
)

@app.route("/turnOff", methods=["POST"])
def turnOff():
    print("turnOff")
    return "turnOff"

@app.route("/turnOn", methods=["POST"])
def turnOn():
    print("turnOn")
    return "turnOn"

@app.route("/fadeLight", methods=["POST"])
def fadeLight():
    print("fadeLight")
    return "fadeLight"

@app.route("/setColor", methods=["POST"])
def setColor():
    print("setColor")
    return "setColor"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")

def index(path):
    return "testy mctesty"


if __name__ == "__main__":
    print(f"serving LIGHTS", flush=True)
    APIDOMAIN = os.getenv("APIDOMAIN")
    if not APIDOMAIN:
        APIDOMAIN = "http://127.0.0.1"
    PORT = os.getenv("PORT")
    if not PORT:
        PORT = 5000
    try:
        serve(app, listen=APIDOMAIN + ":{}".format(PORT))
    except Exception as e:
        print(e)
