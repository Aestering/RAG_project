import os
os.environ["DASHSCOPE_API_KEY"] = "####"

from langchain_community.llms.tongyi import Tongyi

response = Tongyi().invoke("What NFL team won the Super Bowl in the year Justin Bieber was born?")
print(response)
