from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model_name="llama3-8b-8192",
    temperature=0.9)

st.header("Research tool")

company = st.selectbox(
    "Select a company to summarize policies for",
    options=['Amazon','Google','Microsoft','Apple','Meta','Tesla','Netflix','IBM','Oracle']
)

topic = st.selectbox(
    "Select a topic to summarize policies for",
    options=['privacy','security','data retention','user rights','content moderation']
) 

template = PromptTemplate( template = """please provide me the policy of {company} on the following topic: {topic}""",
    input_variables=["company", "topic"])

prompt= template.invoke({"company":company, "topic":topic})

if st.button("summarize"):
    st.write(model.invoke(prompt).content)