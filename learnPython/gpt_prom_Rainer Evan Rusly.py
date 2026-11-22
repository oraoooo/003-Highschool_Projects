# =========================================================
# Program RAPOR SEDERHANA (Versi GUI Modern)
# =========================================================
# Versi ini memoles tampilan dengan ttk (themed‑widgets) + grid layout
# agar antarmuka lebih rapi, responsif, dan "kekinian".
# Setiap baris tetap diberi komentar singkat (bahasa Indonesia)
# sehingga mudah dipelajari maupun dimodifikasi.
# =========================================================

# ---------- 1. IMPORT LIBRARY ----------
import tkinter as tk                    # Tkinter inti: fondasi GUI
from tkinter import ttk, messagebox      # ttk = widget modern; messagebox = pop‑up
from docx import Document                # python‑docx untuk buat / edit .docx
from datetime import datetime            # Mengambil tanggal & waktu saat simpan

# ---------- 2. DATA STRUKTUR PROMPT ----------
prompt_history = [                       # Daftar prompt / pertanyaan ke ChatGPT
    "Buatkan kerangka GUI Tkinter sederhana untuk input nama & 4 nilai.",
    "Tambahkan validasi agar nilai hanya boleh 0‑100.",
    "Bagaimana menghitung rata‑rata dan predikat A/B/C otomatis?",
    "Tulis fungsi penyimpanan ke .docx memakai python‑docx."
]

# ---------- 3. FUNGSI UTIL ----------

def numeric_value(entry_widget):
    """Konversi teks Entry -> int. Jika bukan angka kembalikan -1."""
    try:
        return int(entry_widget.get())
    except ValueError:
        return -1


def nilai_ke_predikat(nilai):
    """Pemetaan angka ke huruf rapor."""
    if nilai >= 85:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 55:
        return "C"
    return "D"

# ---------- 4. INISIALISASI JENDELA & GAYA ----------
root = tk.Tk()                            # Buat jendela utama
root.title("Aplikasi Rapor Siswa ✨")      # Judul di title‑bar
root.geometry("480x520")                 # Ukuran awal jendela
root.minsize(420, 480)                    # Minimal boleh dikecilkan

# Buat style ttk agar tampak lebih menarik
style = ttk.Style(root)                   # Objek style di‑bind ke root
style.theme_use("clam")                  # Gunakan tema "clam" (netral & rapi)
style.configure("Title.TLabel",           # Style kustom untuk judul
                font=("Segoe UI", 16, "bold"))
style.configure("Card.TFrame",            # Frame berwarna lembut seperti "card"
                padding=20,
                relief="ridge")
style.configure("Card.TLabel",            # Label di dalam card
                font=("Segoe UI", 10))
style.configure("Card.TButton",           # Tombol aksen di dalam card
                font=("Segoe UI", 10, "bold"))

# ---------- 5. WIDGET TITLE ----------
judul = ttk.Label(root, text="Aplikasi Rapor Siswa", style="Title.TLabel")
judul.pack(pady=(15, 5))                  # Beri jarak atas 15px, bawah 5px

# ---------- 6. FRAME FORM (CARD) ----------
form_card = ttk.Frame(root, style="Card.TFrame")
form_card.pack(fill="x", padx=30, pady=10)  # Lebar penuh (x) dengan margin kiri‑kanan 30

# Helper: membuat baris label + entry memakai grid agar sejajar rapi
row = 0                                   # Variabel penanda baris grid

def add_labeled_entry(text):
    """Buat sepasang Label & Entry dalam satu baris grid, kembalikan objek Entry."""
    global row
    lbl = ttk.Label(form_card, text=text, style="Card.TLabel")
    lbl.grid(row=row, column=0, sticky="w", pady=6)  # sticky w = align left
    ent = ttk.Entry(form_card, width=10, justify="center")
    ent.grid(row=row, column=1, sticky="e")           # sticky e = align right
    row += 1
    return ent

entry_nama = ttk.Entry(form_card, width=30)            # Entry khusus nama (lebar > nilai)
label_nama = ttk.Label(form_card, text="Nama Siswa:", style="Card.TLabel")
label_nama.grid(row=row, column=0, sticky="w", pady=6)
entry_nama.grid(row=row, column=1, sticky="e")
row += 1

# Empat mata pelajaran (menggunakan helper)
entry_mtk   = add_labeled_entry("Nilai Matematika (0‑100):")
entry_bindo = add_labeled_entry("Nilai Bahasa Indonesia:")
entry_ipa   = add_labeled_entry("Nilai IPA:")
entry_ips   = add_labeled_entry("Nilai IPS:")

# ---------- 7. LABEL RINGKASAN (TERISI OTOMATIS) ----------
summary_var = tk.StringVar(value="Rata‑rata: ‒   |   Predikat: ‒")
summary_lbl = ttk.Label(root, textvariable=summary_var, font=("Segoe UI", 11, "italic"))
summary_lbl.pack(pady=(8, 0))

# ---------- 8. AKSI FUNGSI ----------

def simpan_rapor():
    """Validasi input, tampilkan ringkasan, lalu simpan ke file Word."""
    # Ambil & bersihkan data
    nama = entry_nama.get().strip()
    mtk  = numeric_value(entry_mtk)
    bind = numeric_value(entry_bindo)
    ipa  = numeric_value(entry_ipa)
    ips  = numeric_value(entry_ips)

    # Validasi kosong / bukan angka
    if not nama or -1 in (mtk, bind, ipa, ips):
        messagebox.showwarning("Input salah", "Isi semua kolom dengan angka 0‑100!")
        return
    # Validasi rentang 0‑100
    if not all(0 <= n <= 100 for n in (mtk, bind, ipa, ips)):
        messagebox.showwarning("Range salah", "Nilai harus 0‑100.")
        return

    # Hitung rata‑rata & predikat
    rata = (mtk + bind + ipa + ips) / 4
    pred = nilai_ke_predikat(rata)

    # Tampilkan ringkasan di label bawah judul
    summary_var.set(f"Rata‑rata: {rata:.2f}   |   Predikat: {pred}")

    # Tulis ke dokumen Word
    doc = Document()
    doc.add_heading(f"Rapor Siswa – {nama}", 0)
    doc.add_paragraph(f"Tanggal dicetak: {datetime.now():%d %B %Y %H:%M}")
    doc.add_paragraph("")  # Spacer

    # Tabel rapor
    table = doc.add_table(rows=5, cols=3)
    hdr = table.rows[0].cells
    hdr[0].text, hdr[1].text, hdr[2].text = "Mata Pelajaran", "Nilai", "Predikat"

    data = [
        ("Matematika", mtk),
        ("Bahasa Indonesia", bind),
        ("IPA", ipa),
        ("IPS", ips)
    ]
    for i, (mapel, n) in enumerate(data, start=1):
        c = table.rows[i].cells
        c[0].text, c[1].text, c[2].text = mapel, str(n), nilai_ke_predikat(n)

    doc.add_paragraph("")
    doc.add_paragraph(f"Rata‑rata: {rata:.2f}")
    doc.add_paragraph(f"Predikat akhir: {pred}")

    # Simpan file Word dengan nama unik
    filename = f"Rapor_{nama}_{datetime.now():%Y%m%d_%H%M%S}.docx"
    doc.save(filename)

    messagebox.showinfo("Berhasil", f"Rapor tersimpan sebagai {filename}")
    clear_fields()  # Reset form setelah simpan


def clear_fields():
    """Kosongkan seluruh Entry setelah penyimpanan."""
    for ent in (entry_nama, entry_mtk, entry_bindo, entry_ipa, entry_ips):
        ent.delete(0, tk.END)


def simpan_prompt():
    """Simpan / update file histori prompt ke .docx."""
    doc = Document()
    doc.add_heading("Riwayat Prompt & AI", 0)
    for i, p in enumerate(prompt_history, start=1):
        doc.add_paragraph(f"{i}. {p}   |   AI: ChatGPT")
    doc.save("Riwayat_Prompt_AI.docx")
    messagebox.showinfo("Prompt Tersimpan", "Riwayat prompt berhasil diperbarui!")

# ---------- 9. FRAME TOMBOLOPS ----------
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=15)

btn_save = ttk.Button(btn_frame, text="SIMPAN RAPOR", style="Card.TButton",
                      command=simpan_rapor)
btn_save.grid(row=0, column=0, padx=10)

btn_prompt = ttk.Button(btn_frame, text="SIMPAN RIWAYAT PROMPT", style="Card.TButton",
                        command=simpan_prompt)
btn_prompt.grid(row=0, column=1, padx=10)

# ---------- 10. JALANKAN APLIKASI ----------
root.mainloop()                        # Mulai event‑loop Tkinter
