import os
os.environ["DASHSCOPE_API_KEY"] = "sk-6c57f1fdfa3f44d8bf5617d5c4586f28"

from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels

dashscope_llm = DashScope(model_name=DashScopeGenerationModels.QWEN_MAX)

responses = dashscope_llm.stream_complete("How to make cake?")
for response in responses:
    print(response.delta, end="")