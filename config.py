import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
    MAX_CONTENT_LENGTH = 16 * 1000 * 1000  # 16 mb
    UPLOADED_PHOTOS_DEST = "static/img"


config = Config()
