import customtkinter as ctk
from deep_translator import MyMemoryTranslator

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Language Translator")
app.geometry("450x500")

heading = ctk.CTkLabel(app, text="Language Translator", font=("Arial", 16, "bold"))
heading.pack(pady=10)

input_box = ctk.CTkTextbox(app, width=380, height=100)
input_box.pack(pady=5)
input_box.insert("1.0", "Enter text to translate...")

def show_about():
    about_window=ctk.CTkToplevel(app)
    about_window.title("About")
    about_window.geometry("300x150")

    label=ctk.CTkLabel(about_window, text="Language Translator\nBuilt for Stardance Challenge\nVersion 1.0", font=("Arial", 12))
    label.pack(pady=30)

def clear_text():
    input_box.delete("1.0", "end")
    output_box.delete("1.0", "end")
    status_label.configure(text="Status: Cleared")

languages = {
    "English": "en-GB",
    "German": "de-DE",
    "French": "fr-FR",
    "Hindi": "hi-IN",
    "Spanish": "es-ES",
    "Dutch": "nl-NL"
}

lang_names = list(languages.keys())

source_label = ctk.CTkLabel(app, text="From Language:")
source_label.pack(pady=2)

source_menu = ctk.CTkOptionMenu(app, values=lang_names)
source_menu.set("Hindi")
source_menu.pack(pady=2)

target_label = ctk.CTkLabel(app, text="To Language:")
target_label.pack(pady=2)
target_menu = ctk.CTkOptionMenu(app, values=lang_names)
target_menu.set("English")
target_menu.pack(pady=2)

def translate_text():
    input_text=input_box.get("1.0", "end-1c")
    src_code=languages[source_menu.get()]
    tgt_code=languages[target_menu.get()]

    if input_text.strip():
        try:
            translated = MyMemoryTranslator(source=src_code, target=tgt_code).translate(input_text)
            output_box.delete("1.0","end")
            output_box.insert("1.0", translated)
            status_label.configure(text="Status: Translation Successful")
        except Exception as e:
            output_box.delete("1.0", "end")
            output_box.insert("1.0",f"Error: {e}")
            status_label.configure(text="Status: Translation Failed")

translate_button = ctk.CTkButton(app, text="Translate", command=translate_text)
translate_button.pack(pady=10)

clear_button = ctk.CTkButton(app, text="Clear All", command=clear_text)
clear_button.pack(pady=5)

about_button=ctk.CTkButton(app, text="About App", command=show_about)
about_button.pack(pady=5)

status_label=ctk.CTkLabel(app, text="Ready", font=("Arial",10,"italic"))
status_label.pack(pady=5)

output_box = ctk.CTkTextbox(app, width=380, height=100)
output_box.pack(pady=10)

app.mainloop()