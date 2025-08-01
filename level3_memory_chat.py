from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Step 1: Load and split documents
loader = TextLoader("file:///C:/Users/VKUMAR86/Downloads/Explainx.ai_RAG.pdf")  # Replace with your actual document path
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Step 2: Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# Step 3: Initialize conversational memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Step 4: Create conversational retrieval chain
llm = OpenAI(temperature=0)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    memory=memory
)

# Step 5: Simulate a conversation
questions = [
    "What is the document about?",
    "Can you elaborate on the main topic?",
    "Who is the intended audience?"
]

for question in questions:
    result = qa_chain.run(question)
    print(f"Q: {question}")
    print(f"A: {result}\n")