import tkinter as tk
from tkinter import ttk, messagebox


# ----------------------------
# Konfigurasi jendela aplikasi
# ----------------------------
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("560x570")
root.resizable(False, False)
root.configure(bg="#F1F5F9")

WARNA_UTAMA = "#1D4ED8"
WARNA_TEKAN = "#1E40AF"
WARNA_LATAR = "#F1F5F9"
WARNA_KARTU = "#FFFFFF"
WARNA_TEKS = "#1E293B"


# ----------------------------
# Fungsi aplikasi
# ----------------------------
def simpan_data():
    nama_value = entry_nama.get().strip()
    nim_value = entry_nim.get().strip()
    prodi_value = combo_prodi.get().strip()
    alamat_value = text_alamat.get("1.0", tk.END).strip()

    # Validasi data wajib
    if not nama_value or not nim_value:
        messagebox.showwarning(
            "Data belum lengkap",
            "Nama dan NIM wajib diisi sebelum menyimpan."
        )
        return

    if not prodi_value:
        messagebox.showwarning(
            "Program studi belum dipilih",
            "Silakan pilih program studi terlebih dahulu."
        )
        return

    if not alamat_value:
        alamat_value = "-"

    label_hasil.config(
        text=(
            f"Nama: {nama_value}\n"
            f"NIM: {nim_value}\n"
            f"Program Studi: {prodi_value}\n"
            f"Alamat: {alamat_value}"
        )
    )


def reset_form():
    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)
    combo_prodi.set("")
    text_alamat.delete("1.0", tk.END)
    label_hasil.config(text="")


def keluar_aplikasi():
    root.destroy()


# ----------------------------
# Tampilan utama menggunakan grid
# ----------------------------
root.columnconfigure(0, weight=1)

judul = tk.Label(
    root,
    text="FORMULIR IDENTITAS MAHASISWA",
    font=("Arial", 16, "bold"),
    bg=WARNA_UTAMA,
    fg="white",
    pady=18
)
judul.grid(row=0, column=0, sticky="ew")

kartu = tk.Frame(root, bg=WARNA_KARTU, padx=24, pady=20)
kartu.grid(row=1, column=0, padx=25, pady=18, sticky="ew")
kartu.columnconfigure(1, weight=1)

label_nama = tk.Label(
    kartu, text="Nama", font=("Arial", 10, "bold"),
    bg=WARNA_KARTU, fg=WARNA_TEKS
)
label_nama.grid(row=0, column=0, sticky="w", pady=8)

entry_nama = ttk.Entry(kartu, width=36)
entry_nama.grid(row=0, column=1, sticky="ew", pady=8, padx=(15, 0))

label_nim = tk.Label(
    kartu, text="NIM", font=("Arial", 10, "bold"),
    bg=WARNA_KARTU, fg=WARNA_TEKS
)
label_nim.grid(row=1, column=0, sticky="w", pady=8)

entry_nim = ttk.Entry(kartu, width=36)
entry_nim.grid(row=1, column=1, sticky="ew", pady=8, padx=(15, 0))

label_prodi = tk.Label(
    kartu, text="Program Studi", font=("Arial", 10, "bold"),
    bg=WARNA_KARTU, fg=WARNA_TEKS
)
label_prodi.grid(row=2, column=0, sticky="w", pady=8)

combo_prodi = ttk.Combobox(
    kartu,
    values=[
        "Teknik Informatika",
        "Sistem Informasi",
        "Teknologi Informasi",
    ],
    state="readonly"
)
combo_prodi.grid(row=2, column=1, sticky="ew", pady=8, padx=(15, 0))

label_alamat = tk.Label(
    kartu, text="Alamat", font=("Arial", 10, "bold"),
    bg=WARNA_KARTU, fg=WARNA_TEKS
)
label_alamat.grid(row=3, column=0, sticky="nw", pady=8)

text_alamat = tk.Text(
    kartu,
    width=30,
    height=4,
    font=("Arial", 10),
    wrap="word",
    relief="solid",
    borderwidth=1
)
text_alamat.grid(row=3, column=1, sticky="ew", pady=8, padx=(15, 0))

# Tombol aksi
frame_tombol = tk.Frame(root, bg=WARNA_LATAR)
frame_tombol.grid(row=2, column=0, pady=2)

style = ttk.Style()
style.configure(
    "Aksi.TButton",
    font=("Arial", 10, "bold"),
    padding=(14, 8)
)

ttk.Button(
    frame_tombol, text="Simpan", command=simpan_data,
    style="Aksi.TButton"
).grid(row=0, column=0, padx=6)

ttk.Button(
    frame_tombol, text="Reset", command=reset_form,
    style="Aksi.TButton"
).grid(row=0, column=1, padx=6)

ttk.Button(
    frame_tombol, text="Keluar", command=keluar_aplikasi,
    style="Aksi.TButton"
).grid(row=0, column=2, padx=6)

# Area hasil
label_judul_hasil = tk.Label(
    root,
    text="HASIL DATA MAHASISWA",
    font=("Arial", 11, "bold"),
    bg=WARNA_LATAR,
    fg=WARNA_UTAMA
)
label_judul_hasil.grid(row=3, column=0, pady=(14, 5))

label_hasil = tk.Label(
    root,
    text="Data yang disimpan akan tampil di sini.",
    font=("Arial", 10),
    bg=WARNA_KARTU,
    fg=WARNA_TEKS,
    justify="left",
    anchor="w",
    padx=16,
    pady=12,
    wraplength=470
)
label_hasil.grid(row=4, column=0, padx=25, pady=(0, 15), sticky="ew")

# Menjalankan aplikasi
entry_nama.focus()
root.mainloop()
