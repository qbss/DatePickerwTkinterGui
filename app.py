from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
Appversion = "1.0.0"




def pick_date(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    date_window = tk.Toplevel(root)
    date_window.title(prompt)

    cal = Calendar(date_window, date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)

    def select_date():
        selected_date.set(cal.get_date())
        date_window.destroy()

    selected_date = tk.StringVar()
    tk.Button(date_window, text="Select", command=select_date).pack(pady=10)
    root.wait_window(date_window)
    return selected_date.get()

def calculate_dates_between():
    start_date_str = pick_date("Select Start Date")
    end_date_str = pick_date("Select End Date")
    
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        if start_date > end_date:
            messagebox.showerror("Error", "Start date must be before end date.")
            return
        # Calculate the difference in days
        days_difference = (end_date - start_date).days
        messagebox.showinfo("Result", f"The number of days between the selected dates is {days_difference} days.")    
        
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
# Main function to run the date picker and calculation
calculate_dates_between()