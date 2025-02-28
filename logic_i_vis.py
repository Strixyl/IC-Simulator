import tkinter as tk
from tkinter import simpledialog, messagebox

# Logic gate functions
def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return ~a & 1

def NAND(a, b):
    return ~(a & b) & 1

def NOR(a, b):
    return ~(a | b) & 1

def XOR(a, b):
    return a ^ b

# Function to display logic gate results
def display_logic_gates():
    root = tk.Tk()
    root.title("Logic Gates")

    # Ask the user how many input gates they need
    num_gates = simpledialog.askinteger("Input", "How many input gates do you need?", minvalue=1, maxvalue=14)

    def calculate():
        try:
            inputs = [int(entry.get()) for entry in entries]
            if any(i not in [0, 1] for i in inputs):
                raise ValueError("Inputs must be 0 or 1")
            gate = gate_var.get()
            results = []
            if gate == "NOT":
                for i in inputs:
                    results.append(NOT(i))
            else:
                for i in range(0, len(inputs), 2):
                    a = inputs[i]
                    b = inputs[i + 1] if i + 1 < len(inputs) else 0
                    if gate == "AND":
                        result = AND(a, b)
                    elif gate == "OR":
                        result = OR(a, b)
                    elif gate == "NAND":
                        result = NAND(a, b)
                    elif gate == "NOR":
                        result = NOR(a, b)
                    elif gate == "XOR":
                        result = XOR(a, b)
                    else:
                        result = "Invalid gate selected"
                    results.append(result)
            result_text = "\n".join([f"Gate {i + 1}: {result}" for i, result in enumerate(results)])
            messagebox.showinfo("Results", result_text)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear():
        for entry in entries:
            entry.delete(0, tk.END)

    entries = []
    for i in range(num_gates):
        tk.Label(root, text=f"Input {i + 1}:").grid(row=i, column=0)
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=1)
        entries.append(entry)

    tk.Label(root, text="Select Gate:").grid(row=num_gates, column=0)
    gate_var = tk.StringVar(root)
    gate_var.set("AND")  # default value
    gate_menu = tk.OptionMenu(root, gate_var, "AND", "OR", "NOT", "NAND", "NOR", "XOR")
    gate_menu.grid(row=num_gates, column=1)

    tk.Button(root, text="Calculate", command=calculate).grid(row=num_gates + 1, column=0)
    tk.Button(root, text="Clear", command=clear).grid(row=num_gates + 1, column=1)

    root.mainloop()

# Display logic gates GUI
display_logic_gates()