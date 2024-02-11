from server.service.load import get_retrieval
from flask import request, jsonify
from tools.error import *
from tools.resp import base_resp
from server.service.chain import get_chain


def create_chat_route(app):
    @app.route('/chat', methods=['POST'])
    def chat_route():
        try:
            req = request.get_json()
        except KeyError:
            print("KeyError")
            return jsonify(base_resp(param_error))
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify(base_resp(internal_server_error))

        try:
            question = req['question']
            category = req['category']
        except KeyError:
            print("key error")
            return jsonify(base_resp(param_error))
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify(base_resp(internal_server_error))

        chain = get_chain(category)
        chain.invoke(
            input={"question": question}
        )


