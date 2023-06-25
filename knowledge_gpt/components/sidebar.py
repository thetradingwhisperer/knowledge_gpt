import streamlit as st


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Upload a pdf, docx, or txt file📄\n"
            "2. Ask a question about the document💬\n"
        )
        api_key_input = st.text_input(
            "pass",
            type="password",
            placeholder="",
            value=st.session_state.get("OPENAI_API_KEY", ""),
        )

        if api_key_input:
            set_openai_api_key(api_key_input)

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "This app uses large language models which allows you to ask questions about your "
            "documents and get decent answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "with your feedback and suggestions💡"
        )
        st.markdown("---")
        st.markdown("Made by [Arsene Keya]")
