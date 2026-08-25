import tkinter as tk

def calculate(*args):
    try:
        start_offset = float(offset_var.get())
        move_distance = float(goal_var.get())
        end_offset = float(printer_end_offset_var.get())

        adjusted_distance = end_offset - start_offset
        calibration_factor = move_distance / adjusted_distance

        result_label.config(
            text=f"Calibration Factor: {calibration_factor:.4f}"
        )

        if counts_var.get().strip():
            counts = float(counts_var.get())
            new_counts = calibration_factor * counts
            count_label.config(
                text=f"New Counts Per Unit: {new_counts:.4f}"
            )
        else:
            count_label.config(text="New Counts Per Unit: --")

    except (ValueError, ZeroDivisionError):
        result_label.config(text="Calibration Factor: NA")
        count_label.config(text="New Counts Per Unit: NA")

def copy_count(event=None):
    value = count_label.cget("text").replace("New Counts Per Unit: ", "")

    if value not in ("--", "NA"):
        window.clipboard_clear()
        window.clipboard_append(value)
        window.update()
        copy_status.config(text="Copied!")

# Window
window = tk.Tk()
window.title("Distance Calculator")
window.geometry("350x260")

# Variables
offset_var = tk.StringVar(value="0")
goal_var = tk.StringVar()
printer_end_offset_var = tk.StringVar()
counts_var = tk.StringVar()

# Inputs
inputs = [
    ("Printer Start Offset:", offset_var),
    ("Move Distance:", goal_var),
    ("Printer End Offset:", printer_end_offset_var),
    ("Current Counts Per Unit:", counts_var),
]

for label_text, variable in inputs:
    tk.Label(window, text=label_text).pack()
    tk.Entry(window, textvariable=variable).pack()

# Results
result_label = tk.Label(window, text="Calibration Factor: --")
result_label.pack(pady=5)

count_label = tk.Label(
    window,
    text="New Counts Per Unit: --",
    cursor="hand2",
    fg="blue"
)
count_label.pack()

count_label.bind("<Button-1>", copy_count)

copy_status = tk.Label(window, text="")
copy_status.pack()

# Recalculate whenever an input changes
for variable in (offset_var, goal_var, printer_end_offset_var, counts_var):
    variable.trace_add("write", calculate)

window.mainloop()