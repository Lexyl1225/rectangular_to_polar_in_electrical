# DELTA ↔ WYE Converter (Rectangular ↔ Polar)

A simple GUI tool (Tkinter) to convert three-phase impedances between
Delta (Δ) and Wye (Y) configurations. Accepts impedances in rectangular
form (a±jb) and shows results in both rectangular (a±jb) and polar (a∠θ)
formats. Includes features to append, copy, save, and print solution logs.

## Features
- Convert Δ → Y and Y → Δ using standard network formulas
- Input validation for rectangular form (`a±jb`)
- View results in rectangular and polar form
- Append multiple computations to a scrollable solution log
- Copy, Save As (.txt), Print solution output

## Installation
No external dependencies — requires Python 3.x and the Tkinter package
(usually included with standard Python installations).

Windows example (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python main.py
```

Or simply run:

```powershell
python main.py
```

## Usage
1. Enter three Delta impedances (`Zab`, `Zbc`, `Zca`) in rectangular form (e.g. `3+j4`, `10-j6`).
2. Click `COMPUTE` under the Delta panel to get Wye equivalents. Use `Convert to a∠θ` to show polar form.
3. Enter three Wye impedances (`Za`, `Zb`, `Zc`) in the Wye panel and click `COMPUTE` to get Delta equivalents.
4. Solution output is appended to the box at the bottom. Use `Copy`, `Save As`, `Print`, or `Clear Solution` as needed.

## Input Format
- Rectangular form only: `a+j b` or `a-j b` (spaces are tolerated).
- Examples: `3+j4`, `5-j2`, `-2+j1.5`, `0+j8`.

## Formulas Used
- Delta → Wye:

	Za = (Zab × Zca) / (Zab + Zbc + Zca)
	Zb = (Zab × Zbc) / (Zab + Zbc + Zca)
	Zc = (Zbc × Zca) / (Zab + Zbc + Zca)

- Wye → Delta:

	Zab = ((Za×Zb) + (Za×Zc) + (Zb×Zc)) / Zc
	Zbc = ((Za×Zb) + (Za×Zc) + (Zb×Zc)) / Za
	Zca = ((Za×Zb) + (Za×Zc) + (Zb×Zc)) / Zb

## Files
- `main.py` — GUI application and front-end logic
- `complex_electrical_calc.py`, `Pol_to_Rec.py`, `Rec_to_Pol.py` — calculation & parsing helpers

## Notes
- The app uses the system default print handler on Windows via `os.startfile(..., "print")`.
- If you encounter issues with Tkinter, ensure it is installed and available for your Python distribution.

## License
This is your personal project; add a license file if you plan to share it.

---
Generated/updated by developer assistant on March 18, 2026.
