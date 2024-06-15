import os, sys
from flask import (
    request,
    redirect,
    jsonify,
    Blueprint,
)


# ________________ HANDLE THE PATH THING ________________ #
# get the absolute path of the script's directory
script_path = os.path.dirname(os.path.abspath(__file__))
# get the parent directory of the script's directory
parent_path = os.path.dirname(script_path)
sys.path.append(parent_path)


from Bird_classification_engine.make_prediction_YOLOv8 import YOLOv8_classifier
from Bird_classification_engine.class_indices import Class_indices

from exception import CustomException
from time import time
from uuid import uuid4


yolov8_bp = Blueprint("yolov8_bp", __name__)


UPLOAD_FOLDER = os.path.join(parent_path, "static", "image_to_classify")


@yolov8_bp.route("/bird-classifier", methods=["POST"])
async def upload_image_YOLOv8():
    try:

        # empty the folder image_to_classify before doing anything
        for item in os.listdir(UPLOAD_FOLDER):
            item_path = os.path.join(UPLOAD_FOLDER, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)

        if request.method == "POST":
            if "image" not in request.files:
                print("There is no file")
                return redirect(request.url)

            image = request.files["image"]

            if image.filename == "":
                print("No image uploaded")
                return redirect(request.url)

            if image:
                start_time = time()

                # get the original file extension (e.g., .jpg, .png)
                file_ext = os.path.splitext(image.filename)[1]
                # generate a unique filename by using uuid
                unique_image_name = f"{uuid4()}{file_ext}"

                full_image_path = os.path.join(UPLOAD_FOLDER, unique_image_name)
                image.save(full_image_path)

                classifier = YOLOv8_classifier(UPLOAD_FOLDER)

                (
                    predicted_probability,
                    predicted_label,
                    predicted_scientific_name,
                ) = classifier.make_prediction()

                predicted_label = predicted_label.capitalize()
                # to handle the scientific name styling
                predicted_scientific_name = (
                    predicted_scientific_name[0].capitalize()
                    + predicted_scientific_name[1:].lower()
                )

                execution_time = round(time() - start_time, 2)

        # set the threshold to 0.65
        if round(float(predicted_probability), 4) >= 0.65:
            return jsonify(
                {
                    "predicted_probability": round(float(predicted_probability), 4),
                    "predicted_label": predicted_label,
                    "predicted_scientific_name": predicted_scientific_name,
                    "predicted_index": "NA",
                    "execution_time": execution_time,
                }
            )
        else:
            return jsonify(
                {
                    "predicted_probability": round(float(predicted_probability), 4),
                    "predicted_label": "Sorry, I can't recognize this birdie.",
                    "predicted_scientific_name": "",
                    "predicted_index": "",
                    "execution_time": execution_time,
                }
            )

    except Exception as e:
        raise CustomException(e, sys)
