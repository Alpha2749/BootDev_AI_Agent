import os, sys, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    ## Argument Parser
    parser = argparse.ArgumentParser(description="AI Agent Inputs")
    parser.add_argument("prompt", help="Prompt to be supplied to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Increased logging level")
    args = parser.parse_args()
    
    ## Load API Key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    ## Generate Response
    user_prompt = args.prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages
    )
    response_text = response.text
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    
    print(response_text)
    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

if __name__ == "__main__":
    main()
