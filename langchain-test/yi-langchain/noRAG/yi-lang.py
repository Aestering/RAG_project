from langchain_openai import ChatOpenAI
api_key = "dc2935e111024862885468d5cbe358af"
llm = ChatOpenAI(openai_api_base="https://api.01.ai/v1", openai_api_key=api_key, model="yi-large")

print(llm.invoke("hi, who are you?"))
