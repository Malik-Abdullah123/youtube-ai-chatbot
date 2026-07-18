from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)
from dotenv import load_dotenv

load_dotenv()

# -------------------------------
# Global Variables
# -------------------------------

vector_store = None
retriever = None

chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

# -------------------------------
# LLM & Embeddings
# -------------------------------

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Previous Conversation:
{history}

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=[
        "history",
        "context",
        "question"
    ],
)


# -------------------------------
# Helper Functions
# -------------------------------

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def format_history(history):
    return "\n".join(
        f"{msg.type}: {msg.content}"
        for msg in history
    )


# -------------------------------
# Load YouTube Video
# -------------------------------

def load_video(video_id):

    global vector_store
    global retriever
    global chat_history

    ytt = YouTubeTranscriptApi()

    transcript_list = ytt.fetch(
        video_id,
        languages=["en"]
    )

    transcript = " ".join(
        chunk.text
        for chunk in transcript_list
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.create_documents([transcript])

    vector_store = FAISS.from_documents(
        docs,
        embeddings
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":4}
    )

    # New video => reset history
    chat_history = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]


# -------------------------------
# Ask Question
# -------------------------------

def ask_question(question):

    global retriever
    global chat_history

    if retriever is None:
        return "Please load a YouTube video first."

    chat_history.append(
        HumanMessage(content=question)
    )

    parallel_chain = RunnableParallel(
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
            "history": RunnableLambda(
                lambda _: format_history(chat_history)
            ),
        }
    )

    final_chain = (
        parallel_chain
        | prompt
        | llm
        | parser
    )

    answer = final_chain.invoke(question)

    chat_history.append(
        AIMessage(content=answer)
    )

    return answer