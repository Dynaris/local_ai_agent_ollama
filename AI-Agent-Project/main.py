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

def generate(prompt):
    response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="*")

    args = parser.parse_args()
    user_input = " ".join(args.prompt)

    if not user_input.strip():
        parser.error("Prompt cannot be empty.")

    response = generate(user_input)
    print(response["response"])
    print(f"Prompt tokens:{response["prompt_eval_count"]}")
    print(f"Response tokens:{response["eval_count"]}")

if __name__ == "__main__":
    main()