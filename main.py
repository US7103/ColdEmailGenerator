import streamlit as st
from chain import Chain
from utils import clean_text
from portfolio import Portfolio
from langchain_community.document_loaders import WebBaseLoader

# Create instances
llm = Chain()
portfolio = Portfolio()

# Call the app function
st.title('Cold Email Generator')  # optional if inside function
url_input = st.text_input(
    "Enter a URL:",
    value="https://www.amazon.jobs/en/jobs/3065229/graduate-area-shift-manager-murcia"
)
submit_button = st.button("Submit")

if submit_button:
    try:
        loader = WebBaseLoader([url_input])
        docs = loader.load()
        if not docs:
            st.error("No content found at the URL.")
        else:
            data = clean_text(docs[0].page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get("skills", [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language="markdown")
    except Exception as e:
        st.error(f"An Error occurred: {e}")

       