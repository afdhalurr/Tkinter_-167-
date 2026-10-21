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
     kolom = (i // 5) * 2      # 0 atau 2
    baris = i % 5
    tk.Label(
        frame_input, text=mapel, font=("Segoe UI", 10),
        bg="#f0f4f8", anchor="w", width=16,
    ).grid(row=baris, column=kolom, padx=(10, 5), pady=6, sticky="w")

  entry = ttk.Entry(frame_input, width=8, justify="center")
    entry.grid(row=baris, column=kolom + 1, padx=(0, 20), pady=6)
    entries.append(entry)s

# ---------- Button Hasil Prediksi ----------
btn_prediksi = tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Segoe UI", 12, "bold"),
    bg="#1f6feb",
    fg="white",
    activebackground="#1558b8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=6,
    command=hasil_prediksi,
)
btn_prediksi.pack(pady=(20, 10))
 
# ---------- Label luaran hasil prediksi ----------
tk.Label(
    root, text="Prodi yang diprediksi:", font=("Segoe UI", 10),
    bg="#f0f4f8", fg="#555555",
).pack()
 
label_hasil = tk.Label(
    root,
    text="-",
    font=("Segoe UI", 16, "bold"),
    bg="white",
    fg="#198754",
    width=28,
    pady=8,
    relief="groove",
)
label_hasil.pack(pady=(5, 15))
 
root.mainloop()