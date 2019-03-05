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
from flask import Flask, render_template, request, make_response, session, json, Response, send_file


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
    Summary: Recieves uploaded documents and stores into static folder.

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

        #Clean previous files
        args5 = args_clean()
        app_main(args5, manager)

        uploads = request.files

        file1 = uploads['file1']
        file2 = uploads['file2']
        save_file(file1, filenames)
        save_file(file2, filenames)

        session['uploadedFiles'] = filenames

        if len(filenames) == 2:
            args = args_convert(filenames)
            app_main(args, manager)

            args2 = args_filter()
            app_main(args2, manager)

            args3 = args_graph()
            app_main(args3, manager)
            # thread = threading.Thread(target=app_main, args=[args3, manager])
            # thread.start()

            args4 = args_json()
            data = app_main(args4, manager)
            logger.getLogger().debug("Responding")
            js = json.dumps(data)
            resp = Response(js, status=200, mimetype="application/json")

            return resp
        else:
            return(make_response(('Error')))


@app.route("/graph", methods=['GET', 'POST'])
def graph():
    """
    Summary: Uses uploaded documents and performs processing.

    return: The two documents to compare in a side by side view.
    rtype: html
    """
    try:

        return send_file(os.path.abspath("lispat_app/static/Graph.html"), attachment_filename='Graph.html')

    except Exception as e:
        return str(e)

    #html_file = os.path.abspath("lispat_app/static/uploads/visuals/Standard-Visual.html")
    #return app.send_static_file(html_file)

    #if os.path.isfile(html_file):
    #    webbrowser.open_new_tab("file://" + html_file)
    #    resp = Response(status=200)
    #    return resp

@app.route("/assets/samples.zip")
def download():
    """
    Summary: Uses uploaded documents and performs processing.

    return: The two documents to compare in a side by side view.
    rtype: html
    """
    try:

        return send_file(os.path.abspath("lispat_app/static/samples.zip"), attachment_filename='samples.zip')

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
