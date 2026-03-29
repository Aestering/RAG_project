import os
os.environ["DASHSCOPE_API_KEY"] = "###"

from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels

dashscope_llm = DashScope(model_name=DashScopeGenerationModels.QWEN_MAX)

resp = dashscope_llm.complete("How to make cake?")
print(resp)
