import tkinter as tk
from tkinter import ttk

# Daftar 10 mata pelajaran
MAPEL = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika",
]
 
 
def hasil_prediksi():
    """Menampilkan prodi Teknologi Informasi apapun input yang diberikan."""


# ---------- Jendela utama ----------
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("520x470")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# ---------- Label judul ----------
label_judul = tk.Label(