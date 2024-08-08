import random
from http import HTTPStatus
from dashscope import Generation
import dashscope
dashscope.api_key = "sk-258b7198c52c4abba2a2f40c4f24d41c"

def call_with_messages():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who are you?"}]
    response = Generation.call(model = "qwen-turbo",
                               messages=messages,
                               # Specify the random seed. If leave 1234 as default.
                               seed = random.randint(1, 10000),
                               # Set the output format to message.
                               result_format = "message")
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print("Request id: %s, Status code: %s, error code: %s, error message: %s" % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == "__main__":
    call_with_messages()