from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

loader = DirectoryLoader("data", glob="*.txt")
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
documents = splitter.split_documents(docs)

embeddings = OllamaEmbeddings(model="llama2")
db = FAISS.from_documents(documents, embeddings)

db.save_local("vectorstore")
print("Multi-file vector store created")
