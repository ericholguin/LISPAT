import os
from uuid import uuid4
from lispat.utils.logger import Logger
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, make_response, session


logger = Logger("LISPAT")

app = Flask(__name__, static_folder="../static/build/bundle",
            template_folder="../static/build")

UPLOAD_FOLDER = os.path.abspath("../static/uploads/")
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS


def allowed_file(filename):
    """Summary: For a given file, return whether it's an allowed type."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


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
        # List for files
        filenames = []

        # Create a unique "session ID" for this particular batch of uploads.
        upload_key = str(uuid4())

        # Target folder for these uploads.
        target = os.path.join(UPLOAD_FOLDER, upload_key)

        if not os.path.exists(target):
            os.mkdir(target)

        for upload in request.files.getlist("file"):
            if upload and allowed_file(upload.filename):
                # Get file name and set and save to upload path
                filename = secure_filename(upload.filename)
                destination = "/".join([target, filename])

                logger.getLogger().info("Accept incoming file:", filename)
                logger.getLogger().info("Save it to:", destination)

                upload.save(destination)
                filenames.append(destination)

        session['uploadedFiles'] = filenames

        return make_response(('ok', 200))

"""
@app.route("/analyze", methods=['POST'])
def analyze():"""
    """
    Summary: Uses uploaded documents and performs processing.

    return: The two documents to compare in a side by side view.
    rtype: html
    """


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)

flask_cors.CORS(app, expose_headers='Authorization')
