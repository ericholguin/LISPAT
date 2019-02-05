import os
from uuid import uuid4
from lispat.utils.logger import Logger
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, make_response, session


logger = Logger("LISPAT")

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/storage"
_log = Logger("Flask App")
app = Flask(__name__, static_folder="../static/build/bundle",
            template_folder="../static/build")

CORS(app, expose_headers='Authorization')

UPLOAD_FOLDER = os.path.abspath("../static/uploads/")
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# List for files
filenames = []


def allowed_file(filename):
    """Summary: For a given file, return whether it's an allowed type."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def save_file(file, target):
    """Summary: For a given file save it to its target destination."""
    if file and allowed_file(file.filename):
        # Get file name and set and save to upload path
        filename = secure_filename(file.filename)
        destination = "/".join([target, filename])

        logger.getLogger().info("Accept incoming file:", filename)
        logger.getLogger().info("Save it to:", destination)

        file.save(destination)
        filenames.append(destination)


@app.route("/")
def index():
    """
    Summary: Home Page of the LISPAT API.

    return: Home page
    rtype: html

    """
    return render_template("index.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    """
    Summary: Recieves uploaded documents and stores into static folder.

    return: status
    rtype: response code

    """
    if request.method == 'POST':
        logger.getLogger().info("Uploading File")

        # Create a unique "session ID" for this particular batch of uploads.
        upload_key = str(uuid4())

        # Target folder for these uploads.
        target = os.path.join(UPLOAD_FOLDER, upload_key)

        if not os.path.exists(target):
            os.mkdir(target)

        uploads = request.files

        file1 = uploads['file1']
        file2 = uploads['file2']

        save_file(file1, target)
        save_file(file2, target)

        session['uploadedFiles'] = filenames

        return make_response(('ok', 200))


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)
