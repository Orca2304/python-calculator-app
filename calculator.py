
import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        self.root.geometry("320x450")
        self.root.resizable(False, False)

        self.history = []

        self.display = tk.Entry(
            root,
            font=("Arial", 22),
            justify="right"
        )
        self.display.pack(fill="x")

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "DEL", "+"],
            ["HISTORY", "=", "%", "."]
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")

            for value in row:
                tk.Button(
                    frame,
                    text=value,
                    font=("Arial", 13),
                    command=lambda v=value: self.click(v)
                ).pack(side="left", expand=True, fill="both")

    def click(self, value):
        if value == "C":
            self.display.delete(0, tk.END)

        elif value == "DEL":
            text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, text[:-1])

        elif value == "=":
            self.calculate()

        elif value == "HISTORY":
            self.show_history()

        else:
            self.display.insert(tk.END, value)

    def calculate(self):
        expression = self.display.get()

        try:
            # Allow only basic arithmetic characters
            if not expression or any(
                char not in "0123456789+-*/%.() " 
                for char in expression
            ):
                raise ValueError

            result = eval(expression, {"__builtins__": {}}, {})

            self.history.append(f"{expression} = {result}")

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        except Exception:
            messagebox.showerror(
                "Error",
                "Please enter a valid calculation."
            )

    def show_history(self):
        window = tk.Toplevel(self.root)
        window.title("Calculation History")
        window.geometry("300x300")

        history_box = tk.Listbox(window, font=("Arial", 12))
     

        for item in reversed(self.history):
            history_box.insert(tk.END, item)

        if not self.history:
            history_box.insert(tk.END, "No calculations yet.")


root = tk.Tk()
app = Calculator(root)
root.mainloop()
