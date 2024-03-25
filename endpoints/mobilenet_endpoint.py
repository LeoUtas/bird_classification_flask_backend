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


from Bird_classification_engine.make_prediction_mobilenet import (
    MobileNet_classifier,
    Class_indices,
)
from Bird_classification_engine.data_ingestion import Data_ingestion
from exception import CustomException
from time import time
from uuid import uuid4


mobilenet_bp = Blueprint("mobilenet_bp", __name__)


UPLOAD_FOLDER = os.path.join(parent_path, "static", "image_to_classify")

class_indices_handler = Class_indices()


@mobilenet_bp.route("/bird-classifier", methods=["POST"])
async def upload_image_MobileNet():
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

                Data_ingestion_handler = Data_ingestion(unique_image_name)
                image = Data_ingestion_handler.make_data_in()

                classifier = MobileNet_classifier(image)

                (
                    predicted_probability,
                    predicted_label,
                    predicted_scientific_name,
                    predicted_index,
                ) = classifier.make_prediction()

                predicted_label = predicted_label.capitalize()
                # to handle the scientific name styling
                predicted_scientific_name = (
                    predicted_scientific_name[0].capitalize()
                    + predicted_scientific_name[1:].lower()
                )
                predicted_index = int(predicted_index)

                execution_time = round(time() - start_time, 2)

            return jsonify(
                {
                    "predicted_probability": round(float(predicted_probability), 4),
                    "predicted_label": predicted_label,
                    "predicted_scientific_name": predicted_scientific_name,
                    "predicted_index": predicted_index,
                    "execution_time": execution_time,
                }
            )

    except Exception as e:
        raise CustomException(e, sys)
