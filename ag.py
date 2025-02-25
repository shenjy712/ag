import sys
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the DeepSeek client
API_KEY = os.getenv("API_KEY")
API_BASE_URI = os.getenv("API_BASE_URI")
MODEL = os.getenv("MODEL")

if not API_KEY:
    print("Error: DEEPSEEK_API_KEY not found. Please set it in a .env file.")
    sys.exit(1)

client = OpenAI(
    api_key=API_KEY,
    base_url=API_BASE_URI
)

def ai_mode():
    print("Entering AI mode. Type your prompt (or 'exit' to quit):")
    while True:
        # Get user input
        prompt = input("prompt> ")

        # Check for exit condition
        if prompt.lower() in ["exit", "quit"]:
            print("Exiting AI mode.")
            break

        # Send request to DeepSeek API
        try:
            stream = client.chat.completions.create(
                model=MODEL,  # Assuming this is the intended v3 model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
            # Print the response
            print("AI OUTPUT:\n", end="", flush=True)
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="", flush=True)
            print()  # Newline after the response finishes
        except Exception as e:
            print(f"Error: {e}")

def main():
    # Check if the script is run with no arguments
    if len(sys.argv) == 1:
        ai_mode()
    else:
        print("Usage: ai (enters interactive mode)")

if __name__ == "__main__":
    main()
