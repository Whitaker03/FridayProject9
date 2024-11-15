import tkinter as tk
from tkinter import scrolledtext
import openai
from dotenv import load_dotenv
import os

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion():
    """Fetch completion based on user prompt."""
    prompt = prompt_input.get("1.0", tk.END).strip()
    if not prompt:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        return
    try:
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        completion = response.choices[0].text.strip()
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, completion)
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")

# Create GUI window
root = tk.Tk()
root.title("OpenAI Prompt Completion")

# Prompt input box
tk.Label(root, text="Enter your prompt:").pack(pady=5)
prompt_input = tk.Text(root, height=5, width=50)
prompt_input.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_completion)
submit_button.pack(pady=10)

# Output display box
tk.Label(root, text="Completion Output:").pack(pady=5)
output_box = scrolledtext.ScrolledText(root, height=10, width=50, wrap=tk.WORD)
output_box.pack(pady=5)

# Run the application
root.mainloop()
