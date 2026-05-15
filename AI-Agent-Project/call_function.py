from functions.get_files_info import get_files_info_schema, get_files_info
from functions.get_file_content import get_file_content_schema, get_file_content
from functions.run_python_file import run_python_file_schema, run_python_file
from functions.write_file import write_file_schema, write_file
import copy

#AI Agent available tooling
tool_mapping = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file
}

tools = [
    get_files_info_schema,
    get_file_content_schema,
    run_python_file_schema,
    write_file_schema
]

#Calling functions configuration
def call_function(tool_call ,verbose=False):

    #Protection against "name" value being None
    if tool_call["function"]["name"] is not None:
        function_name = tool_call["function"]["name"]
    else:
        function_name = ""
    
    #Protection against "arguments" value being None
    function_args = dict(tool_call["function"]["arguments"]) if tool_call["function"]["arguments"] else {}
    function_args["working_directory"] = "./calculator"

    #Ensuring the key exists, or return an error instead
    if function_name in tool_mapping:
        tool_response = tool_mapping[function_name](**function_args)
        result = {
            "role": "tool",
            "name": function_name,
            "content": tool_response}
    else:
        return f'"error": "Unknown function: {function_name}'
    
    #Check if verbose was used in the prompt submission
    if verbose:
        print(f'-> {result["content"]}')
    else:
        print(f" - Calling function: {function_name}")

    if result is None:
        raise Exception("The tool response was not valid as no value was returned.")
    elif "role" not in result or "name" not in result or "content" not in result:
        raise Exception("The tool response was not valid as one or more keys are not valid.")
    elif result["role"] == "" or result["name"] == "" or result["content"] == "":
        raise Exception("The tool response was not valid as one or more key values were missing.")
    else:
        return result