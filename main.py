import os

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from flask_uploads import configure_uploads

from form import ImageForm, images
from config import Config
from color_extractor import ColorExtractor

app = Flask(__name__)
app.config.from_object(Config)
configure_uploads(app, images)

color_extractor = ColorExtractor()


@app.route("/", methods=["GET", "POST"])
def home():
    form = ImageForm()
    image_path = None
    rgb_colors = []
    hex_colors = []
    if request.method == "POST":
        if form.validate_on_submit():
            f = form.image.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(
                app.config["UPLOADED_PHOTOS_DEST"], filename
            ))
            image_path = url_for('static', filename=f"img/{filename}")
            colors = color_extractor.extract_colors(image_path)
            rgb_colors = [f"rgb({', '.join(str(i) for i in color)})"
                          for color in colors]
            hex_colors = ["#" + "".join(f"{i:02x}" for i in color)
                          for color in colors]
    return render_template("home.html",
                           form=form,
                           image_path=image_path,
                           rgb_colors=rgb_colors,
                           hex_colors=hex_colors,
                           zip=zip)


if __name__ == "__main__":
    app.run(debug=True)
