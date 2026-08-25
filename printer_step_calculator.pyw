import tkinter as tk

# Calculate Inputs
def calculate(*args):
    try:
        # Inputs
        printer_start_offset = float(offset_var.get())
        move_distance = float(goal_var.get())
        printer_end_offset = float(printer_end_offset_var.get())

        # Calculate
        adjusted_goal = printer_end_offset - printer_start_offset
        difference = move_distance / adjusted_goal

        # Update labels
        result_label.config(
            text=f"Difference: {difference:}"
        )

        # Only calculate counts if an input exists
        if counts_var.get().strip():
            counts_per_unit = float(counts_var.get())
            final_count = difference * counts_per_unit

            count_label.config(
                text=f"New Counts Per Unit: {final_count:}"
            )
        else:
            count_label.config(
                text="New Counts Per Unit: --"
            )

    # If any errors, display NA
    except (ValueError, ZeroDivisionError):
        result_label.config(text="Calibration Factor: NA")
        count_label.config(text="New Counts Per Unit: NA")

# Create Window
window = tk.Tk()
window.title("Distance Calculator")
window.geometry("350x260")

# Text holders
goal_var = tk.StringVar()
offset_var = tk.StringVar(value="0")
printer_end_offset_var = tk.StringVar()
counts_var = tk.StringVar()

# Update whenever any input changes
goal_var.trace_add("write", calculate)
offset_var.trace_add("write", calculate)
printer_end_offset_var.trace_add("write", calculate)
counts_var.trace_add("write", calculate)

# Displays
tk.Label(window, text="Printer Start Offset:").pack()
tk.Entry(window, textvariable=offset_var).pack()

tk.Label(window, text="Move Distance:").pack()
tk.Entry(window, textvariable=goal_var).pack()

tk.Label(window, text="Printer End Offset:").pack()
tk.Entry(window, textvariable=printer_end_offset_var).pack()

result_label = tk.Label(window, text="Calibration Factor: --")
result_label.pack(pady=5)

tk.Label(window, text="Current Counts Per Unit:").pack()
tk.Entry(window, textvariable=counts_var).pack()

# Copyable New Cycles
def copy_count(event=None):
    value = count_label.cget("text").replace("New Counts Per Unit: ", "")

    if value != "--" and value != "NA":
        window.clipboard_clear()
        window.clipboard_append(value)
        window.update()

        copy_status.config(text="Copied!")

# New Count Label
count_label = tk.Label(
    window,
    text="New Counts Per Unit: --",
    cursor="hand2",
    fg="blue"
)
count_label.pack(pady=15)

# Left Click Text to copy
count_label.bind("<Button-1>", copy_count)

copy_status = tk.Label(window, text="")
copy_status.pack()

window.mainloop()
