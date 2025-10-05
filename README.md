# 🍔 In-N-Out Style Ordering (Tkinter GUI)

A desktop GUI (Tkinter) that simulates a simple fast-food ordering flow. Users add items/combos to a cart, view totals with tax, remove items, and complete a checkout/confirmation screen that shows an order number and timestamp. The logo image is optional: place `Logo.png` in the **same folder** as `main.py` and it will render automatically.

---

## 🚀 Features
- **GUI with Tkinter** (no web server required)
- **Cart management**: add/remove items, live totals
- **Tax calculation** (configurable `tax_rate`)
- **Checkout modal** (`Toplevel`) with order number + date/time
- **Optional logo**: `Logo.png` next to `main.py`
- **Graceful fallback** if the logo is missing (app still runs)

---

## 🧰 Tech Stack
- Python 3.x
- Tkinter (standard library)
- datetime, random, math, pathlib (standard library)
- **No external dependencies** required

---

## 📂 Project Structure
```text
burger-ordering-gui/
├── main.py        ← main Tkinter app
└── Logo.png       ← optional logo (same folder as main.py)
