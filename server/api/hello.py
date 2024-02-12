from flask import jsonify


def create_hello_route(app):
    @app.route('/hello', methods=['GET'])
    def hello_route():
        return jsonify({"msg": "hello"})
