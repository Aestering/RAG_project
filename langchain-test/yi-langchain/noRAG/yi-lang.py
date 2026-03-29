from langchain_openai import ChatOpenAI
api_key = "###"
llm = ChatOpenAI(openai_api_base="https://api.01.ai/v1", openai_api_key=api_key, model="yi-large")

print(llm.invoke("hi, who are you?"))
