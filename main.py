# ============================================================
# Program: In-N-Out Burger Ordering (Tkinter GUI)
# Author: Alen Chavez
# Description:
#   Desktop GUI that simulates a simple fast-food ordering flow.
#   Users can add items/combos to a cart, view a running total,
#   see tax and final amount, remove items, and proceed to a
#   checkout/confirmation screen with order number and timestamp.
#   Image loading is optional: place "Logo.png" in the same folder
#   as this file and it will render automatically.
# ============================================================

import tkinter as tk
import math
import random
from datetime import datetime
from pathlib import Path  # for robust local image path

class InNOutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("In-N-Out Burger Mobile App")
        self.geometry("400x800")
        self.configure(bg='#F40000')  # In-N-Out red background

        self.cart = []          # Initialize an empty cart
        self.tax_rate = 0.08    # 8% tax rate

        # ----- Frames -----
        self.home_frame = tk.Frame(self, bg='#F40000')
        self.home_frame.pack(fill="both", expand=True)

        # Define a menu frame so show_* calls work safely
        self.menu_frame = tk.Frame(self, bg='#F40000')

        # ----- Home UI -----
        self.welcome_label = tk.Label(
            self.home_frame,
            text="Welcome to In-N-Out Burger!",
            font=("Arial", 18),
            bg='#F40000',
            fg='white'
        )
        self.welcome_label.pack(pady=10)

        # Load and display the logo image from SAME FOLDER as this file (optional if missing)
        logo_path = Path(__file__).resolve().parent / "Logo.png"
        try:
            if logo_path.exists():
                logo_img = tk.PhotoImage(file=str(logo_path))
                max_w, max_h = 200, 100
                scale = max(logo_img.width() / max_w, logo_img.height() / max_h, 1)
                if scale > 1:
                    resize = math.ceil(scale)
                    self.logo_photo = logo_img.subsample(resize, resize)
                else:
                    self.logo_photo = logo_img
                self.logo_label = tk.Label(self.home_frame, image=self.logo_photo, bg='#F40000')
                self.logo_label.pack(pady=10)
        except Exception:
            # If the image can't be loaded, just skip it (keeps app running)
            pass

        self.order_label = tk.Label(self.home_frame, text="Order:", font=("Arial", 16), bg='#F40000', fg='white')
        self.order_label.pack(pady=5)

        self.combos_label = tk.Label(self.home_frame, text="Combos", font=("Arial", 14), bg='#F40000', fg='white')
        self.combos_label.pack(pady=5)

        self.combos_frame = tk.Frame(self.home_frame, bg='#F40000')
        self.combos_frame.pack(pady=5)

        button_size = 10

        self.combo1_button = tk.Button(
            self.combos_frame,
            text="Double Double, Fries, Medium Drink $9.70",
            width=button_size,
            height=int(button_size / 2),
            wraplength=100,
            bg='white',
            fg='black',
            command=lambda: self.add_to_cart("Double Double Combo", 9.70)
        )
        self.combo1_button.grid(row=0, column=0, padx=5, pady=5)

        self.combo2_button = tk.Button(
            self.combos_frame,
            text="Cheeseburger, Fries, Medium Drink $8.10",
            width=button_size,
            height=int(button_size / 2),
            wraplength=100,
            bg='white',
            fg='black',
            command=lambda: self.add_to_cart("Cheeseburger Combo", 8.10)
        )
        self.combo2_button.grid(row=0, column=1, padx=5, pady=5)

        self.combo3_button = tk.Button(
            self.combos_frame,
            text="Hamburger, Fries, Medium Drink $7.70",
            width=button_size,
            height=int(button_size / 2),
            wraplength=100,
            bg='white',
            fg='black',
            command=lambda: self.add_to_cart("Hamburger Combo", 7.70)
        )
        self.combo3_button.grid(row=0, column=2, padx=5, pady=5)

        self.custom_order_label = tk.Label(self.home_frame, text="Custom Order", font=("Arial", 14), bg='#F40000', fg='white')
        self.custom_order_label.pack(pady=5)

        self.double_double_button = tk.Button(self.home_frame, text="Double Double $5.35", width=button_size * 2, bg='white', fg='black', command=lambda: self.add_to_cart("Double Double", 5.35))
        self.double_double_button.pack(pady=5)

        self.cheeseburger_button = tk.Button(self.home_frame, text="Cheeseburger $3.75", width=button_size * 2, bg='white', fg='black', command=lambda: self.add_to_cart("Cheeseburger", 3.75))
        self.cheeseburger_button.pack(pady=5)

        self.hamburger_button = tk.Button(self.home_frame, text="Hamburger $3.35", width=button_size * 2, bg='white', fg='black', command=lambda: self.add_to_cart("Hamburger", 3.35))
        self.hamburger_button.pack(pady=5)

        self.fries_button = tk.Button(self.home_frame, text="French Fries $2.20", width=button_size * 2, bg='white', fg='black', command=lambda: self.add_to_cart("French Fries", 2.20))
        self.fries_button.pack(pady=5)

        self.shakes_button = tk.Button(self.home_frame, text="Shakes $2.90", width=button_size * 2, bg='white', fg='black', command=lambda: self.add_to_cart("Shake", 2.90))
        self.shakes_button.pack(pady=5)

        self.beverages_label = tk.Label(self.home_frame, text="Beverages", font=("Arial", 14), bg='#F40000', fg='white')
        self.beverages_label.pack(pady=5)

        self.soft_drinks_label = tk.Label(self.home_frame, text="Soft Drinks", font=("Arial", 12), bg='#F40000', fg='white')
        self.soft_drinks_label.pack(pady=5)

        self.size_frame = tk.Frame(self.home_frame, bg='#F40000')
        self.size_frame.pack(pady=5)

        drink_sizes = [("Small $2.00", 2.00), ("Medium $2.15", 2.15), ("Large $2.35", 2.35), ("X-Large $2.55", 2.55)]
        for size, price in drink_sizes:
            btn = tk.Button(self.size_frame, text=size, width=button_size, bg='white', fg='black', command=lambda s=size, p=price: self.add_to_cart(s, p))
            btn.pack(side="left", padx=5, pady=5)

        self.cart_button = tk.Button(self.home_frame, text="View Cart", width=button_size * 2, bg='white', fg='black', command=self.view_cart)
        self.cart_button.pack(pady=20)

    # ----- Cart & Checkout -----
    def add_to_cart(self, item, price):
        self.cart.append((item, price))

    def view_cart(self):
        cart_window = tk.Toplevel(self)
        cart_window.title("Your Cart")
        cart_window.geometry("400x400")
        cart_window.configure(bg='#F40000')

        cart_label = tk.Label(cart_window, text="Your Cart", font=("Arial", 16), bg='#F40000', fg='white')
        cart_label.pack(pady=10)

        total = 0
        for i, (item, price) in enumerate(self.cart):
            frame = tk.Frame(cart_window, bg='#F40000')
            frame.pack(anchor='w', padx=10, pady=5, fill='x')

            item_label = tk.Label(frame, text=item, bg='#F40000', fg='white', wraplength=250, justify="left")
            item_label.pack(side="left")

            price_label = tk.Label(frame, text=f"${price:.2f}", bg='#F40000', fg='white', justify="right")
            price_label.pack(side="right")

            remove_button = tk.Button(frame, text="Remove", bg='white', fg='black', command=lambda idx=i: self.remove_from_cart(idx, cart_window))
            remove_button.pack(side="right", padx=5)

            total += price

        tax = total * self.tax_rate
        total_with_tax = total + tax

        total_label = tk.Label(cart_window, text=f"Total: ${total:.2f}\nTax: ${tax:.2f}\nTotal with Tax: ${total_with_tax:.2f}", font=("Arial", 14), bg='#F40000', fg='white')
        total_label.pack(pady=10)

        checkout_button = tk.Button(cart_window, text="Checkout/Pick-up", bg='white', fg='black', command=lambda: self.show_order_screen(total_with_tax, cart_window))
        checkout_button.pack(pady=20)

    def remove_from_cart(self, idx, window):
        self.cart.pop(idx)
        window.destroy()
        self.view_cart()

    def show_order_screen(self, total_with_tax, cart_window):
        cart_window.destroy()
        order_window = tk.Toplevel(self)
        order_window.title("Order Confirmation")
        order_window.geometry("400x400")
        order_window.configure(bg='#F40000')

        order_number = random.randint(1, 100)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        order_label = tk.Label(order_window, text=f"Order Number: {order_number}", font=("Arial", 24, "bold"), bg='#F40000', fg='white')
        order_label.pack(pady=10)

        datetime_label = tk.Label(order_window, text=current_datetime, font=("Arial", 14), bg='#F40000', fg='white')
        datetime_label.pack(pady=10)

        for item, price in self.cart:
            item_label = tk.Label(order_window, text=f"{item}: ${price:.2f}", font=("Arial", 12), bg='#F40000', fg='white')
            item_label.pack(anchor='w', padx=10)

        total_label = tk.Label(order_window, text=f"Total with Tax: ${total_with_tax:.2f}", font=("Arial", 14), bg='#F40000', fg='white')
        total_label.pack(pady=10)

        directions_label = tk.Label(order_window, text="Directions: Pay at the terminal", font=("Arial", 12), bg='#F40000', fg='white')
        directions_label.pack(pady=10)

        exit_button = tk.Button(order_window, text="Exit", bg='white', fg='black', command=self.quit)
        exit_button.pack(pady=20)

    # ----- Navigation helpers (safe now that menu_frame exists) -----
    def show_home(self):
        self.menu_frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)

    def show_menu(self):
        self.home_frame.pack_forget()
        self.menu_frame.pack(fill="both", expand=True)

    # Placeholders (future screens)
    def show_deals(self): pass
    def show_locations(self): pass
    def show_profile(self): pass

    def show_burgers(self):
        self.menu_frame.pack_forget()
        self.burgers_frame = tk.Frame(self)
        self.burgers_frame.pack(fill="both", expand=True)

        self.burgers_label = tk.Label(self.burgers_frame, text="Burgers", font=("Arial", 24))
        self.burgers_label.pack(pady=20)

        self.double_double = tk.Label(self.burgers_frame, text="Double-Double: $5.35")
        self.double_double.pack(pady=5)

        self.cheeseburger = tk.Label(self.burgers_frame, text="Cheeseburger: $3.75")
        self.cheeseburger.pack(pady=5)

        self.hamburger = tk.Label(self.burgers_frame, text="Hamburger: $3.50")
        self.hamburger.pack(pady=5)

        self.back_to_menu_button = tk.Button(self.burgers_frame, text="Back to Menu", command=self.show_menu_from_burgers)
        self.back_to_menu_button.pack(pady=20)

    def show_menu_from_burgers(self):
        self.burgers_frame.pack_forget()
        self.menu_frame.pack(fill="both", expand=True)

    def show_fries(self):
        self.menu_frame.pack_forget()
        self.fries_frame = tk.Frame(self)
        self.fries_frame.pack(fill="both", expand=True)

        self.fries_label = tk.Label(self.fries_frame, text="Fries", font=("Arial", 24))
        self.fries_label.pack(pady=20)

        self.fries = tk.Label(self.fries_frame, text="French Fries: $2.20")
        self.fries.pack(pady=5)

        self.back_to_menu_button = tk.Button(self.fries_frame, text="Back to Menu", command=self.show_menu_from_fries)
        self.back_to_menu_button.pack(pady=20)

    def show_menu_from_fries(self):
        self.fries_frame.pack_forget()
        self.menu_frame.pack(fill="both", expand=True)

    def show_drinks(self):
        self.menu_frame.pack_forget()
        self.drinks_frame = tk.Frame(self)
        self.drinks_frame.pack(fill="both", expand=True)

        self.drinks_label = tk.Label(self.drinks_frame, text="Drinks", font=("Arial", 24))
        self.drinks_label.pack(pady=20)

        self.drinks = tk.Label(self.drinks_frame, text="Various Drinks: $1.50 - $2.10")
        self.drinks.pack(pady=5)

        self.back_to_menu_button = tk.Button(self.drinks_frame, text="Back to Menu", command=self.show_menu_from_drinks)
        self.back_to_menu_button.pack(pady=20)

    def show_menu_from_drinks(self):
        self.drinks_frame.pack_forget()
        self.menu_frame.pack(fill="both", expand=True)

    def show_shakes(self):
        self.menu_frame.pack_forget()
        self.shakes_frame = tk.Frame(self)
        self.shakes_frame.pack(fill="both", expand=True)

        self.shakes_label = tk.Label(self.shakes_frame, text="Shakes", font=("Arial", 24))
        self.shakes_label.pack(pady=20)

        self.shakes = tk.Label(self.shakes_frame, text="Shakes: $2.90")
        self.shakes.pack(pady=5)

        self.back_to_menu_button = tk.Button(self.shakes_frame, text="Back to Menu", command=self.show_menu_from_shakes)
        self.back_to_menu_button.pack(pady=20)

    def show_menu_from_shakes(self):
        self.shakes_frame.pack_forget()
        self.menu_frame.pack(fill("both"), expand=True)  # <- safe pack call

if __name__ == "__main__":
    app = InNOutApp()
    app.mainloop()
