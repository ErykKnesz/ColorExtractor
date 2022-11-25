from flask_wtf import FlaskForm
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

images = UploadSet("images",
                   IMAGES,
                   default_dest=lambda app: app.config["UPLOADED_PHOTOS_DEST"])


class ImageForm(FlaskForm):
    image = FileField("Upload File",
                      validators=[FileRequired(),
                                  FileAllowed(images, 'Images only!')])
    submit = SubmitField("Upload")
