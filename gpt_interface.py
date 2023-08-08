import openai

from dataclasses import dataclass, field
from typing import List, Dict, Callable

import functools
import logging

import json
import inspect


@dataclass()
class GPTConversation:
    model: str = field()
    functions: List[Callable] = field()

    messages: List[Dict] = field(init=False)
    functions_metadata: List[Dict] = field(init=False)
    function_name_mapping: Dict[str, Callable] = field(init=False)

    def __post_init__(self):
        self.messages = []
        self.functions_metadata = list(map(generate_function_metadata, self.functions))
        self.function_name_mapping = {func.__name__: func for func in self.functions}

        self.send = functools.partial(
            openai.ChatCompletion.create,
            model=self.model,
            messages=self.messages,
            functions=self.functions_metadata,
            function_call="auto"
        )

    def send_user_message(self, content):
        message = {
            "role": "user",
            "content": content,
        }
        self.messages.append(message)
        logging.debug(f"Sending message: {content}")
        response = self.send()
        logging.debug(f"Rendering response...")
        rendered_response = self.render_response(response)
        response_content= response_to_message(rendered_response)["content"]
        logging.debug(f"Received response: {response_content}")
        return response_content

    def execute_function(self, function_call):
        function_name = function_call["function_call"]["name"]
        logging.debug(f"Executing function '{function_name}'")
        function_to_call = self.function_name_mapping[function_name]
        function_args = json.loads(function_call["function_call"]["arguments"])
        function_response = function_to_call(**function_args)

        function_result = {
            "role": "function",
            "name": function_name,
            "content": function_response,
        }
        return function_result

    def render_response(self, response):
        response_message = response_to_message(response)
        self.messages.append(response_message)
        if response_message.get("function_call"):
            function_message = self.execute_function(response_message)
            self.messages.append(function_message)
            after_function_response = self.send()
            return self.render_response(after_function_response)
        return response


def response_to_message(response):
    return response["choices"][0]["message"]


def generate_function_metadata(function: Callable):
    signature = inspect.signature(function)
    parameters = signature.parameters
    param_metadata = []

    for param_name, param in parameters.items():
        param_info = {
            "name": param_name,
            "type": "string",  # Adjust as needed based on parameter type
            "description": "",  # Add description if desired
        }
        param_metadata.append(param_info)

    function_metadata = {
        "name": function.__name__,
        "description": function.__doc__.strip(),
        "parameters": {
            "type": "object",
            "properties": {param["name"]: param for param in param_metadata},
            "required": [param["name"] for param in param_metadata],
        },
    }
    return function_metadata
