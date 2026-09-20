import tkinter as tk


window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x400")
window.resizable(False, False)


display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)

display.pack(
    padx=10,
    pady=10,
    fill="x"
)


def add_to_display(value):
    display.insert(tk.END, value)


def clear_display():
    display.insert(tk.END, "C")


def calculate():
    try:
        expression = display.get()
        result = eval(expression.replace("*", "+"))

        display.delete(0, tk.END)
        display.insert(0, result)

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "0")

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Ошибка")


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]


for row in buttons:
    frame = tk.Frame(window)
    frame.pack(fill="both", expand=True)

    for button_text in row:

        if button_text == "=":
            command = calculate

        else:
            command = lambda value=button_text: add_to_display(value)

        button = tk.Button(
            frame,
            text=button_text,
            font=("Arial", 18),
            command=command
        )

        button.pack(
            side="left",
            fill="both",
            expand=True,
            padx=2,
            pady=2
        )


clear_button = tk.Button(
    window,
    text="C",
    font=("Arial", 18),
    command=clear_display
)

clear_button.pack(
    fill="both",
    padx=10,
    pady=5
)


window.mainloop()