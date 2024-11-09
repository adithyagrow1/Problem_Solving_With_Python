import tkinter as tk


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get().replace('x', '*')))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


def on_enter(event):
    event.widget.config(bg="#666666")


def on_leave(event):
    text = event.widget.cget("text")
    if text == "=":
        event.widget.config(bg="#4EA97D")  # Special color for "=" button
    else:
        event.widget.config(bg="#444444")  # Default button color


def on_press(event):
    event.widget.config(relief=tk.SUNKEN)


def on_release(event):
    event.widget.config(relief=tk.RAISED)


def keypress(event):
    if event.char in "0123456789+-*/":
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        click(event)
    elif event.keysym == "BackSpace":
        entry.delete(len(entry.get()) - 1, tk.END)


# Set up main window
root = tk.Tk()
root.title("ADI'S CALCULATOR")
root.geometry("300x400")
root.resizable(0, 0)
root.configure(bg="#000080")

# Entry field
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief=tk.SUNKEN, justify=tk.RIGHT, bg="#333333",
                 fg="#ffffff", insertbackground="white")
entry.pack(fill=tk.X, padx=10, pady=(10, 20), ipady=10)
entry.bind("<Key>", keypress)

# Button frame
buttons_frame = tk.Frame(root, bg="#222222")
buttons_frame.pack(fill=tk.BOTH, expand=True)

button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    ["C", "0", "+", "="]
]


def create_button(parent, text, bg_color="#4EA97D", fg_color="#ffffff"):
    btn = tk.Button(parent, text=text, font=("Arial", 18, "bold"), fg=fg_color, bg=bg_color, activebackground="#666666",
                    activeforeground="#4EA97D", relief=tk.RAISED, borderwidth=3)
    btn.bind("<Button-1>", click)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<ButtonPress>", on_press)
    btn.bind("<ButtonRelease>", on_release)

    if text == "=":
        btn.config(bg="#4EA97D", fg="#ffffff", font=("Arial", 18, "bold"))
    btn.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)

    return btn


# Create buttons
for row in button_texts:
    row_frame = tk.Frame(buttons_frame, bg="#000080")
    row_frame.pack(expand=True, fill="both")
    for text in row:
        color = "#4EA97D" if text == "=" else "#444444"
        create_button(row_frame, text, bg_color=color)

root.mainloop()
