import os
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

#debug print(OLLAMA_URL, OLLAMA_MODEL) 

if OLLAMA_URL == None or OLLAMA_MODEL == None:
    raise RuntimeError("No Ollama URL or Ollama model detected. Cannot proceed.")

messages = []
messages.append({"role": "system", "content":"..."})

def generate(prompt, messages):

    #user input
    messages.append({"role": "user", "content": prompt})

    response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False
        }
    )
    
    data = response.json()

    #extract assistant reply
    reply = data["message"]["content"]

    #add assistant reply to history
    messages.append({"role": "assistant", "content": reply })

    return data

# def bootdev_api_format_converter(messages):
    # role="user", parts=[{"text": "..."}]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="*")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")

    args = parser.parse_args()
    user_input = " ".join(args.prompt)

    if not user_input.strip():
        parser.error("Prompt cannot be empty.")

    response = generate(user_input, messages)

    if args.verbose:
        print(f'User prompt:{response["message"]["content"]}')
        print(f'Prompt tokens:{response.get("prompt_eval_count")}')
        print(f'Response tokens:{response.get("eval_count")}')
    else:
        print(response["message"]["content"])

if __name__ == "__main__":
    main()