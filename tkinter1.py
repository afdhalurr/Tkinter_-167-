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
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Segoe UI", 18, "bold"),
    bg="#f0f4f8",
    fg="#1f3a5f",
    )
label_judul.pack(pady=(20, 5))

tk.Label(
    root,
    text="Masukkan nilai mata pelajaran (0 - 100)",
    font=("Segoe UI", 10),
    bg="#f0f4f8",
    fg="#555555",
).pack(pady=(0, 10))

# ---------- Frame input nilai (10 input, 2 kolom x 5 baris) ----------
frame_input = tk.Frame(root, bg="#f0f4f8")
frame_input.pack(pady=5)

entries = []
for i, mapel in enumerate(MAPEL):