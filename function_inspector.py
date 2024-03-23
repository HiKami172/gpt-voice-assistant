import inspect
from typing import Callable
from docstring_parser import parse


def generate_function_metadata(function: Callable):
    docstring = parse(function.__doc__)
    parameters_properties = {}
    required = []

    for param in docstring.params:
        param_info = {
            "type": param.type_name,
            "description": param.description,
        }
        if not param.is_optional:
            required.append(param.arg_name)
        parameters_properties[param.arg_name] = param_info

    parameters = {
        "type": "object",
        "properties": parameters_properties,
        "required": required,
    }

    function_info = {
        "name": function.__name__,
        "description": docstring.short_description,
        "parameters": parameters
    }
    return function_info


