import os
os.environ["YI_API_KEY"] = "dc2935e111024862885468d5cbe358af"

from langchain_community.llms.yi import YiLLM

# Load the model
llm = YiLLM(model="yi-large", region = "international")

# basic usage
res = llm.generate(
    prompts=[
        "Explain the concept of large language models.",
        "What are the potential applications of AI in healthcare?",
    ]
)
print(res)