from llama_index.llms.mistralai import MistralAI
from llama_index.core.prompts import PromptTemplate
from llama_index.core.bridge.pydantic import BaseModel


class Restaurant(BaseModel):
    """A restaurant with name, city, and cuisine."""

    name: str
    city: str
    cuisine: str


llm = MistralAI(model="mistral-large-latest", api_key="3GyMujRYXjA3Ti37gq0vCEjQVYTu9ATk")
prompt_tmpl = PromptTemplate(
    "Generate a restaurant in a given city {city_name}"
)

# Option 1: Use `as_structured_llm`
restaurant_obj = (
    llm.as_structured_llm(Restaurant)
    .complete(prompt_tmpl.format(city_name="Miami"))
    .raw
)
# Option 2: Use `structured_predict`
# restaurant_obj = llm.structured_predict(Restaurant, prompt_tmpl, city_name="Miami")

print(restaurant_obj)