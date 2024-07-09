import flask
from werkzeug.utils import secure_filename

from segmenter.segmenter import segment_file

bp = flask.Blueprint("segmenter", __name__)

ALLOWED_EXTENSIONS = {"mp3", "wav", "ogg", "aif"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def log_request_start(request):
    print("---------- ---------- ---------- ----------")
    print(request.url)
    print("\n")


def mk_error_response(msg, status_code):
    message = {
        "status": status_code,
        "message": msg,
    }
    response = flask.jsonify(message)
    response.status_code = status_code
    response.headers.add("Access-Control-Allow-Origin", "*")

    print(f"Serving error response with message `{msg}`: {response}")

    return response


def mk_success_response(msg):
    message = {
        "status": 200,
        "message": msg,
    }
    response = flask.jsonify(message)
    response.status_code = 200
    response.headers.add("Access-Control-Allow-Origin", "*")

    print(f"Serving success response: {response}")

    return response


def get_segments(filepath):
    segment_hierarchy, segment_hierarchy2 = segment_file(filepath)

    print(
        "Num segments per k:",
        [(ix, len(i[1])) for ix, i in enumerate(segment_hierarchy)],
    )

    json_output = []
    for ix, i in enumerate(segment_hierarchy):
        k = ix + 1
        level_dict = {
            k: {
                "branchTimes": [i[0] for i in segment_hierarchy[ix][0]],
                "segmentLabels": [int(i) for i in segment_hierarchy[ix][1]],
            }
        }
        json_output.append(level_dict)

    return json_output



@bp.route("/segment", methods=["GET"])
def segment():
    """Accepts an audio file and returns a JSON object with segment information. Does not save audio."""

    request = flask.request
    log_request_start(request)

    print(request.files)
    if "file" not in request.files:
        return mk_error_response("No file", 400)

    fh = request.files["file"]
    filename = fh.filename
    print(filename, fh)

    if not fh or filename == "":
        return mk_error_response("No selected file", 400)

    if not allowed_file(fh.filename):
        return mk_error_response("Invalid file extension", 400)

    filename = secure_filename(fh.filename)
    print(f"Received {filename=}")

    segments = get_segments(fh)

    response = flask.jsonify(segments)

    response.headers.add("Access-Control-Allow-Origin", "*")
    print(f"serving {response=}")
    return response
