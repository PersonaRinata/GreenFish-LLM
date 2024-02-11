from flask import Flask
from server.api.chat import create_chat_route

app = Flask(__name__)

create_chat_route(app)

if __name__ == '__main__':
    app.run(debug=True)
