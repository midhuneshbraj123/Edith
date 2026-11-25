import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import MyMemoryTranslator

app = tk.Tk()
app.title("Language Translator")
app.geometry("450x520")
app.resizable(False, False)

heading = tk.Label(app, text="Language Translator", font=("Arial", 16, "bold"))
heading.pack(pady=10)

input_label = tk.Label(app, text="Enter text to translate:")
input_label.pack(anchor="w", padx=35, pady=(5, 0))

input_box = tk.Text(app, width=45, height=6)
input_box.pack(pady=5)
input_box.insert("1.0", "Enter text to translate...")

def on_input_click(event):
    if input_box.get("1.0", "end-1c") == "Enter text to translate...":
        input_box.delete("1.0", "end")

input_box.bind("<FocusIn>", on_input_click)

languages = {
    "English": "en-GB",
    "German": "de-DE",
    "French": "fr-FR",
    "Spanish": "es-ES",
    "Hindi": "hi-IN",
    "Malayalam": "ml-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Kannada": "kn-IN",
}
lang_names = list(languages.keys())

source_label = tk.Label(app, text="From Language:")
source_label.pack(anchor="w", padx=35, pady=(5, 0))

source_var = tk.StringVar(app)
source_var.set("Hindi")
source_menu = ttk.Combobox(app, textvariable=source_var, values=lang_names, state="readonly", width=42)
source_menu.pack(pady=2)

target_label = tk.Label(app, text="To Language:")
target_label.pack(anchor="w", padx=35, pady=(5, 0))

target_var = tk.StringVar(app)
target_var.set("English")
target_menu = ttk.Combobox(app, textvariable=target_var, values=lang_names, state="readonly", width=42)
target_menu.pack(pady=2)

output_label = tk.Label(app, text="Translated Output:")
output_label.pack(anchor="w", padx=35, pady=(5, 0))

output_box = tk.Text(app, width=45, height=6)
output_box.pack(pady=5)

def translate_text():
    input_text = input_box.get("1.0", "end-1c")
    src_code = languages[source_var.get()]
    tgt_code = languages[target_var.get()]

    if not input_text.strip() or input_text == "Enter text to translate...":
        status_label.config(text="Status: Please enter valid text!")
        return

    try:
        translated = MyMemoryTranslator(source=src_code, target=tgt_code).translate(input_text)
        output_box.delete("1.0", "end")
        output_box.insert("1.0", translated)
        status_label.config(text="Status: Translation Successful")
    except Exception as e:
        output_box.delete("1.0", "end")
        output_box.insert("1.0", f"Error: {e}")
        status_label.config(text="Status: Translation Failed")

def clear_text():
    input_box.delete("1.0", "end")
    input_box.insert("1.0", "Enter text to translate...")
    output_box.delete("1.0", "end")
    status_label.config(text="Status: Cleared")

def show_about():
    messagebox.showinfo("About", "Language Translator\nBuilt for Stardance Challenge\nVersion 1.0\nClassic Tkinter Version")

translate_button = tk.Button(app, text="Translate", command=translate_text, width=38)
translate_button.pack(pady=10)

clear_button = tk.Button(app, text="Clear All", command=clear_text, width=38)
clear_button.pack(pady=2)

about_button = tk.Button(app, text="About App", command=show_about, width=38)
about_button.pack(pady=2)

status_label = tk.Label(app, text="Status: Ready", font=("Arial", 9, "italic"))
status_label.pack(pady=5)

app.mainloop()