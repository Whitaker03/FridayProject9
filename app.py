import openai
from dotenv import load_dotenv
import os

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please add it to the .env file.")

# Set the API key
openai.api_key = api_key

# Function to call GPT-3 (text-davinci-003)
def generate_gpt3_completion(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to call the custom GPT-4 API
def generate_custom_gpt4_completion(prompt):
    try:
        # Create a custom OpenAI client
        client = openai.OpenAI(
            api_key=api_key
        )
        # Send prompt to the custom GPT-4 model
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4o-2024-08-06",
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Main program loop
def main():
    print("OpenAI Prompt Completion")
    print("=========================")
    print("Type 'exit' to quit.")
    while True:
        # Get user input
        prompt = input("\nEnter your prompt: ").strip()
        if prompt.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        # Choose GPT model
        model_choice = input("Choose a model (1 for GPT-3, 2 for Custom GPT-4): ").strip()

        if model_choice == "1":
            print("\nUsing GPT-3 (text-davinci-003)...")
            result = generate_gpt3_completion(prompt)
        elif model_choice == "2":
            print("\nUsing Custom GPT-4 (gpt-4o-2024-08-06)...")
            result = generate_custom_gpt4_completion(prompt)
        else:
            print("Invalid choice. Please choose 1 or 2.")
            continue

        # Display the result
        print("\nResponse:")
        print(result)

# Run the program
if __name__ == "__main__":
    main()
