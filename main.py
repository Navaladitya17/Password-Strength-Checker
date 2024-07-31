import re
import tkinter as tk

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    if re.search(" ~ ", password):  # Very strong character check
        score += 1

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    else:
        return "Weak"

def evaluate_password():
    password = entry.get()
    strength = check_password_strength(password)
    result_label.config(text=f"Password strength: {strength}")

    # Start animation based on strength
    if strength == "Very Strong":
        animate_color(result_label, "#000080")  # Dark blue for Very Strong
        stop_blinking()
    elif strength == "Strong":
        animate_color(result_label, "#00FF00")  # Green for Strong
        stop_blinking()
    elif strength == "Moderate":
        animate_color(result_label, "#FFFF00")  # Yellow for Moderate
        stop_blinking()
    else:
        animate_color(result_label, "#FF0000")  # Red for Weak
        start_blinking()

def animate_color(widget, target_color, steps=20):
    start_color = widget.cget("bg")
    start_rgb = widget.winfo_rgb(start_color)
    target_rgb = widget.winfo_rgb(target_color)

    r_step = (target_rgb[0] - start_rgb[0]) // steps
    g_step = (target_rgb[1] - start_rgb[1]) // steps
    b_step = (target_rgb[2] - start_rgb[2]) // steps

    def do_step(step):
        if step > steps:
            return
        r = start_rgb[0] + r_step * step
        g = start_rgb[1] + g_step * step
        b = start_rgb[2] + b_step * step
        new_color = f'#{r // 256:02x}{g // 256:02x}{b // 256:02x}'
        widget.config(bg=new_color)
        widget.after(50, do_step, step + 1)

    do_step(0)

def start_blinking():
    alert_label.config(text="Your password is weak! Please use a stronger password.")
    blink()

def stop_blinking():
    alert_label.config(text="")
    if 'blink_id' in app.__dict__:
        app.after_cancel(app.blink_id)

def blink():
    current_color = alert_label.cget("fg")
    next_color = "red" if current_color == "white" else "white"
    alert_label.config(fg=next_color)
    app.blink_id = app.after(500, blink)

app = tk.Tk()
app.title("Password Strength Checker")

tk.Label(app, text="Enter your password:").pack()
entry = tk.Entry(app, show="*")
entry.pack()
tk.Button(app, text="Check", command=evaluate_password).pack()
result_label = tk.Label(app, text="Password strength:", bg="white")
result_label.pack()
alert_label = tk.Label(app, text="", fg="red")
alert_label.pack()

app.mainloop()
