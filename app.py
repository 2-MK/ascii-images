from flask import Flask, render_template, request
from asci import image_to_ascii
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():

    file = request.files["image"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    ascii_art = image_to_ascii(filepath)

    return render_template(
        "result.html",
        ascii_art=ascii_art
    )


if __name__ == "__main__":
    app.run(debug=True)