import tkinter as tk
from tkinter import messagebox

runner_speeds = {}

def add_runner():
    try:
        runner_id = len(runner_speeds) + 1
        speed = float(speed_entry.get())
        runner_speeds[runner_id] = speed
        result_label.config(text=f"Added Runner {runner_id} with speed {speed} m/s")
        speed_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid speed (e.g., 10.5)")

def compare(r1, r2):
    return r1 if runner_speeds[r1] > runner_speeds[r2] else r2

def find_fastest_runner():
    n = len(runner_speeds)
    if n < 2:
        messagebox.showwarning("Not Enough Runners", "Add at least 2 runners.")
        return

    wins = [0] * (n + 1)
    for i in runner_speeds:
        for j in runner_speeds:
            if i != j:
                winner = compare(i, j)
                if winner == i:
                    wins[i] += 1

    for i in runner_speeds:
        if wins[i] == n - 1:
            result_label.config(text=f"🏁 Fastest Runner is: Runner {i} ({runner_speeds[i]} m/s)")
            return

    result_label.config(text="⚠️ No unique fastest runner found.")

# GUI Setup
root = tk.Tk()
root.title("Fastest Runner Finder")

tk.Label(root, text="Enter Runner Speed (m/s):").pack()
speed_entry = tk.Entry(root)
speed_entry.pack()

tk.Button(root, text="Add Runner", command=add_runner).pack(pady=5)
tk.Button(root, text="Find Fastest Runner", command=find_fastest_runner).pack(pady=5)

result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
