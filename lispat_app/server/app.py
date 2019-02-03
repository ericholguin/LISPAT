from flask import Flask, render_template, request
from lispat.utils.logger import Logger
from lispat.run import app_main
from flask_cors import CORS, cross_origin
import os

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/storage"
_log = Logger("Flask App")
app = Flask(__name__, static_folder="../static/build/bundle",
      template_folder="../static/build")
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        _log.getLogger().info("Uploading File")
        f = request.files
        _log.getLogger().debug(f)
        standard = f['file1']
        submission = f['file2']
        standard.save(os.path.join(app.config['UPLOAD_FOLDER'], "standard"))
        submission.save(os.path.join(app.config['UPLOAD_FOLDER'], "submission"))

        std_path = UPLOAD_FOLDER + "/standard"
        sub_path = UPLOAD_FOLDER + "/submission"
        _log.getLogger().debug(std_path)
        args = {
            "compare": True,
            "--standard": std_path,
            "--submission": False,
            "analytics": False,
            "--path": False,
            "input": True,
            "clean": False,
            "--clean": False,
            "--empath": False,
            "--gitc": False,
            "--character": False,
            "--nn": False,
            "--text": "shall include security"
        }
        _log.getLogger().debug("Running Main")
        app_main(args)

        return "success"
        # _log.getLogger().debug("Files")
        # print(f)


if __name__ == "__main__":
    app.run(debug=True)
