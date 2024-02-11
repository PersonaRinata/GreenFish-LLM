import os

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from server.service.load import get_retrieval


def get_chain(category: str):
    from langchain.prompts import PromptTemplate

    template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
    案。尽量使答案具体清晰。总是在回答的最后说“谢谢你的提问！”。
    {context}
    问题: {question}
    有用的回答:"""

    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"],
                                     template=template)
    retrieval = get_retrieval(category)

    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

    # 声明一个检索式问答链
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=retrieval,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    return qa_chain
