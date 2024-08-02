import os
os.environ["DASHSCOPE_API_KEY"] = "sk-258b7198c52c4abba2a2f40c4f24d41c"

from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels

dashscope_llm = DashScope(model_name=DashScopeGenerationModels.QWEN_MAX)

resp = dashscope_llm.complete("How to make cake?")
print(resp)