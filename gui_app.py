import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from pathlib import Path

from txt2pdf import convert_txt
from image2pdf import convert_image
from word2pdf import convert_docx

class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File to PDF Converter")

        self.file_type = tk.StringVar()
        self.input_path = ""
        self.output_path = ""

        self.build_ui()

    def build_ui(self):
        ttk.Label(self.root, text="Choose the file type").pack(pady=5)
        ttk.Combobox(self.root, textvariable=self.file_type, values=["txt", "img", "docx"]).pack()

        ttk.Button(self.root, text=" Choose the file 📂 ", command=self.select_input).pack(pady=10)
        ttk.Button(self.root, text="Where to save it ? 📄", command=self.select_output).pack(pady=10)
        ttk.Button(self.root, text=" Convert 🚀 ", command=self.convert).pack(pady=15)

    def select_input(self):
        path = filedialog.askopenfilename()
        if path:
            self.input_path = path
            messagebox.showinfo("the file hase been chosen", path)

    def select_output(self):
        path = filedialog.asksaveasfilename(defaultextension=".pdf")
        if path:
            self.output_path = path
            messagebox.showinfo("the file will be saved", path)

    def convert(self):
        file_type = self.file_type.get()

        if not file_type or not self.input_path or not self.output_path:
            messagebox.showerror("ERORR❌", "please choose the file , type and where to save it !!!")
            return

        try:
            if file_type == "txt":
                convert_txt(self.input_path, self.output_path)
            elif file_type == "img":
                convert_image(self.input_path, self.output_path)
            elif file_type == "docx":
                convert_docx(self.input_path, self.output_path)
            else:
                raise Exception("Unknown File Type")

            messagebox.showinfo("✅ SUCCESSES", "CONVERTED")
        except Exception as e:
            messagebox.showerror(" ERROR ❌", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()
