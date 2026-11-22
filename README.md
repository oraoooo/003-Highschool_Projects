# SMA Kanisius, TIK Projects

A collection of school (TIK/ICT) projects built across different assignments — static websites and Python/Tkinter desktop programs.

## Projects

### 1. School learning website (`dropdown/`)
A multi-page learning site with a shared dropdown navbar linking subject pages for **Matematika** (Aljabar, Geometri, Kalkulus), **Fisika** (Mekanika, Optik, Termodinamika), **Sejarah** (Kuno, Abad Pertengahan, Modern), and **PKN**. Built with HTML & CSS; the navbar is loaded dynamically into each page via `fetch()` (`navbar.html` + `script.js`).
- Entry point: `dropdown/index.html`

### 2. Interactive photosynthesis website (`Fotosintesis/`)
A single-page HTML site explaining the process of photosynthesis with a styled header/nav and custom inline CSS.
- Entry point: `Fotosintesis/IT3_32_foto.html`

### 3. Python projects (`learnPython/`)
Standalone Tkinter desktop programs covering different GUI widgets and small programs:
- `calculator_Rainer Evan Rusly.py` — basic calculator
- `tictactoe_Rainer Evan Rusly.py` — Tic-Tac-Toe game (with simple AI/random opponent)
- `Rainer Evan Rusly_IT3_30_Kasir Restoran.py` — restaurant cashier/POS program
- `Rainer Evan Rusly_XI-4_26_Cek Zodiak.py` — zodiac sign checker from birth date
- `IT3_Rainer Evan Rusly_XI-4_26_Form Lomba.py` — competition registration form
- `SliderSuhuRainer1/2/3.py` — temperature slider/converter (3 iterations)
- `ListBox02_IT3_Rainer Evan Rusly.py` — Listbox widget demo
- `tampilan.py` — widget showcase (Listbox, Radiobutton, Progressbar, Scale, PhotoImage)
- `sapa_Rainer Evan Rusly_messagebox.py` — greeting program using messagebox
- `intereface_it3_Rainer Evan Rusly.py` — basic Tkinter interface demo
- `gpt_prom_Rainer Evan Rusly.py` — simple report card (rapor) GUI generator

Run any script with:
```bash
python3 "learnPython/<script name>.py"
```

### 4. Vocabulary learning website (`Vocab/`)
A vocabulary-building site ("Glamorous Vocabulary") organized by reading activities — each unit (*Making Every Drop Count*, *Educating Psyche*, *Let's Go Bats*) links to a full text page and a companion vocabulary page. Built with HTML, CSS, and JS, using the same dynamic navbar pattern as the learning website.
- Entry point: `Vocab/index.html`

## Tech stack
- HTML, CSS, JavaScript (static sites, fetch-based shared navbar)
- Python 3 with Tkinter (desktop GUI programs)
