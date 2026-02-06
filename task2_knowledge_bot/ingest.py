from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

loader = TextLoader("data/knowledge.txt")
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
documents = splitter.split_documents(docs)

embeddings = OllamaEmbeddings(model="llama2")
db = FAISS.from_documents(documents, embeddings)

db.save_local("vectorstore")
print("Vector store created successfully")
