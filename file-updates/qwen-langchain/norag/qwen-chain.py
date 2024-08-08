import os
os.environ["DASHSCOPE_API_KEY"] = "sk-6c57f1fdfa3f44d8bf5617d5c4586f28"

from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

llm = Tongyi()

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

chain = prompt | llm

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

answer = chain.invoke({"question": question})

print(answer)