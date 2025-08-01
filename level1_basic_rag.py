# This script represents the first level of a Retrieval-Augmented Generation (RAG) pipeline.
# It demonstrates a basic RAG setup where a user query is answered using retrieved documents and a language model.

# Import necessary libraries
from typing import List

# Simulated document store (in a real-world scenario, this could be a vector database or search engine)
DOCUMENTS = [
    "Retrieval-Augmented Generation (RAG) combines information retrieval with natural language generation.",
    "RAG models retrieve relevant documents from a knowledge base to answer queries more accurately.",
    "The transformer architecture is commonly used in RAG models for both retrieval and generation tasks.",
    "Applications of RAG include question answering, chatbots, and document summarization."
]

# Function to simulate document retrieval based on keyword matching
def retrieve_documents(query: str, documents: List[str]) -> List[str]:
    """
    Retrieve documents that contain any keyword from the query.
    This is a simple keyword-based retrieval for demonstration purposes.
    """
    keywords = query.lower().split()  # Split the query into lowercase keywords
    retrieved = [doc for doc in documents if any(keyword in doc.lower() for keyword in keywords)]
    return retrieved

# Function to simulate a language model generating an answer from retrieved documents
def generate_answer(query: str, retrieved_docs: List[str]) -> str:
    """
    Generate a simple answer by concatenating relevant documents.
    In a real RAG pipeline, this would involve a language model like GPT.
    """
    if not retrieved_docs:
        return "No relevant information found."
    return " ".join(retrieved_docs)  # Combine all retrieved documents into a single response

# Main function to run the basic RAG pipeline
def basic_rag_pipeline(query: str) -> str:
    """
    Executes the basic RAG pipeline:
    1. Retrieve relevant documents.
    2. Generate an answer using the retrieved documents.
    """
    retrieved = retrieve_documents(query, DOCUMENTS)  # Step 1: Retrieve documents
    answer = generate_answer(query, retrieved)        # Step 2: Generate answer
    return answer

# Example usage
if __name__ == "__main__":
    user_query = "What is RAG used for?"  # Sample query
    response = basic_rag_pipeline(user_query)  # Run the pipeline
    print("User Query:", user_query)
    print("RAG Response:", response)