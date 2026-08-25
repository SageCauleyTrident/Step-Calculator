import tkinter as tk

# Calculate Inputs
def calculate(*args):
    try:
        # Inputs
        start_offset = float(offset_var.get())
        original_goal = float(goal_var.get())
        current = float(current_var.get())

        # Calculate
        adjusted_goal = original_goal + start_offset
        difference = adjusted_goal - current
        goal_difference = difference + original_goal

        # Check 0
        if goal_difference == 0:
            raise ZeroDivisionError

        # Final Calculation
        final_value = original_goal / goal_difference

        # Update labels
        result_label.config(
            text=f"Difference: {difference:}"
        )

        final_label.config(
            text=f"Final: {final_value:}"
        )

        # Only calculate counts if an input exists
        if counts_var.get().strip():
            counts_per_unit = float(counts_var.get())
            final_count = final_value * counts_per_unit

            count_label.config(
                text=f"New Counts Per Unit: {final_count:}"
            )
        else:
            count_label.config(
                text="New Counts Per Unit: --"
            )

    # If any errors, display NA
    except (ValueError, ZeroDivisionError):
        result_label.config(text="Difference: NA")
        final_label.config(text="Final: NA")
        count_label.config(text="New Counts Per Unit: NA")

# Create Window
window = tk.Tk()
window.title("Distance Calculator")
window.geometry("350x350")

# Text holders
goal_var = tk.StringVar()
offset_var = tk.StringVar(value="0")
current_var = tk.StringVar()
counts_var = tk.StringVar()

# Update whenever any input changes
goal_var.trace_add("write", calculate)
offset_var.trace_add("write", calculate)
current_var.trace_add("write", calculate)
counts_var.trace_add("write", calculate)

# Displays
tk.Label(window, text="Start Offset:").pack()
tk.Entry(window, textvariable=offset_var).pack()

tk.Label(window, text="Goal Distance:").pack()
tk.Entry(window, textvariable=goal_var).pack()

tk.Label(window, text="Current Distance:").pack()
tk.Entry(window, textvariable=current_var).pack()

result_label = tk.Label(window, text="Difference: --")
result_label.pack(pady=5)

final_label = tk.Label(window, text="Final: --")
final_label.pack(pady=15)

tk.Label(window, text="Counts Per Unit:").pack()
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
