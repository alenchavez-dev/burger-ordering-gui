# 🍔 In-N-Out Style Ordering (Tkinter GUI)

A desktop GUI (Tkinter) that simulates a simple fast-food ordering flow. Users add items/combos to a cart, view totals with tax, remove items, and complete a checkout/confirmation screen that shows an order number and timestamp. The logo image is optional: place `Logo.png` in the **same folder** as the Python file and it will render automatically.

---

## 🚀 Features
- **GUI with Tkinter** (no web server required)
- **Cart management**: add/remove items, live totals
- **Tax calculation** (configurable `tax_rate`)
- **Checkout modal** (`Toplevel`) with order number + date/time
- **Optional logo**: `Logo.png` next to the `.py` file
- **Graceful fallback** if the logo is missing (app still runs)

---

## 🧰 Tech Stack
- Python 3.x
- Tkinter (standard library)
- datetime, random, math, pathlib (standard library)
- **No external dependencies** required

---

## 📂 Project Structure
burger-ordering-gui/
├── app.py        ← main Tkinter app
└── Logo.png      ← optional logo (same folder as app.py)

---

## ▶️ How to Run
1. Make sure you have Python 3 installed.
2. Put your logo image (optional) in the same folder as `app.py` and name it `Logo.png`.
3. Run the app:

    python3 app.py

On Windows you may use:

    py app.py

---

## 🧪 What to Try
- Click any **Combo** or individual items (burgers, fries, shakes, drinks) to **add to cart**.
- Click **View Cart** to:
  - See itemized list and prices
  - **Remove** any line item
  - View **Total**, **Tax**, and **Total with Tax**
  - Proceed to **Checkout/Pick-up** to get an order number and timestamp

---

## ⚠️ Notes
- App uses a red theme similar to In-N-Out for visual flair. If publishing publicly, consider renaming and using a generic logo to avoid trademark issues.
- Prices, tax rate, and items are hard-coded for demonstration. Adjust easily in `app.py`.
- Floating-point totals are fine for demos. For production-grade money handling, consider using `decimal.Decimal`.

---

## 🧑‍💻 Author
**Alen Chavez**

---

## 📝 License
MIT License
