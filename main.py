"""
main.py

Boot.dev AI Agent Project

This script is the main entry point for the AI Agent project.
Make sure to activate your virtual environment before running!

Dependencies:
- google-genai==1.12.1
- python-dotenv==1.1.0
- black

Author: Pedro Morales
Date: [2025-06-19]
"""

import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def get_args():
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    return args


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        return f"Response: \n{response.text}"
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        try:
            expected_response = function_call_result.parts[0].function_response.response

        except (AttributeError, IndexError) as e:
            raise Exception(f"Fatal exception of some sort: {e}")

        if verbose:
            print(f"-> {expected_response}")
        function_responses.append(function_call_result.parts[0])
    if not function_responses:
        raise Exception("No function responses generated, exiting...")


def main():
    args = get_args()
    verbose = "--verbose" in sys.argv
    user_prompt = " ".join(args)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if verbose:
        print(f"User prompt: {user_prompt}\n")
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    client = genai.Client(api_key=api_key)
    generate_content(client, messages, verbose)


if __name__ == "__main__":
    main()
