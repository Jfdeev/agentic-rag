from langsmith import Client
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

hub = Client()
llm = ChatOllama(model="qwen3.5:4b", temperature=0)
prompt = hub.pull_prompt("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()