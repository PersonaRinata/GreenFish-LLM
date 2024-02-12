from flask import Flask
from server.api.chat import create_chat_route
from server.api.hello import create_hello_route
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

if __name__ == '__main__':
    app = Flask(__name__)
    create_chat_route(app)
    create_hello_route(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
