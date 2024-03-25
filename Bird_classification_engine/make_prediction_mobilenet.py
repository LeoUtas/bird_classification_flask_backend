import os, sys

# ________________ HANDLE THE PATH THING ________________ #
# get the absolute path of the script's directory
script_path = os.path.dirname(os.path.abspath(__file__))
# get the parent directory of the script's directory
parent_path = os.path.dirname(script_path)
sys.path.append(parent_path)


import numpy as np
from tensorflow.keras.models import load_model
from exception import CustomException
from Bird_classification_engine.class_indices import Class_indices


class MobileNet_classifier:
    """
    This class is the core part of the project. It loads a chosen model of MobileNet, class indices and retrieve uploaded images to use in prediction generating a series of probabilities for class indices, the class index, with the highest probability, will be chosen and mapped with its label (i.e., common name) and scientific name.

    """

    def __init__(self, image):
        """
        This initialization part is to load required items, including a chosen model, class indices, and the test image.

        """

        model_path = os.path.join(script_path, "models", "h5", "chosen_model.h5")
        self.model = load_model(model_path)
        Class_indices_handler = Class_indices()
        self.class_indices = Class_indices_handler.make_class_indices()

        self.image = image

    def make_prediction(self):
        """
        This function handles the prediciton process.

        """

        try:
            # make prediction
            probabilities = self.model.predict(self.image)[0]
            prediction = np.argmax(probabilities)

            predicted_probability = probabilities[prediction]
            prediction_dict = self.class_indices[prediction]
            predicted_label = prediction_dict["label"]
            predicted_scientific_name = prediction_dict["scientific_name"]

            return (
                predicted_probability,
                predicted_label,
                predicted_scientific_name,
                prediction,
            )

        except Exception as e:
            raise CustomException(e, sys)


# test code execution
# if __name__ == "__main__":
#     from data_ingestion import Data_ingestion

#     image_name = os.path.join(parent_path, "static", "images", "003.jpg")
#     Data_ingestion_handler = Data_ingestion(image_name)
#     image = Data_ingestion_handler.make_data_in()

#     classifier = MobileNet_classifier(image)
#     predicted_class = classifier.make_prediction()
#     print(predicted_class)
