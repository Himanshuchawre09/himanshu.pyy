import tkinter as tk
from tkinter import messagebox
import json

def get_rating(reviews):
    return '⭐' * (sum(reviews) // len(reviews) if reviews else 5)

# Load the menu from a JSON file
with open('menu.json', 'r') as f:
    data = json.load(f)

items = data.get('items', [])

def show_menu():
    menu_text = "ID\tName\t\tPrice\tRating\n" + '-' * 50 + '\n'
    for item in items:
        menu_text += f'{item["id"]}\t{item["name"]}\t{item["price"]}\t{get_rating(item.get("reviews", []))}\n'
    menu_label.config(text=menu_text)

def order_items():
    order_ids = order_entry.get().split(',')
    total_bill = 0
    order_details = "ID\tName\t\tPrice\n" + '-' * 50 + '\n'
    for order_id in order_ids:
        for item in items:
            if item['id'] == int(order_id.strip()):
                order_details += f'{item["id"]}\t{item["name"]}\t{item["price"]}\n'
                total_bill += int(item['price'])
                break
    order_details += '-' * 50 + f'\nTotal Amount: {total_bill}'
    messagebox.showinfo("Order Details", order_details)

def add_feedback():
    item_no = int(item_id_entry.get())
    rating = int(rating_entry.get())
    for item in items:
        if item['id'] == item_no:
            item.setdefault('reviews', []).append(rating)
            break
    messagebox.showinfo("Feedback", "Thank you for your rating!")

root = tk.Tk()
root.title("Diamond Cafe")

# Menu Section
menu_label = tk.Label(root, text='', justify='left', font=('Arial', 10))
menu_label.pack()

show_menu_button = tk.Button(root, text="Show Menu", command=show_menu)
show_menu_button.pack()

# Order Section
order_label = tk.Label(root, text="Order Items (comma separated item IDs):")
order_label.pack()

order_entry = tk.Entry(root)
order_entry.pack()

order_button = tk.Button(root, text="Order Items", command=order_items)
order_button.pack()

# Feedback Section
feedback_label = tk.Label(root, text="Add Your Feedback")
feedback_label.pack()

item_id_label = tk.Label(root, text="Item ID:")
item_id_label.pack()

item_id_entry = tk.Entry(root)
item_id_entry.pack()

rating_label = tk.Label(root, text="Rating (1-5):")
rating_label.pack()

rating_entry = tk.Entry(root)
rating_entry.pack()

feedback_button = tk.Button(root, text="Submit Feedback", command=add_feedback)
feedback_button.pack()

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

# Start the application
root.mainloop()
