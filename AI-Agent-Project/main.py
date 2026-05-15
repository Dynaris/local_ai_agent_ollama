import os
import requests
import argparse

from dotenv import load_dotenv
from prompts import system_prompt
from call_function import tool_mapping, tools, call_function

load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

#debug print(OLLAMA_URL, OLLAMA_MODEL) 

if OLLAMA_URL == None or OLLAMA_MODEL == None:
    raise RuntimeError("No Ollama URL or Ollama model detected. Cannot proceed.")

messages = []

#system prompt
messages.append({"role": "system", "content": system_prompt})

def generate(prompt, messages, verbose=False, working_directory = os.getcwd()):

    #user input
    messages.append({"role": "user", "content": prompt})

    response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False,
            "tools": tools
        }
    )
    
    #Debug
    #print("RAW RESPONSE:", response.text)
    #print("PARSED:", data)

    data = response.json()

    #Debug 2
    #print("DATA:", data)

    #extract tool calls and their descriptive name + args (tool calls are function calls)
    if "tool_calls" in data["message"] and data["message"]["tool_calls"]:
        for tool_call in data["message"]["tool_calls"]:
            tool_response = call_function(tool_call, verbose)

            #add tool result to history
            messages.append(tool_response)

        response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False,
            "tools": tools
            }
        )

        #replace the first response with the second one (updated ver. after tool execution)
        data = response.json()
        reply = data["message"]["content"]

        #extract updated assistant reply
        messages.append({
            "role": "assistant", 
            "content": reply })

    else:
        
        #extract assistant reply
        reply = data["message"]["content"]

        #add assistant reply to history if tool calls don't exist
        messages.append({
            "role": "assistant", 
            "content": reply })

    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="*")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")

    args = parser.parse_args()
    user_input = " ".join(args.prompt)

    if not user_input.strip():
        parser.error("Prompt cannot be empty.")

    response = generate(user_input, messages, args.verbose)

    if args.verbose:
        print(f'User prompt:{response["message"]["content"]}')
        print(f'Prompt tokens:{response.get("prompt_eval_count")}')
        print(f'Response tokens:{response.get("eval_count")}')
    else:
        print(response["message"]["content"])

if __name__ == "__main__":
    main()