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
    root.geometry("400x400")  # Set fixed size for the window

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

    def return_to_main():
        root.destroy()
        main_menu()

    entries = []
    for i in range(num_gates):
        tk.Label(root, text=f"Input {i + 1}:").grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    tk.Label(root, text="Select Gate:").grid(row=num_gates, column=0, padx=10, pady=5)
    gate_var = tk.StringVar(root)
    gate_var.set("AND")  # default value
    gate_menu = tk.OptionMenu(root, gate_var, "AND", "OR", "NOT", "NAND", "NOR", "XOR")
    gate_menu.grid(row=num_gates, column=1, padx=10, pady=5)

    tk.Button(root, text="Calculate", command=calculate).grid(row=num_gates + 1, column=0, padx=10, pady=10)
    tk.Button(root, text="Clear", command=clear).grid(row=num_gates + 1, column=1, padx=10, pady=10)
    tk.Button(root, text="Return", command=return_to_main).grid(row=num_gates + 2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()


# NEW FUNCTION FOR INTEGRATED CIRCUIT
# Function to display integrated circuit results
def display_integrated_circuit():
    root = tk.Tk()
    root.title("Integrated Circuit")
    root.geometry("600x800")  # Set initial size for the window

    num_gates = 7  # Fixed number of gates

    def calculate():
        try:
            inputs = [int(entry.get()) for entry in entries]
            if any(i not in [0, 1] for i in inputs):
                raise ValueError("Inputs must be 0 or 1")
            results = []
            for i in range(num_gates):
                gate = gate_vars[i].get()
                a = inputs[i * 2]
                b = inputs[i * 2 + 1] if i * 2 + 1 < len(inputs) else 0
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
            output_gate = simpledialog.askinteger("Output", "Which gate provides the output signal?", minvalue=1, maxvalue=num_gates)
            result_text = f"Output from Gate {output_gate}: {results[output_gate - 1]}"
            messagebox.showinfo("Results", result_text)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear():
        for entry in entries:
            entry.delete(0, tk.END)

    def return_to_main():
        root.destroy()
        main_menu()

    entries = []
    gate_vars = []
    for i in range(num_gates * 2):
        tk.Label(root, text=f"Input {i + 1}:").grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    for i in range(num_gates):
        tk.Label(root, text=f"Select Gate {i + 1}:").grid(row=num_gates * 2 + i, column=0, padx=10, pady=5)
        gate_var = tk.StringVar(root)
        gate_var.set("AND")  # default value
        gate_menu = tk.OptionMenu(root, gate_var, "AND", "OR", "NAND", "NOR", "XOR")
        gate_menu.grid(row=num_gates * 2 + i, column=1, padx=10, pady=5)
        gate_vars.append(gate_var)

    tk.Button(root, text="Calculate", command=calculate).grid(row=num_gates * 3, column=0, padx=10, pady=10)
    tk.Button(root, text="Clear", command=clear).grid(row=num_gates * 3, column=1, padx=10, pady=10)
    tk.Button(root, text="Return", command=return_to_main).grid(row=num_gates * 3 + 1, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

# Main menu to choose between logic gates calculator and integrated circuit
def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("300x200")  # Set fixed size for the window

    def open_logic_gates():
        root.destroy()
        display_logic_gates()

    def open_integrated_circuit():
        root.destroy()
        display_integrated_circuit()

    tk.Button(root, text="Logic Gates Calculator", command=open_logic_gates).pack(pady=10)
    tk.Button(root, text="Integrated Circuit", command=open_integrated_circuit).pack(pady=10)

    root.mainloop()

# Display main menu
main_menu()