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


def main ():
    if len(sys.argv) >= 3:
        print("Error: too many arguments")
        exit(1)
    elif len(sys.argv) <= 1:
        print("Error: please provide one valid argument")
        exit(1)
    else:
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=sys.argv[1],
        )
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()