# model.py

import pandas as pd
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3")

# This will store the most recently uploaded DataFrame
latest_df = None

def load_csv_to_memory(file_path):
    global latest_df
    latest_df = pd.read_csv(file_path)

def evaluate_prompt(question):
    global latest_df

    if latest_df is not None:
        # Convert the dataframe to a string summary (first 10 rows)
        context = latest_df.head(10).to_string()
        prompt = f"""You are a data analyst. A CSV dataset has been uploaded. Here are the first few rows:\n\n{context}\n\nNow answer this user query based on the data:\n\n{question}"""
    else:
        prompt = f"No dataset has been uploaded yet. Answer this general question:\n{question}"

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
