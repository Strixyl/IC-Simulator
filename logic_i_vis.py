import tkinter as tk
from tkinter import simpledialog, messagebox

# Logic gate functions
def AND(*args):
    result = args[0]
    for arg in args[1:]:
        result &= arg
    return result

def OR(*args):
    result = args[0]
    for arg in args[1:]:
        result |= arg
    return result

def NOT(a):
    return ~a & 1

def NAND(*args):
    result = args[0]
    for arg in args[1:]:
        result &= arg
    return ~result & 1

def NOR(*args):
    result = args[0]
    for arg in args[1:]:
        result |= arg
    return ~result & 1

def XOR(*args):
    result = args[0]
    for arg in args[1:]:
        result ^= arg
    return result

# for validating inputs 1 or 0 
def validate_digit(char):
    return char in '01' and len(char) == 1

# display logic gate
def display_logic_gates():
    root = tk.Tk()
    root.title("Logic Gates")
    root.geometry("400x400")  

    
    num_gates = simpledialog.askinteger("Input", "How many input gates do you need?", minvalue=1, maxvalue=14)


    num_inputs = simpledialog.askinteger("Input", "How many inputs per gate (2 or 3)?", minvalue=2, maxvalue=3)

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
                for i in range(0, len(inputs), num_inputs):
                    a = inputs[i]
                    b = inputs[i + 1] if i + 1 < len(inputs) else 0
                    c = inputs[i + 2] if num_inputs == 3 and i + 2 < len(inputs) else 0
                    if gate == "AND":
                        result = AND(a, b, c)
                    elif gate == "OR":
                        result = OR(a, b, c)
                    elif gate == "NAND":
                        result = NAND(a, b, c)
                    elif gate == "NOR":
                        result = NOR(a, b, c)
                    elif gate == "XOR":
                        result = XOR(a, b, c)
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

  
    vcmd = (root.register(validate_digit), '%S')

    entries = []
    for i in range(num_gates * num_inputs):
        tk.Label(root, text=f"Input {i + 1}:").grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(root, width=15, validate='key', validatecommand=vcmd)  # Increased width and added validation
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    tk.Label(root, text="Select Gate:").grid(row=num_gates * num_inputs, column=0, padx=10, pady=5)
    gate_var = tk.StringVar(root)
    gate_var.set("AND")  # default value
    gate_menu = tk.OptionMenu(root, gate_var, "AND", "OR", "NOT", "NAND", "NOR", "XOR")
    gate_menu.config(width=10)  # Increased width
    gate_menu.grid(row=num_gates * num_inputs, column=1, padx=10, pady=5)

    tk.Button(root, text="Calculate", command=calculate).grid(row=num_gates * num_inputs + 1, column=0, padx=10, pady=10)
    tk.Button(root, text="Clear", command=clear).grid(row=num_gates * num_inputs + 1, column=1, padx=10, pady=10)
    tk.Button(root, text="Return", command=return_to_main).grid(row=num_gates * num_inputs + 2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

# display ic
def display_integrated_circuit():
    root = tk.Tk()
    root.title("Integrated Circuit")
    root.geometry("750x800")  

    num_gates = 7  # Fixed number of gates

    # Ask the user how many inputs per gate
    num_inputs = simpledialog.askinteger("Input", "How many inputs per gate (2 or 3)?", minvalue=2, maxvalue=3)
    
    # canvas illutstration fot IC
    canvas = tk.Canvas(root, width=750, height=800)
    canvas.grid(row=0, column=0)
    
    #draw gates and connections
    gate_positions = []
    for i in range(num_gates):
        x = 50 + i * 100
        y = 50
        gate_positions.append((x, y))
        canvas.create_rectangle(x, y, x + 50, y + 50, outline="black", fill="white")
        canvas.create_text(x + 25, y + 25, text=f"Gate {i + 1}")
    
    for i in range(num_gates - 1):
        x1, y1 = gate_positions[i][0] + 50, gate_positions[i][1] + 25
        x2, y2 = gate_positions[i + 1][0], gate_positions[i + 1][1] + 25
        canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
    
    # Validate inputs for 1 and 0
    def validate_inputs(inputs):
        if any(i not in [0, 1] for i in inputs):
            raise ValueError("Inputs must be 0 or 1")

    def calculate():
        try:
            inputs = [int(entry.get()) for entry in entries]
            if any(i not in [0, 1] for i in inputs):
                raise ValueError("Inputs must be 0 or 1")
            results = []
            for i in range(num_gates):
                gate = gate_vars[i].get()
                a = inputs[i * num_inputs]
                b = inputs[i * num_inputs + 1] if i * num_inputs + 1 < len(inputs) else 0
                c = inputs[i * num_inputs + 2] if num_inputs == 3 and i * num_inputs + 2 < len(inputs) else 0
                if gate == "AND":
                    result = AND(a, b, c)
                elif gate == "OR":
                    result = OR(a, b, c)
                elif gate == "NAND":
                    result = NAND(a, b, c)
                elif gate == "NOR":
                    result = NOR(a, b, c)
                elif gate == "XOR":
                    result = XOR(a, b, c)
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

    # Validation command for entry widgets
    vcmd = (root.register(validate_digit), '%S')

    entries = []
    gate_vars = []
    for i in range(num_gates * num_inputs):
        tk.Label(root, text=f"Input {i + 1}:").grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(root, width=20, validate='key', validatecommand=vcmd)  # Increased width and added validation
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    for i in range(num_gates):
        tk.Label(root, text=f"Select Gate {i + 1}:").grid(row=num_gates * num_inputs + i, column=0, padx=10, pady=5)
        gate_var = tk.StringVar(root)
        gate_var.set("AND")  # default value
        gate_menu = tk.OptionMenu(root, gate_var, "AND", "OR", "NAND", "NOR", "XOR")
        gate_menu.config(width=10)  # Increased width
        gate_menu.grid(row=num_gates * num_inputs + i, column=1, padx=10, pady=5)
        gate_vars.append(gate_var)

    tk.Button(root, text="Calculate", command=calculate).grid(row=num_gates * num_inputs + num_gates, column=0, padx=10, pady=10)
    tk.Button(root, text="Clear", command=clear).grid(row=num_gates * num_inputs + num_gates, column=1, padx=10, pady=10)
    tk.Button(root, text="Return", command=return_to_main).grid(row=num_gates * num_inputs + num_gates + 1, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

# Main menu to choose between logic gates calculator and integrated circuit
def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("600x300")  # Set fixed size for the window

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