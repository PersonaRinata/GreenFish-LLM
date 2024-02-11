import os

from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from server.service.split import split_docs

from server.service.load import load_docs


def persist_vector_db(category: str, s_docs):
    # 定义 Embeddings
    embedding = OpenAIEmbeddings()
    base_directory = '../../data_base/chroma/'
    # 定义持久化路径
    persist_directory = os.path.join(base_directory, category)

    # 加载数据库
    vectordb = Chroma.from_documents(
        documents=split_docs(s_docs),
        embedding=embedding,
        persist_directory=persist_directory  # 允许我们将persist_directory目录保存到磁盘上
    )

    # 向量数据库持久化
    vectordb.persist()


if __name__ == '__main__':
    docs_dict = load_docs()
    for category, docs in docs_dict.items():
        persist_vector_db(category, docs)
