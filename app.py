import openai
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
import os

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please add it to the .env file.")

# Set the API key
openai.api_key = api_key

# Function to handle the GPT-3 completion
def generate_gpt3_completion():
    prompt = input_box.get("1.0", tk.END).strip()
    if not prompt:
        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        output_box.config(state="disabled")
        return

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        completion = response.choices[0].text.strip()
    except Exception as e:
        completion = f"Error: {str(e)}"

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, completion)
    output_box.config(state="disabled")

# Function to handle the custom GPT-4 completion
def generate_custom_gpt4_completion():
    prompt = input_box.get("1.0", tk.END).strip()
    if not prompt:
        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        output_box.config(state="disabled")
        return

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
        completion = response.choices[0].message.content.strip()
    except Exception as e:
        completion = f"Error: {str(e)}"

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, completion)
    output_box.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("OpenAI Prompt GUI")
root.geometry("700x500")
root.resizable(False, False)

# Input Label and Text Box
input_label = tk.Label(root, text="Enter your prompt:", font=("Helvetica", 12))
input_label.pack(pady=10)

input_box = tk.Text(root, height=10, width=80, font=("Helvetica", 10), wrap=tk.WORD, bd=2, relief="solid")
input_box.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# GPT-3 Button
gpt3_button = tk.Button(button_frame, text="Submit (GPT-3)", font=("Helvetica", 10), bg="lightblue", command=generate_gpt3_completion)
gpt3_button.grid(row=0, column=0, padx=10)

# Custom GPT-4 Button
gpt4_button = tk.Button(button_frame, text="Submit (Custom GPT-4)", font=("Helvetica", 10), bg="lightgreen", command=generate_custom_gpt4_completion)
gpt4_button.grid(row=0, column=1, padx=10)

# Output Label and Scrolled Text Box
output_label = tk.Label(root, text="Output:", font=("Helvetica", 12))
output_label.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, height=15, width=80, font=("Helvetica", 10), wrap=tk.WORD, state="disabled", bd=2, relief="solid")
output_box.pack(pady=5)

# Run the application
root.mainloop()
