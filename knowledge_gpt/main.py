import streamlit as st
from components.sidebar import sidebar
from openai.error import OpenAIError
from utils import (
    embed_docs,
    get_answer,
    parse_docx,
    parse_pdf,
    parse_txt,
    parse_csv,
    search_docs,
    text_to_docs,
    wrap_text_in_html,
)
import pandas as pd


def clear_submit():
    st.session_state["submit"] = False


st.set_page_config(page_title="KnowledgeGPT", page_icon="📖", layout="wide")
st.header("📖KnowledgeGPT")

sidebar()

uploaded_file = st.file_uploader(
    "Upload a pdf, docx, or txt file",
    type=["pdf", "docx", "txt", "csv"],
    help="Scanned documents are not supported yet!",
    on_change=clear_submit,
    accept_multiple_files = True
)

index = None
docs = None
if uploaded_file is not None:
    if len(uploaded_file) >= 1: # Must be removed for one file upload
        if uploaded_file[0].name.endswith(".pdf"): 
            docs = [parse_pdf(doc_x) for doc_x in uploaded_file if doc_x.name.endswith(".pdf")]
        elif uploaded_file[0].name.endswith(".docx"): 
            docs = [parse_docx(doc_x) for doc_x in uploaded_file if doc_x.name.endswith(".docx")]
        elif uploaded_file[0].name.endswith(".txt"): 
            docs = [parse_txt(doc_x) for doc_x in uploaded_file if doc_x.name.endswith(".txt")]
        elif uploaded_file[0].name.endswith(".csv"): 
            docs = [parse_csv(doc_x) for doc_x in uploaded_file if doc_x.name.endswith(".csv")]
        else: raise ValueError("File type not supported!")   
        
    text = text_to_docs(docs)
    try:
        with st.spinner("Indexing document... This may take a while⏳"):
            index = embed_docs(text)
        st.session_state["api_key_configured"] = True
    except OpenAIError as e:
        st.error(e._message)

# Add tabs for either generative QA or extractive QA

tab1, tab2 = st.tabs(["Generative QA", "Extractive QA"])

# Tab1 - Generative QA
with tab1:
    query = st.text_area("Ask a question about the document", on_change=clear_submit)
    with st.expander("Advanced Options"):
        show_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
        show_full_doc = st.checkbox("Show parsed contents of the document")

    if show_full_doc and doc:
        with st.expander("Document"):
            # Hack to get around st.markdown rendering LaTeX
            st.markdown(f"<p>{wrap_text_in_html(doc)}</p>", unsafe_allow_html=True)

    button = st.button("Submit")
    if button or st.session_state.get("submit"):
        if not st.session_state.get("api_key_configured"):
            st.error("Please configure your OpenAI API key!")
        elif not index:
            st.error("Please upload a document!")
        elif not query:
            st.error("Please enter a question!")
        else:
            st.session_state["submit"] = True
            # Output Columns
            answer_col, sources_col = st.columns(2)
            sources = search_docs(index, query)
            
            try:
                answer = get_answer(sources, query)

                with answer_col:
                    st.markdown("#### Answer")
                    st.markdown(answer["output_text"].split("SOURCES: ")[0])
                    

                with sources_col:
                    st.markdown("#### Sources")
                    st.markdown(answer["output_text"].split("SOURCES: ")[-1].split(", ")[0])
                    for source in sources:
                        st.markdown(source.page_content)
                        st.markdown(source.metadata["document"])
                        st.markdown("---")

            except OpenAIError as e:
                st.error(e._message)

# Extractive QA
with tab2:
    st.write("work in progress")