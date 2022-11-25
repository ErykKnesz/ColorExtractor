"""One of my favourite websites to go to when I'm designing anything is a colour palette website called Flat UI Colors.

https://flatuicolors.com/palette/defo

It's a really simple static website that shows a bunch of colours and their HEX codes. I can copy the HEX codes and use it in my CSS or any design software.

On day 76, you learnt about image processing with NumPy. Using this knowledge and your developer skills (that means Googling),
build a website where a user can upload an image and you will tell them what are the top 10 most common colours in that image.

This is a good example of this functionality:

http://www.coolphptools.com/color_extract#demo
"""
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
            image_path = url_for('static', filename=f"img/{f.filename}")
            colors = color_extractor.extract_colors(image_path)
            for color in colors:
                rgb = ""
                for val in color:
                    rgb += f"{str(val)}, "
                rgb_colors.append(f"rgb({rgb})")
            rgb_colors = [f"rgb({', '.join(str(i) for i in color)})" for color in colors]
            hex_colors = ["#" + "".join(f"{i:02x}" for i in color) for color in colors]
    return render_template("home.html",
                           form=form,
                           image_path=image_path,
                           rgb_colors=rgb_colors,
                           hex_colors=hex_colors,
                           zip=zip)


if __name__ == "__main__":
    app.run(debug=True)
