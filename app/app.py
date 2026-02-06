from flask import Flask
import logging
import json
import random
import time

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def log(level, message, extra={}):
    entry = {
        "service": "user-service",
        "level": level,
        "message": message,
        "latency_ms": random.randint(20, 600),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    entry.update(extra)

    if level == "ERROR":
        logging.error(json.dumps(entry))
    else:
        logging.info(json.dumps(entry))

@app.route("/")
def home():
    log("INFO", "Home endpoint hit")
    return "OK"

@app.route("/login")
def login():
    log("INFO", "User login attempt")
    return "Login OK"

@app.route("/error")
def error():
    log("ERROR", "Database connection failed")
    return "ERROR", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
