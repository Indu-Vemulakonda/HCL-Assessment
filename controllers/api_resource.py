import json
from app import *
import openai
from flask_cors import CORS
from flask_restful import Resource
from ai_utilities import *


CORS(app)

response_id = 0


class LLMApi(Resource):
    # GET end point
    def get(self, usr_msg):
        system_response = get_system_response(usr_msg)
        response_id += 1
        json_response = json.dumps(
            {"reponse_id": response_id, "response": system_response}
        )
        return json_response

    # PUT end point
    def put(self, system_content):
        set_system_content(system_content)
        json_response = json.dumps({"role": "system", "content": system_content})
        return json_response

    # DELETE end point
    def delete(self):
        delete_system_content()
        return "Successfully Deleted", 200

    # POST end point
    def post(self, system_content):
        set_system_content(system_content)
        json_response = json.dumps({"role": "system", "content": system_content})
        return json_response


api.add_resource(PostResource, "/posts/<int:post_id>")
