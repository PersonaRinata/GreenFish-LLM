from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from server.service.split import split_docs

def persist_vector_db():
    # 定义 Embeddings
    embedding = OpenAIEmbeddings()

    # 定义持久化路径
    persist_directory = '../data_base/vector_db/chroma'

    # 加载数据库
    vectordb = Chroma.from_documents(
        documents=split_docs(),
        embedding=embedding,
        persist_directory=persist_directory  # 允许我们将persist_directory目录保存到磁盘上
    )

    # 向量数据库持久化
    vectordb.persist()

persist_vector_db()