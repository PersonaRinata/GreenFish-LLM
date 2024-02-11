import os

import openai
from dotenv import load_dotenv

from server.service.chain import get_chain

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.base_url = os.getenv('OPENAI_BASE_URL')

chain = get_chain('type0')
ans=chain.invoke(
    input={"query": "灰色预测的步骤"}
)

print(ans)