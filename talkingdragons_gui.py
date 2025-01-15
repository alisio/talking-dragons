import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from pathlib import Path
import whisper
import time

class TalkingDragonsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Talking Dragons - Transcription Tool")

        self.file_paths = []
        self.model = None

        # Whisper models
        self.models = ["tiny", "base", "small", "medium", "large"]

        # Whisper languages
        self.languages = [
            "", "af", "sq", "am", "ar", "hy", "as", "az", "ba", "eu", "be", "bn", "bs", "br", "bg", "ca", "zh", "zh-cn", "zh-tw", "hr", "cs", "da", "nl", "en", "et", "fa", "fi", "fr", "gl", "ka", "de", "el", "gu", "ht", "he", "hi", "hu", "is", "id", "it", "ja", "jv", "kn", "kk", "km", "ko", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "ne", "no", "ny", "oc", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sa", "sr", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu"
        ]

        # Model selection
        tk.Label(root, text="Select Whisper Model:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.model_var = tk.StringVar(value="base")
        self.model_dropdown = ttk.Combobox(root, textvariable=self.model_var, values=self.models, state="readonly")
        self.model_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        # Language selection
        tk.Label(root, text="Select Language (leave blank for auto-detect):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.language_var = tk.StringVar(value="")
        self.language_dropdown = ttk.Combobox(root, textvariable=self.language_var, values=self.languages, state="readonly")
        self.language_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        # File selection
        self.file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=10, width=50)
        self.file_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        tk.Button(root, text="Add Files", command=self.add_files).grid(row=3, column=0, padx=10, pady=5, sticky="we")
        tk.Button(root, text="Clear Files", command=self.clear_files).grid(row=3, column=1, padx=10, pady=5, sticky="we")

        # Transcribe button
        self.transcribe_button = tk.Button(root, text="Start Transcription", command=self.start_transcription)
        self.transcribe_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Progress bar
        self.progress_var = tk.IntVar()
        self.progress_bar = ttk.Progressbar(root, maximum=100, variable=self.progress_var)
        self.progress_bar.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        # Console output
        self.console = tk.Text(root, height=10, width=50, state="disabled")
        self.console.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    def add_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Audio/Video Files", "*.mp3 *.mp4 *.wav *.m4a *.flac *.aac")])
        for path in file_paths:
            if path not in self.file_paths:
                self.file_paths.append(path)
                self.file_listbox.insert(tk.END, path)

    def clear_files(self):
        self.file_paths.clear()
        self.file_listbox.delete(0, tk.END)

    def log(self, message):
        self.console.config(state="normal")
        self.console.insert(tk.END, message + "\n")
        self.console.config(state="disabled")
        self.console.see(tk.END)

    def start_transcription(self):
        if not self.file_paths:
            messagebox.showerror("Error", "No files selected for transcription.")
            return

        model_name = self.model_var.get()
        language = self.language_var.get() or None

        self.transcribe_button.config(state="disabled")
        self.progress_var.set(0)
        self.log("Starting transcription...")

        # Run transcription in a separate thread
        threading.Thread(target=self.transcribe_files, args=(model_name, language)).start()

    def transcribe_files(self, model_name, language):
        try:
            self.log(f"Loading model '{model_name}'...")
            self.model = whisper.load_model(model_name)

            total_files = len(self.file_paths)
            for i, file_path in enumerate(self.file_paths):
                self.log(f"Transcribing: {file_path}")
                start_time = time.time()

                result = self.model.transcribe(file_path, language=language)
                transcription = result['text']

                output_file = Path(file_path).parent / (Path(file_path).stem + "_transcription.txt")
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(transcription)

                duration = time.time() - start_time
                self.log(f"Saved transcription to: {output_file} ({duration:.2f}s)")

                self.progress_var.set(int((i + 1) / total_files * 100))

            self.log("Transcription complete.")
        except Exception as e:
            self.log(f"Error: {e}")
        finally:
            self.transcribe_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = TalkingDragonsApp(root)
    root.mainloop()
