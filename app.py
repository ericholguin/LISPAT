import os
import sys
import threading
import webbrowser
from uuid import uuid4
from flask_cors import CORS
from joblib import Parallel, delayed
from lispat_app.lispat.run import app_main
from werkzeug.utils import secure_filename
from lispat_app.lispat.utils.logger import Logger
from lispat_app.lispat.base.manager import CommandManager
from lispat_app.lispat.base.constants import args_convert, args_filter, args_json, args_clean, args_all, args_graph
from flask import Flask, render_template, request, make_response, session, json, Response, send_file, url_for


logger = Logger("LISPAT - Flask App")

app = Flask(__name__, static_folder="lispat_app/static/build/bundle",
            template_folder="lispat_app/static/build")

app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = os.urandom(24)

CORS(app, expose_headers='Authorization')

UPLOAD_FOLDER = os.path.abspath("lispat_app/static/uploads/")
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS


def allowed_file(filename):
    """Summary: For a given file, return whether it's an allowed type."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def save_file(file, filenames):
    """Summary: For a given file save it to its target destination."""
    if file and allowed_file(file.filename):
        # Get file name and set and save to upload path
        filename = secure_filename(file.filename)
        destination = os.path.join(UPLOAD_FOLDER, filename)

        logger.getLogger().info("Accept incoming file: {}".format(filename))
        logger.getLogger().info("Save it to: {}".format(destination))

        file.save(destination)
        filenames.append(destination)


def delete_files():
    """ Cleans the upload directory."""
    try:
        shutil.rmtree(os.path.abspath("lispat_app/static/uploads"))
    except RuntimeError:
        logger.getLogger().error("Error cleaning storage")


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
    Summary: Recieves uploaded documents and calls processing functions.

    return: status
    rtype: response code

    """
    if request.method == 'POST':
        logger.getLogger().info("Uploading File")

        # List for files
        filenames = []
        # Dictionary for JSON response
        data = {}
        # Command Manager
        manager = CommandManager()

        # Target folder for these uploads.
        if not os.path.exists(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)

        # Clean previous files
        args5 = args_clean()
        app_main(args5, manager)

        # Get list of files uploaded by users
        uploads = request.files
        # Separate files
        file1 = uploads['file1']
        file2 = uploads['file2']
        # Save files locally
        save_file(file1, filenames)
        save_file(file2, filenames)

        session['uploadedFiles'] = filenames

        if len(filenames) == 2:
            args = args_convert(filenames)
            app_main(args, manager)

            args2 = args_filter()
            app_main(args2, manager)

            args3 = args_graph()
            thread = threading.Thread(target=app_main, args=[args3, manager])
            thread.start()

            args4 = args_json()
            data = app_main(args4, manager)

            logger.getLogger().debug("Responding")

            js = json.dumps(data)
            resp = Response(js, status=200, mimetype="application/json")

            return resp
        else:
            return(make_response(('Error')))


@app.route("/graph")
def graph():
    """
    Summary: Route that opens graph html in new tab.

    return: Status of response
    rtype: status
    """
    url_for('static', filename='graph.html')
    html_file = os.path.abspath("lispat_app/static/build/graph.html")
    #return render_template("graph.html")
    return app.send_static_file("graph.html")
    """if os.path.isfile(html_file):
        webbrowser.open_new_tab("file://" + html_file)
        resp = Response(status=200)
        return resp"""

@app.route("/assets/samples.zip")
def download():
    """
    Summary: Route that sends a zipped file containing samples for users.

    return: None
    """
    try:

        return send_file(os.path.abspath("lispat_app/static/samples.zip"), attachment_filename='samples.zip')

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
