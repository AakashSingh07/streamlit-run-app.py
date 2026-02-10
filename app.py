import streamlit as st
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

st.set_page_config(page_title="AI Text Summarizer", page_icon="⚡")

st.title("⚡ AI Text Summarizer")
st.write("Paste long text and get a short summary instantly!")

text = st.text_area("Enter your text:", height=250)

if st.button("Generate Summary"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()

        summary = summarizer(parser.document, 3)  # 3 lines summary

        st.success("Here is your summary:")
        
        for sentence in summary:
            st.success(sentence)


# TO RUN THE PROJECT COPY AND PASTE
#  FIRST STEP ;-             source venv/bin/activate

#  SECOND STEP ;-              streamlit run app.py



