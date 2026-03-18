from tkinter import *
from tkinter import messagebox
import re
import os
import tempfile
import datetime
from complex_electrical_calc import *

# ── Color palette ─────────────────────────────────────────────────────────────
BG        = "#1b1f3a"   # main window background
PANEL     = "#252a4a"   # panel / frame background
SUBPANEL  = "#1e2240"   # sub-section inside a frame
INPUT_BG  = "#2d3250"   # entry background (editable)
RESULT_BG = "#151929"   # entry background (read-only results)
BORDER    = "#3d4470"   # relief / separators
TXT       = "#e8eaf6"   # default text
TXT_DIM   = "#9fa8da"   # secondary / label text
DELTA_C   = "#ff7043"   # orange  – delta side accent
WYE_C     = "#ce93d8"   # lavender – wye side accent
TITLE_C   = "#ffd54f"   # gold title
HINT_C    = "#80cbc4"   # teal hint text in solution
OK_C      = "#a5d6a7"   # ok / result text
SEP_C     = "#37415e"   # separator line colour

FONT_TITLE = ("Segoe UI", 15, "bold")
FONT_HEAD  = ("Segoe UI", 10, "bold")
FONT_BODY  = ("Segoe UI", 10)
FONT_MONO  = ("Consolas", 10)
FONT_SMALL = ("Segoe UI", 8)

# ── Input-validation regex  (accepts: a+jb | a-jb | -a+jb | -a-jb) ──────────
# real and imaginary parts may be integers or decimals, spaces around +/- ignored
_RECT_RE = re.compile(
    r"^\s*-?\d+(\.\d+)?\s*[+-]\s*j\d+(\.\d+)?\s*$",
    re.IGNORECASE
)


def _normalise(value: str) -> str:
    """Remove interior spaces so '3 + j4' becomes '3+j4' before passing to parser."""
    return re.sub(r"\s+", "", value)


def _validate(value: str, label: str) -> bool:
    """Return True when value matches rectangular form a+/-jb, else show an error dialog."""
    if not _RECT_RE.match(value):
        messagebox.showerror(
            "Invalid Input \u2013 Rectangular Form Required",
            f"  Field : {label}\n"
            f"  Got   : \"{value}\"\n\n"
            "Input must be in the form  a\u00b1jb\n"
            "where a and b are real numbers.\n\n"
            "Valid examples:\n"
            "  3+j4      10-j6      -2+j5\n"
            "  5.5+j2.3     0+j8     7+j0"
        )
        return False
    return True


# ── Shared state for intermediate rectangular results ─────────────────────────
zaa = zbb = zcc = None           # Delta-side wye result Entry refs
zaa_wye = zbb_wye = zcc_wye = None   # Wye-side delta result Entry refs


# ── Solution box helpers ──────────────────────────────────────────────────────
def _sol_write(text: str):
    """Replace entire solution box content (used only for the welcome message)."""
    sol_text.config(state=NORMAL)
    sol_text.delete(1.0, END)
    sol_text.insert(1.0, text)
    sol_text.config(state=DISABLED)


def _sol_append(text: str):
    """Append a new block to the solution box and scroll to the end."""
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    separator = f"\n{'='*60}  [{ts}]\n"
    sol_text.config(state=NORMAL)
    sol_text.insert(END, separator + text + "\n")
    sol_text.config(state=DISABLED)
    sol_text.see(END)


def _sol_clear():
    """Clear the entire solution box."""
    sol_text.config(state=NORMAL)
    sol_text.delete(1.0, END)
    sol_text.config(state=DISABLED)


def _sol_print():
    """Write the solution box contents to a temp file and send to printer."""
    content = sol_text.get(1.0, END).strip()
    if not content:
        messagebox.showinfo("Nothing to Print", "The solution box is empty.")
        return
    header = (
        "DELTA <-> WYE CONVERTER  -  by Engr. APF\n"
        + "-" * 60 + "\n"
        + f"Printed: {datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}\n"
        + "=" * 60 + "\n\n"
    )
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as f:
        f.write(header + content + "\n")
        tmp_path = f.name
    try:
        os.startfile(tmp_path, "print")
    except Exception as e:
        messagebox.showerror("Print Error", str(e))


def _sol_copy():
    """Copy the entire solution box content to the clipboard."""
    content = sol_text.get(1.0, END).strip()
    if not content:
        messagebox.showinfo("Nothing to Copy", "The solution box is empty.")
        return
    window.clipboard_clear()
    window.clipboard_append(content)
    window.update()


def _sol_saveas():
    """Save the solution box content to a user-chosen .txt file."""
    from tkinter import filedialog
    content = sol_text.get(1.0, END).strip()
    if not content:
        messagebox.showinfo("Nothing to Save", "The solution box is empty.")
        return
    header = (
        "DELTA <-> WYE CONVERTER  -  by Engr. APF\n"
        + "-" * 60 + "\n"
        + f"Saved: {datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}\n"
        + "=" * 60 + "\n\n"
    )
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save Solution As"
    )
    if not path:
        return
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(header + content + "\n")
        messagebox.showinfo("Saved", f"Solution saved to:\n{path}")
    except Exception as e:
        messagebox.showerror("Save Error", str(e))


def _entry_set(entry, value, readonly=True):
    """Safely set an Entry widget value."""
    entry.config(state=NORMAL)
    entry.delete(0, END)
    entry.insert(0, value)
    if readonly:
        entry.config(state="readonly")


# =============================================================================
#  DELTA -> WYE
# =============================================================================
def convert():
    """Compute Wye equivalents from Delta inputs (rectangular form)."""
    global zaa, zbb, zcc

    raw_ab = zab.get().strip()
    raw_bc = zbc.get().strip()
    raw_ca = zca.get().strip()

    if not _validate(raw_ab, "Zab"): return
    if not _validate(raw_bc, "Zbc"): return
    if not _validate(raw_ca, "Zca"): return

    v0 = _normalise(raw_ab)
    v1 = _normalise(raw_bc)
    v2 = _normalise(raw_ca)

    # Formula (unchanged):
    #   Za = (Zab x Zca) / (Zab + Zbc + Zca)
    #   Zb = (Zab x Zbc) / (Zab + Zbc + Zca)
    #   Zc = (Zbc x Zca) / (Zab + Zbc + Zca)
    denom = add_rr(add_rr(v0, v1), v2)
    za = div_pr(convert_rtp(multi_rr(v0, v2)), denom)
    zb = div_pr(convert_rtp(multi_rr(v0, v1)), denom)
    zc = div_pr(convert_rtp(multi_rr(v1, v2)), denom)

    _entry_set(dw_za_rect, za)
    _entry_set(dw_zb_rect, zb)
    _entry_set(dw_zc_rect, zc)
    zaa, zbb, zcc = dw_za_rect, dw_zb_rect, dw_zc_rect

    # clear stale polar results
    for w in (dw_za_polar, dw_zb_polar, dw_zc_polar):
        _entry_set(w, "", readonly=False)
        w.config(state="readonly")

    sol = (
        "--- DELTA -> WYE  (Rectangular Results) ---\n"
        "Formula:\n"
        "  Za = (Zab x Zca) / (Zab + Zbc + Zca)\n"
        "  Zb = (Zab x Zbc) / (Zab + Zbc + Zca)\n"
        "  Zc = (Zbc x Zca) / (Zab + Zbc + Zca)\n\n"
        f"  Inputs ->  Zab = {v0}   Zbc = {v1}   Zca = {v2}\n\n"
        f"  Za  =  {za}\n"
        f"  Zb  =  {zb}\n"
        f"  Zc  =  {zc}\n"
    )
    _sol_append(sol)
    print(sol)


def convert_ab():
    """Convert Delta->Wye rectangular results to polar form."""
    if zaa is None:
        messagebox.showwarning("No Data", "Compute the Delta->Wye result first.")
        return

    pp1 = convert_rtp(zaa.get())
    pp2 = convert_rtp(zbb.get())
    pp3 = convert_rtp(zcc.get())

    _entry_set(dw_za_polar, pp1)
    _entry_set(dw_zb_polar, pp2)
    _entry_set(dw_zc_polar, pp3)

    sol = (
        "--- DELTA -> WYE  (Polar Results) ---\n"
        f"  Za  =  {pp1}\n"
        f"  Zb  =  {pp2}\n"
        f"  Zc  =  {pp3}\n"
    )
    _sol_append(sol)
    print(sol)


# =============================================================================
#  WYE -> DELTA
# =============================================================================
def convert1():
    """Compute Delta equivalents from Wye inputs (rectangular form)."""
    global zaa_wye, zbb_wye, zcc_wye

    raw_a = za_wye.get().strip()
    raw_b = zb_wye.get().strip()
    raw_c = zc_wye.get().strip()

    if not _validate(raw_a, "Za"): return
    if not _validate(raw_b, "Zb"): return
    if not _validate(raw_c, "Zc"): return

    v0 = _normalise(raw_a)
    v1 = _normalise(raw_b)
    v2 = _normalise(raw_c)

    # Formula (unchanged):
    #   Zab = ((Za*Zb) + (Za*Zc) + (Zb*Zc)) / Zc
    #   Zbc = ((Za*Zb) + (Za*Zc) + (Zb*Zc)) / Za
    #   Zca = ((Za*Zb) + (Za*Zc) + (Zb*Zc)) / Zb
    numer = add_rr(add_rr(multi_rr(v0, v1), multi_rr(v0, v2)), multi_rr(v1, v2))
    zab_r = div_rr(numer, v2)
    zbc_r = div_rr(numer, v0)
    zca_r = div_rr(numer, v1)

    _entry_set(wd_zab_rect, zab_r)
    _entry_set(wd_zbc_rect, zbc_r)
    _entry_set(wd_zca_rect, zca_r)
    zaa_wye, zbb_wye, zcc_wye = wd_zab_rect, wd_zbc_rect, wd_zca_rect

    for w in (wd_zab_polar, wd_zbc_polar, wd_zca_polar):
        _entry_set(w, "", readonly=False)
        w.config(state="readonly")

    sol = (
        "--- WYE -> DELTA  (Rectangular Results) ---\n"
        "Formula:\n"
        "  Zab = ((Za*Zb) + (Za*Zc) + (Zb*Zc)) / Zc\n"
        "  Zbc = ((Za*Zb) + (Za*Zc) + (Zb*Zc)) / Za\n"
        "  Zca = ((Za*Zb) + (Za*Zc) + (Zb*Zc)) / Zb\n\n"
        f"  Inputs ->  Za = {v0}   Zb = {v1}   Zc = {v2}\n\n"
        f"  Zab  =  {zab_r}\n"
        f"  Zbc  =  {zbc_r}\n"
        f"  Zca  =  {zca_r}\n"
    )
    _sol_append(sol)
    print(sol)


def convert_ba():
    """Convert Wye->Delta rectangular results to polar form."""
    if zaa_wye is None:
        messagebox.showwarning("No Data", "Compute the Wye->Delta result first.")
        return

    pp1 = convert_rtp(zaa_wye.get())
    pp2 = convert_rtp(zbb_wye.get())
    pp3 = convert_rtp(zcc_wye.get())

    _entry_set(wd_zab_polar, pp1)
    _entry_set(wd_zbc_polar, pp2)
    _entry_set(wd_zca_polar, pp3)

    sol = (
        "--- WYE -> DELTA  (Polar Results) ---\n"
        f"  Zab  =  {pp1}\n"
        f"  Zbc  =  {pp2}\n"
        f"  Zca  =  {pp3}\n"
    )
    _sol_append(sol)
    print(sol)


# =============================================================================
#  CLEAR helpers
# =============================================================================
def _clear_delta():
    for w in (zab, zbc, zca):
        w.delete(0, END)
    for w in (dw_za_rect, dw_zb_rect, dw_zc_rect,
              dw_za_polar, dw_zb_polar, dw_zc_polar):
        w.config(state=NORMAL)
        w.delete(0, END)
        w.config(state="readonly")


def _clear_wye():
    for w in (za_wye, zb_wye, zc_wye):
        w.delete(0, END)
    for w in (wd_zab_rect, wd_zbc_rect, wd_zca_rect,
              wd_zab_polar, wd_zbc_polar, wd_zca_polar):
        w.config(state=NORMAL)
        w.delete(0, END)
        w.config(state="readonly")


# =============================================================================
#  WINDOW SETUP
# =============================================================================
window = Tk()
try:
    window.iconbitmap('IIEE2.ico')
except Exception:
    pass
window.title("DELTA <-> WYE CONVERTER  by Engr. APF")
window.geometry("1300x940")
window.minsize(1200, 860)
window.config(bg=BG)

# ── Title bar ─────────────────────────────────────────────────────────────────
title_frame = Frame(window, bg=SUBPANEL, pady=8)
title_frame.grid(row=0, column=0, columnspan=3, sticky="ew", padx=6, pady=(6, 4))
Label(
    title_frame,
    text="DELTA  \u21d4  WYE  CONVERTER",
    font=FONT_TITLE, fg=TITLE_C, bg=SUBPANEL
).pack()
Label(
    title_frame,
    text="Enter impedances in rectangular form  a \u00b1 jb   (e.g. 3+j4  or  10-j6)",
    font=FONT_SMALL, fg=TXT_DIM, bg=SUBPANEL
).pack()

window.columnconfigure(0, weight=1, minsize=340)
window.columnconfigure(1, weight=0)        # canvas column – fixed
window.columnconfigure(2, weight=1, minsize=340)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=0)


# =============================================================================
#  LEFT PANEL  –  DELTA -> WYE
# =============================================================================
lf_delta = LabelFrame(
    window,
    text="  \u0394  DELTA \u2192 WYE  ",
    font=FONT_HEAD, fg=DELTA_C, bg=PANEL,
    bd=2, relief=RIDGE, padx=12, pady=10
)
lf_delta.grid(row=1, column=0, sticky="nsew", padx=(6, 3), pady=4)
lf_delta.columnconfigure(1, weight=1)

# -- section header
Label(lf_delta, text="Delta Impedances (a\u00b1jb)",
      font=FONT_HEAD, fg=DELTA_C, bg=PANEL
      ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 6))

# -- input labels
for r, lbl in enumerate(["Zab", "Zbc", "Zca"], start=1):
    Label(lf_delta, text=lbl, font=FONT_BODY, fg=TXT_DIM, bg=PANEL,
          width=5, anchor="e").grid(row=r, column=0, sticky="e", pady=3)

# -- input entries
zab = Entry(lf_delta, font=FONT_MONO, bg=INPUT_BG, fg=TXT,
            insertbackground=TXT, relief=FLAT,
            highlightthickness=1, highlightbackground=BORDER, highlightcolor=DELTA_C)
zab.grid(row=1, column=1, sticky="ew", pady=3, ipady=4)
zab.insert(0, "3+j4")

zbc = Entry(lf_delta, font=FONT_MONO, bg=INPUT_BG, fg=TXT,
            insertbackground=TXT, relief=FLAT,
            highlightthickness=1, highlightbackground=BORDER, highlightcolor=DELTA_C)
zbc.grid(row=2, column=1, sticky="ew", pady=3, ipady=4)
zbc.insert(0, "5-j2")

zca = Entry(lf_delta, font=FONT_MONO, bg=INPUT_BG, fg=TXT,
            insertbackground=TXT, relief=FLAT,
            highlightthickness=1, highlightbackground=BORDER, highlightcolor=DELTA_C)
zca.grid(row=3, column=1, sticky="ew", pady=3, ipady=4)
zca.insert(0, "6+j1")

# -- buttons row
btn_row_d = Frame(lf_delta, bg=PANEL)
btn_row_d.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 4))
Button(btn_row_d, text="  COMPUTE", font=FONT_HEAD,
       bg=DELTA_C, fg="#111", activebackground="#e64a19",
       relief=FLAT, padx=12, pady=5, cursor="hand2",
       command=convert).pack(side=LEFT, padx=(0, 8))
Button(btn_row_d, text="Clear", font=FONT_SMALL,
       bg=BORDER, fg=TXT_DIM, activebackground=SEP_C,
       relief=FLAT, padx=8, pady=5, cursor="hand2",
       command=_clear_delta).pack(side=LEFT)

# -- separator
Frame(lf_delta, bg=SEP_C, height=1).grid(row=5, column=0, columnspan=2,
                                           sticky="ew", pady=8)

# -- result header (rectangular)
Label(lf_delta, text="Wye Equivalent  (a\u00b1jb)",
      font=FONT_HEAD, fg=OK_C, bg=PANEL
      ).grid(row=6, column=0, columnspan=2, sticky="w", pady=(0, 4))

for r, lbl in enumerate(["Za", "Zb", "Zc"], start=7):
    Label(lf_delta, text=lbl, font=FONT_BODY, fg=TXT_DIM, bg=PANEL,
          width=5, anchor="e").grid(row=r, column=0, sticky="e", pady=3)

dw_za_rect = Entry(lf_delta, font=FONT_MONO, bg=RESULT_BG, fg=OK_C,
                    relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                    state="readonly", readonlybackground=RESULT_BG)
dw_za_rect.grid(row=7, column=1, sticky="ew", pady=3, ipady=4)

dw_zb_rect = Entry(lf_delta, font=FONT_MONO, bg=RESULT_BG, fg=OK_C,
                    relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                    state="readonly", readonlybackground=RESULT_BG)
dw_zb_rect.grid(row=8, column=1, sticky="ew", pady=3, ipady=4)

dw_zc_rect = Entry(lf_delta, font=FONT_MONO, bg=RESULT_BG, fg=OK_C,
                    relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                    state="readonly", readonlybackground=RESULT_BG)
dw_zc_rect.grid(row=9, column=1, sticky="ew", pady=3, ipady=4)

# -- convert-to-polar button
Button(lf_delta, text="  Convert to  a\u2220\u03b8",
       font=FONT_BODY, bg="#37474f", fg=TITLE_C, activebackground="#455a64",
       relief=FLAT, padx=10, pady=4, cursor="hand2",
       command=convert_ab
       ).grid(row=10, column=0, columnspan=2, sticky="w", pady=(6, 4))

# -- result header (polar)
Label(lf_delta, text="Wye Equivalent  (a\u2220\u03b8)",
      font=FONT_HEAD, fg=TITLE_C, bg=PANEL
      ).grid(row=11, column=0, columnspan=2, sticky="w", pady=(0, 4))

for r, lbl in enumerate(["Za", "Zb", "Zc"], start=12):
    Label(lf_delta, text=lbl, font=FONT_BODY, fg=TXT_DIM, bg=PANEL,
          width=5, anchor="e").grid(row=r, column=0, sticky="e", pady=3)

dw_za_polar = Entry(lf_delta, font=FONT_MONO, bg=RESULT_BG, fg=TITLE_C,
                     relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                     state="readonly", readonlybackground=RESULT_BG)
dw_za_polar.grid(row=12, column=1, sticky="ew", pady=3, ipady=4)

dw_zb_polar = Entry(lf_delta, font=FONT_MONO, bg=RESULT_BG, fg=TITLE_C,
                     relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                     state="readonly", readonlybackground=RESULT_BG)
dw_zb_polar.grid(row=13, column=1, sticky="ew", pady=3, ipady=4)

dw_zc_polar = Entry(lf_delta, font=FONT_MONO, bg=RESULT_BG, fg=TITLE_C,
                     relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                     state="readonly", readonlybackground=RESULT_BG)
dw_zc_polar.grid(row=14, column=1, sticky="ew", pady=3, ipady=4)


# =============================================================================
#  CENTER  –  Circuit Diagram Canvas
# =============================================================================
canvas_frame = Frame(window, bg=BG)
canvas_frame.grid(row=1, column=1, sticky="ns", padx=4, pady=4)

Label(canvas_frame, text="Circuit Diagram",
      font=FONT_SMALL, fg=TXT_DIM, bg=BG).pack(pady=(0, 2))

canvas = Canvas(canvas_frame, height=620, width=550,
                bg="#0d1117", highlightthickness=2, highlightbackground=BORDER)
canvas.pack()

# All x-coordinates are shifted +35 from the original 0-480 layout
# so the triangle corners and bus labels have clear margins on both sides.
# delta triangle (outer shape)
pts_tri = [35, 500, 275, 60, 515, 500]
# delta impedance rectangles
pts_bc  = [230, 488, 320, 488, 320, 512, 230, 512]
pts_ca  = [182, 248, 163, 237, 118, 315, 137, 326]
pts_ab  = [368, 248, 387, 237, 432, 315, 413, 326]
# wye impedance rectangles
pts_a   = [264, 255, 264, 164, 286, 164, 286, 255]
pts_b   = [355, 413, 366, 394, 445, 439, 434, 458]
pts_c   = [105, 439, 184, 394, 195, 413, 116, 458]

canvas.create_polygon(pts_tri, fill="#1a2a1a", outline="#ff7043", width=3)
# wye neutral lines
canvas.create_line(275, 60,  275, 350, fill="#42a5f5", width=3)
canvas.create_line(275, 350, 515, 500, fill="#42a5f5", width=3)
canvas.create_line(275, 350,  35, 500, fill="#42a5f5", width=3)

# delta impedance blocks
canvas.create_polygon(pts_bc, fill="#ff7043", outline="#fff", width=2)
canvas.create_text(275, 524, fill="#ffd54f",
                   font=("Consolas", 10, "bold"), text="Zbc")

canvas.create_polygon(pts_ca, fill="#ff7043", outline="#fff", width=2)
canvas.create_text(143, 280, fill="#ffd54f",
                   font=("Consolas", 10, "bold"), text="Zca")

canvas.create_polygon(pts_ab, fill="#ff7043", outline="#fff", width=2)
canvas.create_text(407, 280, fill="#ffd54f",
                   font=("Consolas", 10, "bold"), text="Zab")

# wye impedance blocks
canvas.create_polygon(pts_a, fill="#42a5f5", outline="#fff", width=2)
canvas.create_text(275, 209, fill="#e8eaf6",
                   font=("Consolas", 10, "bold"), text="Za")

canvas.create_polygon(pts_b, fill="#42a5f5", outline="#fff", width=2)
canvas.create_text(400, 426, fill="#e8eaf6",
                   font=("Consolas", 10, "bold"), text="Zb")

canvas.create_polygon(pts_c, fill="#42a5f5", outline="#fff", width=2)
canvas.create_text(150, 426, fill="#e8eaf6",
                   font=("Consolas", 10, "bold"), text="Zc")

# bus labels  (y=560 gives 60 px below triangle base for clear visibility)
canvas.create_text(275, 40,  fill="#ffd54f",
                   font=("Segoe UI", 9, "bold"), text="Bus A")
canvas.create_text(55,  560, fill="#ffd54f",
                   font=("Segoe UI", 9, "bold"), text="Bus B")
canvas.create_text(495, 560, fill="#ffd54f",
                   font=("Segoe UI", 9, "bold"), text="Bus C")


# =============================================================================
#  RIGHT PANEL  –  WYE -> DELTA
# =============================================================================
lf_wye = LabelFrame(
    window,
    text="  Y  WYE \u2192 DELTA  ",
    font=FONT_HEAD, fg=WYE_C, bg=PANEL,
    bd=2, relief=RIDGE, padx=12, pady=10
)
lf_wye.grid(row=1, column=2, sticky="nsew", padx=(3, 6), pady=4)
lf_wye.columnconfigure(1, weight=1)

# -- section header
Label(lf_wye, text="Wye Impedances (a\u00b1jb)",
      font=FONT_HEAD, fg=WYE_C, bg=PANEL
      ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 6))

for r, lbl in enumerate(["Za", "Zb", "Zc"], start=1):
    Label(lf_wye, text=lbl, font=FONT_BODY, fg=TXT_DIM, bg=PANEL,
          width=5, anchor="e").grid(row=r, column=0, sticky="e", pady=3)

za_wye = Entry(lf_wye, font=FONT_MONO, bg=INPUT_BG, fg=TXT,
               insertbackground=TXT, relief=FLAT,
               highlightthickness=1, highlightbackground=BORDER, highlightcolor=WYE_C)
za_wye.grid(row=1, column=1, sticky="ew", pady=3, ipady=4)
za_wye.insert(0, "1+j1")

zb_wye = Entry(lf_wye, font=FONT_MONO, bg=INPUT_BG, fg=TXT,
               insertbackground=TXT, relief=FLAT,
               highlightthickness=1, highlightbackground=BORDER, highlightcolor=WYE_C)
zb_wye.grid(row=2, column=1, sticky="ew", pady=3, ipady=4)
zb_wye.insert(0, "2+j0")

zc_wye = Entry(lf_wye, font=FONT_MONO, bg=INPUT_BG, fg=TXT,
               insertbackground=TXT, relief=FLAT,
               highlightthickness=1, highlightbackground=BORDER, highlightcolor=WYE_C)
zc_wye.grid(row=3, column=1, sticky="ew", pady=3, ipady=4)
zc_wye.insert(0, "3+j2")

# -- buttons row
btn_row_w = Frame(lf_wye, bg=PANEL)
btn_row_w.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 4))
Button(btn_row_w, text="  COMPUTE", font=FONT_HEAD,
       bg=WYE_C, fg="#111", activebackground="#8e24aa",
       relief=FLAT, padx=12, pady=5, cursor="hand2",
       command=convert1).pack(side=LEFT, padx=(0, 8))
Button(btn_row_w, text="Clear", font=FONT_SMALL,
       bg=BORDER, fg=TXT_DIM, activebackground=SEP_C,
       relief=FLAT, padx=8, pady=5, cursor="hand2",
       command=_clear_wye).pack(side=LEFT)

# -- separator
Frame(lf_wye, bg=SEP_C, height=1).grid(row=5, column=0, columnspan=2,
                                         sticky="ew", pady=8)

# -- result header (rectangular)
Label(lf_wye, text="Delta Equivalent  (a\u00b1jb)",
      font=FONT_HEAD, fg=OK_C, bg=PANEL
      ).grid(row=6, column=0, columnspan=2, sticky="w", pady=(0, 4))

for r, lbl in enumerate(["Zab", "Zbc", "Zca"], start=7):
    Label(lf_wye, text=lbl, font=FONT_BODY, fg=TXT_DIM, bg=PANEL,
          width=5, anchor="e").grid(row=r, column=0, sticky="e", pady=3)

wd_zab_rect = Entry(lf_wye, font=FONT_MONO, bg=RESULT_BG, fg=OK_C,
                     relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                     state="readonly", readonlybackground=RESULT_BG)
wd_zab_rect.grid(row=7, column=1, sticky="ew", pady=3, ipady=4)

wd_zbc_rect = Entry(lf_wye, font=FONT_MONO, bg=RESULT_BG, fg=OK_C,
                     relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                     state="readonly", readonlybackground=RESULT_BG)
wd_zbc_rect.grid(row=8, column=1, sticky="ew", pady=3, ipady=4)

wd_zca_rect = Entry(lf_wye, font=FONT_MONO, bg=RESULT_BG, fg=OK_C,
                     relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                     state="readonly", readonlybackground=RESULT_BG)
wd_zca_rect.grid(row=9, column=1, sticky="ew", pady=3, ipady=4)

# -- convert-to-polar button
Button(lf_wye, text="  Convert to  a\u2220\u03b8",
       font=FONT_BODY, bg="#37474f", fg=TITLE_C, activebackground="#455a64",
       relief=FLAT, padx=10, pady=4, cursor="hand2",
       command=convert_ba
       ).grid(row=10, column=0, columnspan=2, sticky="w", pady=(6, 4))

# -- result header (polar)
Label(lf_wye, text="Delta Equivalent  (a\u2220\u03b8)",
      font=FONT_HEAD, fg=TITLE_C, bg=PANEL
      ).grid(row=11, column=0, columnspan=2, sticky="w", pady=(0, 4))

for r, lbl in enumerate(["Zab", "Zbc", "Zca"], start=12):
    Label(lf_wye, text=lbl, font=FONT_BODY, fg=TXT_DIM, bg=PANEL,
          width=5, anchor="e").grid(row=r, column=0, sticky="e", pady=3)

wd_zab_polar = Entry(lf_wye, font=FONT_MONO, bg=RESULT_BG, fg=TITLE_C,
                      relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                      state="readonly", readonlybackground=RESULT_BG)
wd_zab_polar.grid(row=12, column=1, sticky="ew", pady=3, ipady=4)

wd_zbc_polar = Entry(lf_wye, font=FONT_MONO, bg=RESULT_BG, fg=TITLE_C,
                      relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                      state="readonly", readonlybackground=RESULT_BG)
wd_zbc_polar.grid(row=13, column=1, sticky="ew", pady=3, ipady=4)

wd_zca_polar = Entry(lf_wye, font=FONT_MONO, bg=RESULT_BG, fg=TITLE_C,
                      relief=FLAT, highlightthickness=1, highlightbackground=BORDER,
                      state="readonly", readonlybackground=RESULT_BG)
wd_zca_polar.grid(row=14, column=1, sticky="ew", pady=3, ipady=4)


# =============================================================================
#  BOTTOM  –  Solution / Output area
# =============================================================================
sol_frame = LabelFrame(
    window,
    text="  Solution / Output  ",
    font=FONT_HEAD, fg=HINT_C, bg=PANEL,
    bd=2, relief=RIDGE, padx=8, pady=6
)
sol_frame.grid(row=2, column=0, columnspan=3, sticky="ew",
               padx=6, pady=(4, 6))
sol_frame.columnconfigure(0, weight=1)

# -- toolbar row for the solution box
sol_toolbar = Frame(sol_frame, bg=PANEL)
sol_toolbar.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 4))
Button(sol_toolbar, text="Clear Solution", font=FONT_SMALL,
       bg="#b71c1c", fg=TXT, activebackground="#c62828",
       relief=FLAT, padx=10, pady=3, cursor="hand2",
       command=_sol_clear).pack(side=LEFT, padx=(0, 6))
Button(sol_toolbar, text="Copy", font=FONT_SMALL,
       bg="#2e7d32", fg=TXT, activebackground="#388e3c",
       relief=FLAT, padx=10, pady=3, cursor="hand2",
       command=_sol_copy).pack(side=LEFT, padx=(0, 6))
Button(sol_toolbar, text="Save As", font=FONT_SMALL,
       bg="#4527a0", fg=TXT, activebackground="#512da8",
       relief=FLAT, padx=10, pady=3, cursor="hand2",
       command=_sol_saveas).pack(side=LEFT, padx=(0, 6))
Button(sol_toolbar, text="Print", font=FONT_SMALL,
       bg="#1565c0", fg=TXT, activebackground="#1976d2",
       relief=FLAT, padx=10, pady=3, cursor="hand2",
       command=_sol_print).pack(side=LEFT)

sol_text = Text(
    sol_frame,
    font=FONT_MONO, fg=HINT_C, bg="#0d1117",
    height=8, relief=FLAT, state=DISABLED,
    selectbackground=BORDER, insertbackground=HINT_C
)
sol_text.grid(row=1, column=0, sticky="ew")

sol_scroll = Scrollbar(sol_frame, orient=VERTICAL, command=sol_text.yview,
                       bg=PANEL, troughcolor=BG, activebackground=BORDER)
sol_scroll.grid(row=1, column=1, sticky="ns")
sol_text.config(yscrollcommand=sol_scroll.set)

_sol_write(
    "  Ready.  Enter impedances in  a +/- jb  form and press  COMPUTE.\n\n"
    "  Format examples:\n"
    "    3+j4        ->  real = 3,  imaginary = +4\n"
    "    10-j6.5     ->  real = 10, imaginary = -6.5\n"
    "    -2+j5       ->  real = -2, imaginary = +5\n"
    "    7+j0        ->  purely real impedance\n"
    "    0+j8        ->  purely reactive impedance\n"
)

window.mainloop()
