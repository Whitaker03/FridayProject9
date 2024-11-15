import os
import tkinter as tk
from tkinter import scrolledtext
import openai
from dotenv import load_dotenv

# Suppress tkinter deprecation warnings
os.environ["TK_SILENCE_DEPRECATION"] = "1"

# Load environment variables
def configure():
    load_dotenv()

configure()

# Load the API key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion():
    """Fetch completion based on user input."""
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

def clear_text():
    """Clear the input and output text boxes."""
    prompt_input.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

# Create GUI window
root = tk.Tk()
root.title("OpenAI Prompt Completion")
root.geometry("600x500")  # Adjusted size for better spacing
root.resizable(False, False)

# Styling
font_label = ("Helvetica", 12)
font_text = ("Helvetica", 10)

# Prompt label and input box
prompt_label = tk.Label(root, text="Enter your prompt:", font=font_label)
prompt_label.pack(pady=(10, 5))

prompt_input = tk.Text(root, height=5, width=70, font=font_text, wrap=tk.WORD, bd=2, relief="solid")
prompt_input.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

submit_button = tk.Button(button_frame, text="Submit", command=get_completion, font=font_label, bg="lightblue", width=10)
submit_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text, font=font_label, bg="lightgray", width=10)
clear_button.grid(row=0, column=1, padx=10)

# Output label and display box
output_label = tk.Label(root, text="Completion Output:", font=font_label)
output_label.pack(pady=(10, 5))

output_box = scrolledtext.ScrolledText(root, height=15, width=70, wrap=tk.WORD, font=font_text, bd=2, relief="solid")
output_box.pack(pady=5)

# Run the application
root.mainloop()
