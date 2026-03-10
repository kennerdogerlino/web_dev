import os
from flask import Flask, request, render_template

app = Flask(__name__)
UPLOAD_OLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methodos={"GET", "POST"})")
def upload_file():
    