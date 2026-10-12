import tkinter as tk

root = tk.Tk()
root.title("My First App")
root.geometry("300x150")

label = tk.Label(root, text="Hello, World!", font=("Arial", 16))


root.mainloop()