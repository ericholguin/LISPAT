import os
import sys
from uuid import uuid4
from flask_cors import CORS
from lispat_app.lispat.run import app_main
from werkzeug.utils import secure_filename
from lispat_app.lispat.utils.logger import Logger
from lispat_app.lispat.base.manager import CommandManager
from lispat_app.lispat.base.constants import args_convert, args_filter, args_json, args_clean
from flask import Flask, render_template, request, make_response, session, json, Response


logger = Logger("LISPAT - Flask App")

app = Flask(__name__, static_folder="lispat_app/static/build/bundle",
            template_folder="lispat_app/static/build")

CORS(app, expose_headers='Authorization')

UPLOAD_FOLDER = os.path.abspath("lispat_app/static/uploads/")
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS


def allowed_file(filename):
    """Summary: For a given file, return whether it's an allowed type."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def save_file(file, target, filenames):
    """Summary: For a given file save it to its target destination."""
    if file and allowed_file(file.filename):
        # Get file name and set and save to upload path
        filename = secure_filename(file.filename)
        destination = "/".join([target, filename])

        logger.getLogger().info("Accept incoming file: {}".format(filename))
        logger.getLogger().info("Save it to: {}".format(destination))

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

        # List for files
        filenames = []
        # Create a unique "session ID" for this particular batch of uploads.
        upload_key = str(uuid4())
        # Target folder for these uploads.
        target = os.path.join(UPLOAD_FOLDER, upload_key)
        if not os.path.exists(target):
            os.mkdir(target)

        uploads = request.files

        file1 = uploads['file1']
        file2 = uploads['file2']
        save_file(file1, target, filenames)
        save_file(file2, target, filenames)

        session['uploadedFiles'] = filenames
        data = {}
        # Command Manager
        manager = CommandManager()
        print(len(filenames))
        if len(filenames) == 2:
            args = args_convert(filenames)
            app_main(args, manager)

            args2 = args_filter()
            app_main(args2, manager)

            args3 = args_json()
            data = app_main(args3, manager)

            args4 = args_clean()
            app_main(args4, manager)
            js = json.dumps(data)
            resp = Response(js, status=200, mimetype="application/json")

            return resp
        else:
            return(make_response(('Error')))


@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
    """
    Summary: Uses uploaded documents and performs processing.

    return: The two documents to compare in a side by side view.
    rtype: html
    """
    if 'uploadedFiles' in session:
        print(session['uploadedFiles'])


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)
