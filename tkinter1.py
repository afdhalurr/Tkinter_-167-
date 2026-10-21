import tkinter as tk
from tkinter import ttk

# Daftar 10 mata pelajaran
MAPEL = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika",
]
 
 
def hasil_prediksi():
    """Menampilkan prodi Teknologi Informasi apapun input yang diberikan."""
    label_hasil.config(text="Teknologi Informasi")