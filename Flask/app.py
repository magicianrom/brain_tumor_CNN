from flask import Flask, request, render_template, redirect, session, send_from_directory
from PIL import Image
import numpy as np
import keras
#from keras.applications.resnet50 import preprocess_input
from keras.applications.vgg16 import preprocess_input
#from keras.applications.efficientnet import preprocess_input
import os
from translations import TEXT

app = Flask(__name__)
app.secret_key = "test"

MODEL_PATH = "vgg_flask.keras"  #effb0_flask.keras, resnet50_flask.keras, vgg_flask.keras#
IMG_SIZE = (512, 512)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CLASS_NAMES = ["glioma", "meningioma", "notumor", "pituitary"]

model = keras.models.load_model(
    MODEL_PATH,
    custom_objects={"preprocess_input": preprocess_input},
    compile=False,
    safe_mode=False
)

def predict_pil(img):
    img = img.convert("RGB").resize(IMG_SIZE)
    x = np.asarray(img, dtype=np.float32)
    x = np.expand_dims(x, axis=0)

    probs = model.predict(x, verbose=0)[0]
    idx = int(np.argmax(probs))

    return CLASS_NAMES[idx], float(probs[idx]), probs

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/language", methods=["GET", "POST"])
def language():
    if request.method == "POST":
        selected_language = request.form.get("language", "en")
        session["language"] = selected_language
        return redirect("/menu")
    return render_template("language.html")

@app.route("/menu")
def menu():
    lang = session.get("language", "en")
    texts = TEXT[lang]
    return render_template("menu.html", texts=texts, lang=lang)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    lang = session.get("language", "en")
    texts = TEXT[lang]

    if request.method == "GET":
        return render_template("predict.html", texts=texts, lang=lang)

    f = request.files.get("image")
    if not f or f.filename == "":
        return "No file uploaded", 400

    filename = os.path.basename(f.filename)
    save_path = os.path.join(UPLOAD_FOLDER, filename)

    f.save(save_path)

    img = Image.open(save_path)
    label, conf, probs = predict_pil(img)

    return render_template(
        "result.html",
        pred=label,
        conf=round(conf * 100, 2),
        probs={n: round(float(p) * 100, 2) for n, p in zip(CLASS_NAMES, probs)},
        texts=texts,
        lang=lang,
        image_file=filename
    )

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)