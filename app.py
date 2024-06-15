import os, sys
from dotenv import load_dotenv

# ________________ HANDLE THE PATH THING ________________ #
# get the absolute path of the script's directory
script_path = os.path.dirname(os.path.abspath(__file__))
# get the parent directory of the script's directory
parent_path = os.path.dirname(script_path)
sys.path.append(parent_path)


from flask import Flask

from endpoints.YOLOv8_endpoint import yolov8_bp


app = Flask(__name__, static_folder="static")

load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def render_index():
    return "hello world"


app.register_blueprint(yolov8_bp, url_prefix="/yolov8")


if __name__ == "__main__":
    port = int(
        os.environ.get("PORT", 5001)
    )  # define port so we can map container port to localhost
    app.run(host="0.0.0.0", port=port, debug=False)  # define 0.0.0.0 for Docker
