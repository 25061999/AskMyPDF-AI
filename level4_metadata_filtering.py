"""
This script demonstrates a Retrieval-Augmented Generation (RAG) pipeline
that incorporates metadata tagging and filtering during document retrieval.

Each document is associated with metadata such as source, topic, and date.
The retriever filters documents based on both keyword relevance and metadata constraints.
"""

from typing import List, Dict, Any

# -------------------------------
# Simulated Document Store with Metadata
# -------------------------------
DOCUMENTS_WITH_METADATA = [
    {
        "content": "Retrieval-Augmented Generation (RAG) combines retrieval and generation for better answers.",
        "metadata": {"source": "Wikipedia", "topic": "RAG", "date": "2023-01-01"}
    },
    {
        "content": "LangChain is a framework for building applications with language models.",
        "metadata": {"source": "LangChain Docs", "topic": "LangChain", "date": "2023-02-15"}
    },
    {
        "content": "Transformers are the backbone of modern NLP models including RAG.",
        "metadata": {"source": "Arxiv", "topic": "Transformers", "date": "2022-12-10"}
    },
    {
        "content": "RAG is used in chatbots, search engines, and document summarization.",
        "metadata": {"source": "Blog", "topic": "RAG", "date": "2023-03-05"}
    },
    {
        "content": "Metadata filtering allows more precise document retrieval in RAG systems.",
        "metadata": {"source": "Research Paper", "topic": "Metadata", "date": "2023-04-01"}
    }
]

# -------------------------------
# Metadata-Aware Retriever
# -------------------------------
def metadata_filtering_retriever(query: str, documents: List[Dict[str, Any]], metadata_filter: Dict[str, str]) -> List[str]:
    """
    Retrieves documents that match the query keywords and satisfy the metadata filter.

    Parameters:
        query (str): The user query.
        documents (List[Dict]): A list of documents with 'content' and 'metadata'.
        metadata_filter (Dict[str, str]): Metadata constraints (e.g., {"topic": "RAG"}).

    Returns:
        List[str]: A list of document contents that match the query and metadata.
    """
    keywords = query.lower().split()
    filtered_docs = []

    for doc in documents:
        content = doc["content"].lower()
        metadata = doc["metadata"]

        # Check if any keyword is in the content
        keyword_match = any(keyword in content for keyword in keywords)

        # Check if all metadata filters match
        metadata_match = all(metadata.get(k) == v for k, v in metadata_filter.items())

        if keyword_match and metadata_match:
            filtered_docs.append(doc["content"])

    return filtered_docs

# -------------------------------
# Simple Generator
# -------------------------------
def simple_generator(query: str, context_docs: List[str]) -> str:
    """
    Generates a response by concatenating retrieved documents.

    Parameters:
        query (str): The user query.
        context_docs (List[str]): Retrieved documents.

    Returns:
        str: Generated response.
    """
    if not context_docs:
        return "No relevant documents found for the given query and metadata filter."
    return " ".join(context_docs)

# -------------------------------
# Metadata-Aware RAG Pipeline
# -------------------------------
class MetadataRAGPipeline:
    """
    A RAG pipeline that supports metadata filtering during retrieval.
    """
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def run(self, query: str, metadata_filter: Dict[str, str]) -> str:
        """
        Executes the RAG pipeline with metadata filtering.

        Parameters:
            query (str): The user query.
            metadata_filter (Dict[str, str]): Metadata constraints.

        Returns:
            str: Generated response.
        """
        retrieved_docs = self.retriever(query, DOCUMENTS_WITH_METADATA, metadata_filter)
        return self.generator(query, retrieved_docs)

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Instantiate the pipeline
    pipeline = MetadataRAGPipeline(
        retriever=metadata_filtering_retriever,
        generator=simple_generator
    )

    # Define a query and metadata filter
    user_query = "What is RAG used for?"
    metadata_constraints = {"topic": "RAG"}

    # Run the pipeline
    response = pipeline.run(user_query, metadata_constraints)

    # Output the result
    print("User Query:", user_query)
    print("Metadata Filter:", metadata_constraints)
    print("RAG Response:", response)