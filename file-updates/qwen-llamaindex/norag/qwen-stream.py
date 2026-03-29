import os
os.environ["DASHSCOPE_API_KEY"] = "###"

from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels

dashscope_llm = DashScope(model_name=DashScopeGenerationModels.QWEN_MAX)

responses = dashscope_llm.stream_complete("How to make cake?")
for response in responses:
    print(response.delta, end="")
