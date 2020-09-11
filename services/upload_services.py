import os

from werkzeug.utils import secure_filename

import main

UPLOAD_FOLDER = "inputs"
ALLOWED_EXTENSIONS = {'jpg'}
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def file_save(file):
    if file.filename == '':
        raise Exception("Error No file selected")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return filename
    else:
        raise Exception('File format not supported - Upload an Image')