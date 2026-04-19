import tkinter as tk

def convert():
    value = float(entry.get())
    choice = var.get()

    if choice == "C to F":
        result = (value * 9/5) + 32
    elif choice == "F to C":
        result = (value - 32) * 5/9
    elif choice == "IN to FT":
        result = value / 12
    elif choice == "FT to IN":
        result = value * 12
    elif choice == "INR to USD":
        result = value / 83
    elif choice == "USD to INR":
        result = value * 83

    label_result.config(text=f"Result: {result:.2f}")

root = tk.Tk()
root.title("Unit Converter")

entry = tk.Entry(root)
entry.pack()

var = tk.StringVar()
var.set("C to F")

options = ["C to F", "F to C", "IN to FT", "FT to IN", "INR to USD", "USD to INR"]
menu = tk.OptionMenu(root, var, *options)
menu.pack()

btn = tk.Button(root, text="Convert", command=convert)
btn.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

root.mainloop()