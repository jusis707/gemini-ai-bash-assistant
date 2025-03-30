#!/usr/bin/env python3
# Gemini-AI assistant for automation via bash/python. Credits: https://www.linkedin.com/in/juris-embergs-054b8326/
# Juris Embergs embergs.usa@gmail.com
import argparse
import requests
import json
import datetime

def setup_gemini():
    return "YOUR-GEMINI-API-KEY"  # Replace with your actual API key -> https://aistudio.google.com/app/apikey

def generate_response(api_key, conversation):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent"
    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': api_key
    }
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": conversation}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    result = response.json()
    return result['candidates'][0]['content']['parts'][0]['text']

def get_post_content():
    """Reads and returns the content of the ./post file."""
    try:
        with open("./post", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Warning: The file './post' was not found.")
        return ""
    except Exception as e:
        print(f"Warning: An error occurred while reading './post': {e}")
        return ""

def main():
    parser = argparse.ArgumentParser(description='Chat with Gemini AI in the terminal')
    parser.add_argument('-i', '--input', type=str, help='Input prompt for Gemini AI')
    parser.add_argument('-post', action='store_true', help='Append the content of the ./post file to the input')
    args = parser.parse_args()
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    api_key = setup_gemini()
    conversation = ""

    # Define ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

    if args.input:
        conversation = f"User: {args.input}"
        if args.post:
            post_content = get_post_content()
            conversation += f" {post_content}"
        conversation += "\n"
        try:
            response_text = generate_response(api_key, conversation)
            conversation += f"Assistant: {response_text}\n"
            print(f"\n{GREEN}AI Response:{RESET}\n")
            print(f"[{timestamp}]")
            print(response_text)
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
        except KeyError as e:
            print(f"Unexpected response format: {e}")
    else:
        print("Welcome to the Gemini AI Chat!")
        print("Type 'exit' to end the conversation.")
        print("Type 'help' for instructions.")

        while True:
            user_input = input(f"\n{RED}You: {RESET}")

            if user_input.lower() == 'exit':
                print("Ending the conversation. Goodbye!")
                break

            if user_input.lower() == 'help':
                print("Instructions:")
                print("  - Type your message and press Enter to send.")
                print("  - Type 'exit' to end the conversation.")
                print("  - Keep talking, and Gemini AI will maintain the context.")
                continue

            conversation += f"User: {user_input}\n"

            try:
                response_text = generate_response(api_key, conversation)
                conversation += f"Assistant: {response_text}\n"
                print(f"\n{GREEN}AI Response:{RESET}\n")
                print(response_text)
            except requests.exceptions.RequestException as e:
                print(f"API request failed: {e}")
            except KeyError as e:
                print(f"Unexpected response format: {e}")

if __name__ == '__main__':
    main()
