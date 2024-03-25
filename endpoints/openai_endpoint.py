import sys, os
from dotenv import load_dotenv


from flask import (
    request,
    jsonify,
    Blueprint,
)


# ________________ HANDLE THE PATH THING ________________ #
# get the absolute path of the script's directory
script_path = os.path.dirname(os.path.abspath(__file__))
# get the parent directory of the script's directory
parent_path = os.path.dirname(script_path)
sys.path.append(parent_path)


from funfact_engine.openai_requests import OpenaiAPI
from exception import CustomException


# ________________ CONFIG OPENAI API ________________ #
load_dotenv()
api_key = os.getenv("OPENAI_FUNFACT_API_KEY")
model_text_generation = os.getenv("chosen_model_text_generation")


model = "gpt-3.5-turbo"
role = "assistant"
personality = "professional"
note = ""


openai_engine = OpenaiAPI(
    api_key,
    model,
)


openai_funfact_bp = Blueprint("openai_funfact_bp", __name__)


@openai_funfact_bp.route("/funfact", methods=["POST"])
async def get_ai_response():

    try:

        data = request.get_json()

        # Check if there's text data in the request
        if not data or "text" not in data:
            return jsonify({"error": "No text provided"}), 400

        species = data["text"]

        prompt = (
            f"You are a {personality} zoologist, "
            + f"telling a fun fact about a bird species, {species}."
            + f"{note}"
        )

        ai_response = openai_engine.request_openai_response_for_funfact(
            role=role, prompt=prompt
        )

        return jsonify({"ai_response": ai_response})

    except Exception as e:
        raise CustomException(e, sys)


# test code execution
if __name__ == "__main__":
    print(api_key)
