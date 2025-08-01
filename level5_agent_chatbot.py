"""
This script demonstrates an agent-based RAG pipeline.
An agent orchestrates multiple tools (retriever, generator, summarizer) to answer user queries.
The agent decides which tools to invoke based on the query type.
"""

from typing import List, Dict, Any

# -------------------------------
# Simulated Document Store
# -------------------------------
DOCUMENTS = [
    "Retrieval-Augmented Generation (RAG) combines retrieval and generation for better answers.",
    "LangChain is a framework for building applications with language models.",
    "Transformers are the backbone of modern NLP models including RAG.",
    "RAG is used in chatbots, search engines, and document summarization.",
    "Metadata filtering allows more precise document retrieval in RAG systems."
]

# -------------------------------
# Tool: Retriever
# -------------------------------
def keyword_retriever(query: str, documents: List[str]) -> List[str]:
    """
    Retrieves documents that contain any keyword from the query.
    """
    keywords = query.lower().split()
    return [doc for doc in documents if any(keyword in doc.lower() for keyword in keywords)]

# -------------------------------
# Tool: Generator
# -------------------------------
def simple_generator(query: str, context_docs: List[str]) -> str:
    """
    Generates a response by concatenating retrieved documents.
    """
    if not context_docs:
        return "No relevant information found."
    return " ".join(context_docs)

# -------------------------------
# Tool: Summarizer
# -------------------------------
def simple_summarizer(text: str) -> str:
    """
    Simulates summarization by returning the first sentence.
    """
    return text.split(".")[0] + "." if "." in text else text

# -------------------------------
# Agent Logic
# -------------------------------
class RAGAgent:
    """
    Agent that decides which tools to invoke based on the query.
    """
    def __init__(self, documents: List[str]):
        self.documents = documents

    def decide_tools(self, query: str) -> Dict[str, Any]:
        """
        Determines which tools to use based on keywords in the query.
        """
        query_lower = query.lower()
        use_summary = "summarize" in query_lower or "brief" in query_lower
        use_retrieval = True  # Always retrieve documents
        use_generation = not use_summary  # Generate full answer unless summarization is requested

        return {
            "use_retrieval": use_retrieval,
            "use_generation": use_generation,
            "use_summary": use_summary
        }

    def run(self, query: str) -> str:
        """
        Executes the agent-based RAG pipeline.
        """
        decision = self.decide_tools(query)

        # Step 1: Retrieve documents
        retrieved_docs = keyword_retriever(query, self.documents) if decision["use_retrieval"] else []

        # Step 2: Generate or summarize response
        if decision["use_generation"]:
            response = simple_generator(query, retrieved_docs)
        elif decision["use_summary"]:
            full_text = " ".join(retrieved_docs)
            response = simple_summarizer(full_text)
        else:
            response = "No tools selected to answer the query."

        return response

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    agent = RAGAgent(documents=DOCUMENTS)

    # Sample queries
    queries = [
        "What is RAG used for?",
        "Summarize the role of transformers in RAG.",
        "Tell me briefly about LangChain."
    ]

    for q in queries:
        print("User Query:", q)
        print("Agent Response:", agent.run(q))
        print("-" * 50)