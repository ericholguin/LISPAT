DESIRED_TERMS = [
    "asset",
    "authentication",
    "authenticity",
    "authorization",
    "availability",
    "confidentiality",
    "configuration",
    "cryptographically strong",
    "cybersecurity",
    "cybersecurity bill of materials",
    "cbom",
    "denial of service",
    "encryption",
    "end of support",
    "integrity",
    "jitter",
    "life-cycle",
    "malware",
    "patchability",
    "updatability",
    "patient harm",
    "privileged user",
    "quality of service",
    "risk",
    "risk analysis",
    "trustworthy device",
    "regulations",
    "regulatory",
    "regulation"
]

DESIRED_PHRASE = [
    "shall",
    "required",
    "requires",
    "must",
    "need",
    "has"
]

css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""

LISPAT_DOCOPT = """Lost in Space and Time.

Usage:
    lispat analytics --path=<content-path>  [--train] [--compare] [--array] [--df] [--sp] [-A]
    lispat convert --docA=<content-path> --docB=<content-path>
    lispat compare --standard=<content-path> --submission=<content-path> [--clean] [--empath] [--gitc] [--character] [--nn]
    lispat compare input --standard=<content-path> --text=<text> --nn
    lispat clean [--all]
    lispat [-h | --help]
    lispat --version

Options:

  -h --help                      Show this screen.
  --version                      Show version.

  Analytics:
    analytics                    A look at the data given, whether its a single doc or directory of docs.

    Args:
    --convert                    Convert Documents to .txt format
    --compare                    Submit a Document to be compared
    --train                      Submit documents to be used for training data
    --array                      Processing data as an array
    --df                         Processing data as a dataframe
    --sp                         Get semantic properties
    -A                           Get all processed txt data.
    --path=<content-path>        Process data from a single path. multiple docs or single docs

                Example: lispat analytics --path=<content-path> --train --array --df

  Comparisons:
    compare                      Compare a standard with a submission

    Args:
    --standard=<content-path>    A standard document to use for comparing against a submission
    --submission=<content-path>  A submission document to use for comparing against a standard.

                Example: lispat compare --standard=<content-path> --submission=<content_path>

  Utilities:
     clean                        remove data in local storage.
     --all                        remove all data in local storage.

"""


def args_convert(filenames):
    args = {
        "convert": True,
        "--docA": filenames[0],
        "--docB": filenames[1],
        "filter": False,
        "data": False,
        "graph":False,
        "all": False,
        "compare": False,
        "--standard": False,
        "--submission": False,
        "analytics": False,
        "--path": False,
        "input": False,
        "clean": False,
        "--clean": False,
        "--empath": False,
        "--gitc": False,
        "--character": False,
        "--nn": False,
        "--text": False
    }
    return args


def args_filter():
    args = {
        "convert": False,
        "--docA": False,
        "--docB": False,
        "filter": True,
        "data": False,
        "graph":False,
        "all": False,
        "compare": False,
        "--standard": False,
        "--submission": False,
        "analytics": False,
        "--path": False,
        "input": False,
        "clean": False,
        "--clean": False,
        "--empath": False,
        "--gitc": False,
        "--character": False,
        "--nn": False,
        "--text": False
    }
    return args


def args_json():
    args = {
        "convert": False,
        "--docA": False,
        "--docB": False,
        "filter": False,
        "data": True,
        "graph": False,
        "all": False,
        "compare": False,
        "--standard": False,
        "--submission": False,
        "analytics": False,
        "--path": False,
        "input": False,
        "clean": False,
        "--clean": False,
        "--empath": False,
        "--gitc": False,
        "--character": False,
        "--nn": False,
        "--text": False
    }
    return args


def args_clean():
    args = {
        "convert": False,
        "--docA": False,
        "--docB": False,
        "filter": False,
        "data": False,
        "graph":False,
        "all": False,
        "compare": False,
        "--standard": False,
        "--submission": False,
        "analytics": False,
        "--path": False,
        "input": False,
        "clean": True,
        "--clean": False,
        "--empath": False,
        "--gitc": False,
        "--character": False,
        "--nn": False,
        "--text": False
    }
    return args


def args_all():
    args = {
        "convert": False,
        "--docA": False,
        "--docB": False,
        "filter": False,
        "data": False,
        "graph":False,
        "all": True,
        "compare": False,
        "--standard": False,
        "--submission": False,
        "analytics": False,
        "--path": False,
        "input": False,
        "clean": False,
        "--clean": False,
        "--empath": False,
        "--gitc": False,
        "--character": False,
        "--nn": False,
        "--text": False
    }
    return args


def args_graph():
    args = {
        "convert": False,
        "--docA": False,
        "--docB": False,
        "filter": False,
        "data": False,
        "graph": True,
        "all": False,
        "compare": False,
        "--standard": False,
        "--submission": False,
        "analytics": False,
        "--path": False,
        "input": False,
        "clean": False,
        "--clean": False,
        "--empath": False,
        "--gitc": False,
        "--character": False,
        "--nn": False,
        "--text": False
    }
    return args
