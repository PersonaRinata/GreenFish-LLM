import openai
from langchain.vectorstores import Chroma  # 导入Chroma向量存储库
from langchain.document_loaders import PyMuPDFLoader  # 导入PyMuPDFLoader文档加载库
from langchain.text_splitter import RecursiveCharacterTextSplitter  # 导入RecursiveCharacterTextSplitter文本拆分库
from langchain.document_loaders import UnstructuredMarkdownLoader  # 导入UnstructuredMarkdownLoader文档加载库
from langchain.document_loaders import UnstructuredFileLoader  # 导入UnstructuredFileLoader文档加载库
from langchain.embeddings.openai import OpenAIEmbeddings  # 导入OpenAIEmbeddings嵌入库
import os
from dotenv import load_dotenv


def load_docs():
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.base_url = os.getenv('OPENAI_BASE_URL')

    base_path = '../../knowledge_db/'
    dirs = os.listdir(base_path)
    print(dirs)

    docs_set = []
    for dir in dirs:
        # 创建加载器列表
        loaders = []
        # 创建文档列表
        docs = []
        # 指定 PDF 文件所在的文件夹路径
        category_path = os.path.join(base_path, dir)
        print(f'category_path:{category_path}')
        # ../../ knowledge_db / type0
        folder_paths = os.listdir(category_path)
        for folder_path in folder_paths:
            # 获取文件夹中的所有文件名
            print(f'folder_path:{folder_path}')
            file_path = os.path.join(category_path, folder_path)
            files = os.listdir(file_path)
            print(f'file_path:{file_path}')
            if folder_path == 'pdf':
                # 遍历文件列表
                for one_file in files:
                    print(os.path.join(file_path, one_file))
                    # 根据文件路径创建 PyMuPDFLoader 加载器
                    loader = PyMuPDFLoader(os.path.join(file_path, one_file))

                    # 将加载器添加到列表中
                    loaders.append(loader)

                # 遍历加载器列表
                for loader in loaders:
                    # 加载文档并将其添加到文档列表中
                    docs.extend(loader.load())

            elif folder_path == 'md':
                # 遍历文件列表
                for one_file in files:
                    # 根据文件路径创建 UnstructuredMarkdownLoader 加载器
                    loader = UnstructuredMarkdownLoader(os.path.join(file_path, one_file))

                    # 将加载器添加到列表中
                    loaders.append(loader)

                # 遍历加载器列表
                for loader in loaders:
                    # 加载文档并将其添加到文档列表中
                    docs.extend(loader.load())

        docs_set.append(docs)
    return docs_set


# print(load_docs())
