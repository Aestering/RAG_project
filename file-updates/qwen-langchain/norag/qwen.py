import os
os.environ["DASHSCOPE_API_KEY"] = "sk-6c57f1fdfa3f44d8bf5617d5c4586f28"

from langchain_community.llms.tongyi import Tongyi

response = Tongyi().invoke("What NFL team won the Super Bowl in the year Justin Bieber was born?")
print(response)