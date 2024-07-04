import json
from app import *
from flask_restful import Resource, Api
from ai_utilities import *


api = Api(app)

response_id = 0


class LLMApi(Resource):
    # GET end point
    def get(self, user_msg):
        print("Hi, get")
        system_response = get_system_response(user_msg)
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


api.add_resource(
    LLMApi,
    "/api/chat-bot/<user_msg>",
    "/api/chat-bot/<system_content>",
    "/api/chat-bot/",
)
