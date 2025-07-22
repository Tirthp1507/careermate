import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
from career_ai import get_career_response

# Theme toggler
is_dark = True

def toggle_theme():
    global is_dark
    is_dark = not is_dark
    apply_theme()

def apply_theme():
    bg = "#1e1e1e" if is_dark else "#ffffff"
    fg = "#ffffff" if is_dark else "#000000"
    entry_bg = "#2e2e2e" if is_dark else "#f0f0f0"

    root.config(bg=bg)
    chat_window.config(bg=bg, fg=fg, insertbackground=fg)
    entry.config(bg=entry_bg, fg=fg, insertbackground=fg)
    send_button.config(bg=entry_bg, fg=fg)
    toggle_button.config(bg=entry_bg, fg=fg)
    career_btn_frame.config(bg=bg)

# Get user profile
def get_user_profile():
    name = simpledialog.askstring("User Profile", "Enter your name:")
    age = simpledialog.askstring("User Profile", "Enter your age:")
    interests = simpledialog.askstring("User Profile", "Enter your interests (comma-separated):")
    if not (name and age and interests):
        messagebox.showwarning("Incomplete", "Please fill all details.")
        root.quit()
    return name, age, interests

# Send message
def send_message(msg=None):
    user_input = entry.get() if msg is None else msg
    if not user_input.strip():
        return
    chat_window.config(state='normal')
    chat_window.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)

    try:
        response = get_career_response(user_input, *user_profile)
        chat_window.insert(tk.END, f"CareerAI: {response}\n\n")
    except Exception as e:
        chat_window.insert(tk.END, f"CareerAI: Error - {str(e)}\n\n")

    chat_window.config(state='disabled')
    chat_window.see(tk.END)

# Setup GUI
root = tk.Tk()
root.title("CareerAI Chatbot")
root.geometry("800x600")

# Profile
user_profile = get_user_profile()

# Chat Display
chat_window = scrolledtext.ScrolledText(root, width=100, height=25, state='disabled', wrap=tk.WORD)
chat_window.pack(padx=10, pady=(10, 0))

# Entry Field
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=70)
entry.pack(side=tk.LEFT, padx=10)
entry.bind("<Return>", lambda event=None: send_message())

send_button = tk.Button(entry_frame, text="Send", width=10, command=send_message)
send_button.pack(side=tk.LEFT)

# Quick Suggestion Buttons
career_btn_frame = tk.Frame(root)
career_btn_frame.pack(pady=10)

def make_button(text):
    return tk.Button(career_btn_frame, text=text, width=25, command=lambda: send_message(text))

make_button("Suggest best career based on my interests").pack(side=tk.LEFT, padx=5)
make_button("What skills should I learn in 2025?").pack(side=tk.LEFT, padx=5)
make_button("What jobs are trending in tech industry?").pack(side=tk.LEFT, padx=5)

# Theme Toggle
toggle_button = tk.Button(root, text="🌙 Toggle Theme", command=toggle_theme)
toggle_button.pack(pady=(5, 10))

apply_theme()
root.mainloop()
