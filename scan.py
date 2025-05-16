import tkinter as tk
from tkinter import ttk, messagebox

class FastestRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fastest Runner (Efficient Linear Scan)")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Set theme
        style = ttk.Style()
        style.theme_use("clam")

        # Configure colors
        self.bg_color = "#f5f5f5"
        self.accent_color = "#4a7abc"
        self.root.configure(bg=self.bg_color)

        style.configure("TFrame", background=self.bg_color)
        style.configure("TButton",
                        background=self.accent_color,
                        foreground="white",
                        font=("Arial", 10, "bold"),
                        padding=5)
        style.configure("TLabel",
                        background=self.bg_color,
                        font=("Arial", 10))
        style.configure("Header.TLabel",
                        background=self.bg_color,
                        font=("Arial", 14, "bold"))

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)

        # Title
        title_label = ttk.Label(main_frame,
                                text="Fastest Runner Finder (O(n) Scan)",
                                style="Header.TLabel")
        title_label.pack(pady=(0, 20))

        # Input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill="x", pady=10)

        # Speeds
        ttk.Label(input_frame, text="Runner Speeds (comma-separated, in m/s):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.speed_var = tk.StringVar()
        speed_entry = ttk.Entry(input_frame, textvariable=self.speed_var, width=40)
        speed_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Distance
        ttk.Label(input_frame, text="Race Distance (in meters):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.distance_var = tk.StringVar()
        distance_entry = ttk.Entry(input_frame, textvariable=self.distance_var, width=40)
        distance_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=20)

        simulate_btn = ttk.Button(button_frame, text="Find Fastest", command=self.find_fastest)
        simulate_btn.pack(side="left", padx=5)

        clear_btn = ttk.Button(button_frame, text="Clear Results", command=self.clear_results)
        clear_btn.pack(side="left", padx=5)

        # Results area
        result_frame = ttk.LabelFrame(main_frame, text="Results", padding=10)
        result_frame.pack(fill="both", expand=True, pady=10)

        self.result_text = tk.Text(result_frame, height=15, wrap="word",
                                   font=("Consolas", 10), bg="white")
        self.result_text.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(fill="y", side="right")
        self.result_text.config(yscrollcommand=scrollbar.set)

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var,
                               relief="sunken", anchor="w")
        status_bar.pack(side="bottom", fill="x")

    def find_fastest(self):
        try:
            self.result_text.delete(1.0, "end")
            self.status_var.set("Running scan...")
            self.root.update_idletasks()

            # Get and parse speeds
            raw_input = self.speed_var.get().strip()
            distance_input = self.distance_var.get().strip()

            if not raw_input:
                raise ValueError("No runner speeds provided")

            if not distance_input:
                raise ValueError("Race distance is required")

            speed_list = [float(x.strip()) for x in raw_input.split(",") if x.strip()]
            distance = float(distance_input)

            if len(speed_list) < 2:
                raise ValueError("At least 2 runners are required")
            if distance <= 0:
                raise ValueError("Distance must be a positive number")

            # Find max speed and its index
            max_speed = speed_list[0]
            fastest_idx = 0

            for i in range(1, len(speed_list)):
                if speed_list[i] > max_speed:
                    max_speed = speed_list[i]
                    fastest_idx = i

            # Display results
            self.result_text.insert("end", f"Race Distance: {distance} meters\n")
            self.result_text.insert("end", f"Runner Speeds (m/s) and Time (s):\n")

            for i, speed in enumerate(speed_list):
                time_taken = distance / speed
                self.result_text.insert("end", f"Runner #{i} - {speed} m/s - Time: {time_taken:.2f} seconds\n")

            self.result_text.insert("end", f"\nFastest Runner: Runner #{fastest_idx} with speed {max_speed} m/s\n")
            fastest_time = distance / max_speed
            self.result_text.insert("end", f"Time Taken: {fastest_time:.2f} seconds\n")
            self.result_text.insert("end", f"Total Runners: {len(speed_list)}\n")
            self.result_text.insert("end", f"Time Complexity: O(n)\n")
            self.result_text.insert("end", f"Space Complexity: O(n)\n")

            self.status_var.set("Scan completed successfully.")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            self.status_var.set("Error in scan")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            self.status_var.set("Error in scan")

    def clear_results(self):
        self.result_text.delete(1.0, "end")
        self.status_var.set("Results cleared")


if __name__ == "__main__":
    root = tk.Tk()
    app = FastestRunnerApp(root)
    root.mainloop()
