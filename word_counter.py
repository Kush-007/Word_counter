
import tkinter as tk
from tkinter import messagebox

# Function to count words
def count_words(text):
    words = text.strip().split()
    return len(words)

# Function triggered on button click
def on_count():
    user_input = text_box.get("1.0", tk.END)
    if not user_input.strip():
        messagebox.showerror("Input Error", "Please enter some text to count.")
        return
    result = count_words(user_input)
    result_label.config(text=f"Word Count: {result} words")

# Set up GUI window
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
header = tk.Label(root, text="Word Counter", font=("Helvetica", 16, "bold"))
header.pack(pady=10)

text_box = tk.Text(root, height=8, width=40)
text_box.pack(pady=10)

count_button = tk.Button(root, text="Count Words", command=on_count)
count_button.pack(pady=5)

result_label = tk.Label(root, text="Word Count: 0 words", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()