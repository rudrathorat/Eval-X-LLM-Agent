from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

def evaluate_prompt(prompt: str) -> str:
    try:
        # Load the locally running Ollama model
        llm = ChatOllama(model="llama3")

        # Send the prompt to the model
        response = llm.invoke([HumanMessage(content=prompt)])

        # Return the model's reply
        return response.content

    except Exception as e:
        return f"Error: {str(e)}"
