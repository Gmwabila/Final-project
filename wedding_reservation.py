import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to handle booking confirmation
def confirm_booking():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    event_date = entry_event_date.get()
    num_guests = entry_num_guests.get()
    deposit_amount = entry_deposit_amount.get()  # Get user-defined deposit amount

    if not first_name or not last_name or not event_date or not num_guests or not deposit_amount:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    try:
        num_guests = int(num_guests)
        if num_guests <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Number of guests must be a positive integer!")
        return

    try:
        deposit_amount = float(deposit_amount)
        if deposit_amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Deposit amount must be a positive number!")
        return

    # Summary of reservation
    summary = (
        f"Reservation Summary:\n"
        f"Name: {first_name} {last_name}\n"
        f"Event Date: {event_date}\n"
        f"Number of Guests: {num_guests}\n"
        f"Deposit Amount: ${deposit_amount}\n\n"
        f"Do you want to confirm this booking?"
    )
    confirm = messagebox.askyesno("Confirm Booking", summary)
    if confirm:
        save_reservation(first_name, last_name, event_date, num_guests, deposit_amount)
        messagebox.showinfo("Booking Confirmed", "Your reservation has been confirmed!")
        clear_inputs()

# Function to save reservation details to a file
def save_reservation(first_name, last_name, event_date, num_guests, deposit_amount):
    with open("wedding_reservations.txt", "a") as file:
        file.write(f"{first_name} {last_name}, {event_date}, {num_guests} guests, ${deposit_amount}\n")

# Function to clear input fields
def clear_inputs():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_event_date.delete(0, tk.END)
    entry_num_guests.delete(0, tk.END)
    entry_deposit_amount.delete(0, tk.END)

# Create main application window
root = tk.Tk()
root.title("Wedding Reservation App")

# Layout widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and entries for input
ttk.Label(frame, text="First Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_first_name = ttk.Entry(frame, width=25)
entry_first_name.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Last Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_last_name = ttk.Entry(frame, width=25)
entry_last_name.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Event Date (YYYY-MM-DD):").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_event_date = ttk.Entry(frame, width=25)
entry_event_date.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Number of Guests:").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_num_guests = ttk.Entry(frame, width=25)
entry_num_guests.grid(row=3, column=1, pady=5)

ttk.Label(frame, text="Deposit Amount:").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_deposit_amount = ttk.Entry(frame, width=25)
entry_deposit_amount.grid(row=4, column=1, pady=5)

# Confirm Booking Button
btn_confirm = ttk.Button(frame, text="Confirm Booking", command=confirm_booking)
btn_confirm.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
 

