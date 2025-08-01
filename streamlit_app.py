# Streamlit UI for RAG Pipeline Demo with Metadata Filtering

import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="RAG Pipeline Demo", layout="centered")

# -------------------------------
# Title and Description
# -------------------------------
st.title("🔍 Retrieval-Augmented Generation (RAG) Demo")
st.write("""
This demo showcases a multi-level RAG pipeline with metadata filtering.
Enter a query below and optionally apply metadata filters to refine document retrieval.
""")

# -------------------------------
# Input Section
# -------------------------------
st.header("📝 User Query")
query = st.text_input("Enter your question:", placeholder="e.g., What is RAG used for?")

# -------------------------------
# Metadata Filter Section
# -------------------------------
st.header("🧷 Metadata Filters")

# Simulated metadata options
topics = ["RAG", "LangChain", "Transformers", "Metadata"]
sources = ["Wikipedia", "LangChain Docs", "Arxiv", "Blog", "Research Paper"]

# Dropdowns for metadata filtering
selected_topic = st.selectbox("Filter by Topic:", options=["Any"] + topics)
selected_source = st.selectbox("Filter by Source:", options=["Any"] + sources)

# Construct metadata filter dictionary
metadata_filter = {}
if selected_topic != "Any":
    metadata_filter["topic"] = selected_topic
if selected_source != "Any":
    metadata_filter["source"] = selected_source

# -------------------------------
# Submit Button
# -------------------------------
if st.button("Run RAG Pipeline"):
    # Placeholder response logic
    st.subheader("📄 RAG Response")
    if query.strip() == "":
        st.warning("Please enter a query to proceed.")
    else:
        # Simulated response output
        st.write(f"**Query:** {query}")
        st.write(f"**Metadata Filter:** {metadata_filter if metadata_filter else 'None'}")
        st.success("This is a placeholder response from the RAG pipeline.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("© 2024 RAG Demo UI – Streamlit Interface for Multi-Level Retrieval-Augmented Generation")