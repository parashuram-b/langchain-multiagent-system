from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.tools import Tool
import logging
logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def calculator(expr: str):
    try:
        return str(eval(expr))
    except:
        return "Invalid calculation"

calc_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Performs mathematical calculations"
)

llm = Ollama(model="llama2")

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

embeddings = OllamaEmbeddings(model="llama2")
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(),
    memory=memory
)

print("🤖 Knowledge Bot ready. Type 'exit' to quit.")

while True:
    q = input("You: ")

    if q.lower() == "exit":
        print("Bot: Bye 👋")
        break

    tool_keywords = ["calculate", "add", "subtract", "multiply", "divide", "+", "-", "*", "/"]

    try:
        if any(k in q.lower() for k in tool_keywords):
            answer = calculator(q)
            print("Bot (tool):", answer)
        else:
            result = qa.invoke({"question": q})
            print("Bot:", result["answer"])

    except Exception as e:
        print("Bot: Sorry, something went wrong.")
