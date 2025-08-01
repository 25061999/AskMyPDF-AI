# This script demonstrates a modular Retrieval-Augmented Generation (RAG) pipeline.
# It separates the retrieval and generation components into modular functions,
# mimicking the design of LangChain-style pipelines.

from typing import List

# -------------------------------
# Simulated Document Store
# -------------------------------
DOCUMENTS = [
    "Retrieval-Augmented Generation (RAG) combines information retrieval with natural language generation.",
    "RAG models retrieve relevant documents from a knowledge base to answer queries more accurately.",
    "The transformer architecture is commonly used in RAG models for both retrieval and generation tasks.",
    "Applications of RAG include question answering, chatbots, and document summarization.",
    "LangChain is a framework for developing applications powered by language models."
]

# -------------------------------
# Retriever Module
# -------------------------------
def keyword_retriever(query: str, documents: List[str]) -> List[str]:
    """
    A simple keyword-based retriever.
    It returns documents that contain any of the keywords from the query.
    This simulates how a retriever might work in a real RAG system.
    """
    keywords = query.lower().split()  # Break query into lowercase keywords
    retrieved_docs = [doc for doc in documents if any(keyword in doc.lower() for keyword in keywords)]
    return retrieved_docs

# -------------------------------
# Generator Module
# -------------------------------
def simple_generator(query: str, context_docs: List[str]) -> str:
    """
    A simple generator that concatenates retrieved documents to form a response.
    In a real-world scenario, this would use a language model like GPT.
    """
    if not context_docs:
        return "I'm sorry, I couldn't find any relevant information."
    return "Based on the retrieved documents: " + " ".join(context_docs)

# -------------------------------
# RAG Pipeline Class
# -------------------------------
class ModularRAGPipeline:
    """
    A modular RAG pipeline that separates retrieval and generation logic.
    This design allows for easy swapping of components (retrievers, generators).
    """
    def __init__(self, retriever, generator):
        self.retriever = retriever  # Assign retriever function
        self.generator = generator  # Assign generator function

    def run(self, query: str) -> str:
        """
        Executes the RAG pipeline:
        1. Retrieve relevant documents using the retriever.
        2. Generate a response using the generator.
        """
        retrieved = self.retriever(query, DOCUMENTS)  # Step 1: Retrieve documents
        response = self.generator(query, retrieved)   # Step 2: Generate response
        return response

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Instantiate the pipeline with the keyword retriever and simple generator
    rag_pipeline = ModularRAGPipeline(retriever=keyword_retriever, generator=simple_generator)

    # Sample query
    user_query = "What is LangChain and how is it used in RAG?"

    # Run the pipeline
    answer = rag_pipeline.run(user_query)

    # Output the result
    print("User Query:", user_query)
    print("RAG Response:", answer)