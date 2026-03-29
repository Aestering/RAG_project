import os
os.environ["YI_API_KEY"] = "###"

from langchain_community.chat_models.yi import ChatYi
from langchain_core.prompts import ChatPromptTemplate


# Load the model
llm = ChatYi(model="yi-large", 
             region = "international",
             temperature = 0,
             timeout = 60,
             yi_api_base = "https://api.01.ai/v1/chat/completions")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
translation = chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)
print(translation)
