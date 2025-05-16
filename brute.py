import tkinter as tk
from tkinter import ttk, messagebox

class FastestRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fastest Runner Tournament (Brute Force)")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        # Theme and styles
        style = ttk.Style()
        style.theme_use("clam")
        self.bg_color = "#f5f5f5"
        self.accent_color = "#4a7abc"
        self.root.configure(bg=self.bg_color)
        
        style.configure("TFrame", background=self.bg_color)
        style.configure("TButton", background=self.accent_color, foreground="white", font=("Arial", 10, "bold"), padding=5)
        style.configure("TLabel", background=self.bg_color, font=("Arial", 10))
        style.configure("Header.TLabel", background=self.bg_color, font=("Arial", 14, "bold"))

        self.speed_entries = []  # For runner speeds
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)

        title_label = ttk.Label(main_frame, text="Fastest Runner (Based on Speeds)", style="Header.TLabel")
        title_label.pack(pady=(0, 20))

        # Number of runners input
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill="x", pady=10)

        ttk.Label(input_frame, text="Number of Runners:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.runner_var = tk.StringVar(value="5")
        runner_entry = ttk.Entry(input_frame, textvariable=self.runner_var, width=10)
        runner_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(input_frame, text="Set Runners", command=self.generate_speed_inputs).grid(row=0, column=2, padx=10)

        self.speeds_frame = ttk.Frame(main_frame)
        self.speeds_frame.pack(fill="x", pady=10)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=20)

        ttk.Button(button_frame, text="Run Simulation", command=self.run_simulation).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear Results", command=self.clear_results).pack(side="left", padx=5)

        result_frame = ttk.LabelFrame(main_frame, text="Results", padding=10)
        result_frame.pack(fill="both", expand=True, pady=10)

        self.result_text = tk.Text(result_frame, height=15, wrap="word", font=("Consolas", 10), bg="white")
        self.result_text.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(fill="y", side="right")
        self.result_text.config(yscrollcommand=scrollbar.set)

        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")
        status_bar.pack(side="bottom", fill="x")

    def generate_speed_inputs(self):
        for widget in self.speeds_frame.winfo_children():
            widget.destroy()

        try:
            n = int(self.runner_var.get())
            if n <= 1:
                messagebox.showerror("Invalid Input", "Number of runners must be greater than 1.")
                return

            self.speed_entries = []
            for i in range(n):
                label = ttk.Label(self.speeds_frame, text=f"Speed of Runner {i}:")
                label.grid(row=i, column=0, padx=5, pady=3, sticky="w")
                entry = ttk.Entry(self.speeds_frame, width=10)
                entry.grid(row=i, column=1, padx=5, pady=3, sticky="w")
                self.speed_entries.append(entry)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for runners.")

    def run_simulation(self):
        try:
            speeds = [float(entry.get()) for entry in self.speed_entries]
            n = len(speeds)

            if len(speeds) != n or any(speed <= 0 for speed in speeds):
                messagebox.showerror("Invalid Speeds", "Please enter valid positive speeds for all runners.")
                return

            self.result_text.delete(1.0, "end")
            self.status_var.set("Running simulation...")
            self.root.update_idletasks()

            comparisons = 0
            race_log = []

            for i in range(n):
                for j in range(i + 1, n):
                    comparisons += 1
                    if speeds[i] > speeds[j]:
                        winner = i
                    elif speeds[j] > speeds[i]:
                        winner = j
                    else:
                        winner = i  # if equal, take i as winner arbitrarily
                    race_log.append(f"Race {comparisons}: Runner {i} (Speed: {speeds[i]}) vs Runner {j} (Speed: {speeds[j]}) => Winner: Runner {winner}")

            fastest_index = speeds.index(max(speeds))

            self.result_text.insert("end", "--- Speeds ---\n")
            for i, spd in enumerate(speeds):
                self.result_text.insert("end", f"Runner {i}: Speed = {spd}\n")

            self.result_text.insert("end", "\n--- Race Logs ---\n")
            for log in race_log:
                self.result_text.insert("end", f"{log}\n")

            self.result_text.insert("end", f"\nTotal Comparisons: {comparisons} (Expected: {n*(n-1)//2})\n")
            self.result_text.insert("end", f"\nFastest Runner: Runner {fastest_index} with speed {speeds[fastest_index]} ✓\n")
            self.status_var.set("Simulation completed.")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter numeric values for all speeds.")
            self.status_var.set("Simulation failed.")

    def clear_results(self):
        self.result_text.delete(1.0, "end")
        self.status_var.set("Results cleared")

if __name__ == "__main__":
    root = tk.Tk()
    app = FastestRunnerApp(root)
    root.mainloop()
