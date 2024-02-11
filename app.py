import os
import sys

import openai
from flask import Flask
from server.api.chat import create_chat_route
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
# openai.api_key = os.getenv('OPENAI_API_KEY')
# openai.base_url = os.getenv('OPENAI_BASE_URL')
# sys.path.append(os.path.abspath(sys.path[0]))


app = Flask(__name__)

create_chat_route(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
