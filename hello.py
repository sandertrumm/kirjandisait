import os
import random

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    files = os.listdir("kirjandisait/text")
    return f"<p>This is file {random.choice(files)}</p>"