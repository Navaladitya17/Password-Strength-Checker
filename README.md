# My Project on Password Strength checker 
# main.py :- 
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

    if score == 4:
        return "Very Strong"
    elif score == 3:
        return "Strong"
    elif score == 2:
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

# pwd.html :-
 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Password Strength Checker</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #000000;
        color: #ffffff;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        text-align: center;
        overflow: hidden; /* Prevent scrollbars */
    }
    .wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
    }
    .main-message {
        font-size: 36px; /* for the main message */
        color: #ffffff;
        margin-bottom: 20px; /* Space between the message and container */
        animation: blink 1s infinite; /* Blinking effect */
        font-family: 'Verdana', sans-serif;
    }
    .container {
        position: relative;
        background-color: #ffffff; /* Container background color (white) */
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        width: 350px;
        text-align: center;
        transition: background-color 0.3s;
    }
    .container::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .weak::before {
        background-color: rgba(255, 0, 0, 0.2);
    }
    .moderate::before {
        background-color: rgba(255, 255, 0, 0.2);
    }
    .strong::before {
        background-color: rgba(0, 255, 0, 0.2);
    }
    .very-strong::before {
        background-color: rgba(0, 0, 128, 0.2);
    }
    h2 {
        margin-bottom: 20px;
        color: #000000; /* Heading color (black) */
        font-size: 24px; /* Increased font size for the heading */
        position: relative; /* Ensure z-index works correctly */
    }
    .message {
        font-size: 18px; /* For the message */
        font-weight: bold;
        margin-bottom: 20px; /* Add some bottom margin for spacing */
        text-transform: uppercase;
    }
    input[type="password"] {
        width: calc(100% - 40px);
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 16px;
    }
    button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }
    button:hover {
        background-color: #45a049;
    }
    .result {
        margin-top: 20px;
        font-size: 24px;
        font-weight: bold;
        transition: color 0.3s, transform 0.3s;
        position: relative; /* Ensure z-index works correctly */
    }
    .result.weak {
        color: red; /* for weak result */
    }
    .result.moderate {
        color: yellow; /* for moderate result */
    }
    .result.strong {
        color: green; /* for strong result */
    }
    .result.very-strong {
        color: navy; /* for very strong result */
    }
    .alert {
        color: red;
        font-weight: bold;
        margin-top: 10px;
        font-size: 14px;
        animation: blink 1s infinite;
        display: none;
    }
    @keyframes blink {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0;
        }
    }
</style>
</head>
<body>
    <div class="wrapper">
        <div class="main-message">HERE YOU CAN CHECK YOUR PASSWORD STRENGTH</div>
        <div class="container" id="container">
            <h2>Password Strength Checker</h2>
            <p class="message">HERE IS YOUR PASSWORD STRENGTH:</p>
            <input type="password" id="password" placeholder="Enter your password...">
            <br>
            <button onclick="checkPassword()">Check</button>
            <p class="result" id="result"></p>
            <p class="alert" id="alert">Your password is weak! Please use a stronger password.</p>
        </div>
    </div>

    <script>
        function checkPassword() {
            var password = document.getElementById("password").value;
            var strength = "";
            var alertElement = document.getElementById("alert");

            // Perform simple check (length check)
            if (password.length < 8) {
                strength = "Weak";
                animateResult("weak");
                showAlert();
            } else {
                // Check password complexity
                if (/[a-z]/.test(password) && /[A-Z]/.test(password) && /\d/.test(password) && /[!@#$%^&*(),.?":{}|<>]/.test(password)) {
                    strength = "Very Strong";
                    animateResult("very-strong");
                    hideAlert();
                } else if (/[a-z]/.test(password) && /[A-Z]/.test(password) && /\d/.test(password)) {
                    strength = "Strong";
                    animateResult("strong");
                    hideAlert();
                } else if (/[a-zA-Z]/.test(password) && /\d/.test(password)) {
                    strength = "Moderate";
                    animateResult("moderate");
                    hideAlert();
                } else {
                    strength = "Weak";
                    animateResult("weak");
                    showAlert();
                }
            }

            var resultElement = document.getElementById("result");
            resultElement.textContent = strength;
            resultElement.className = "result " + strength.toLowerCase().replace(" ", "-");

            var container = document.getElementById("container");
            container.className = "container " + strength.toLowerCase().replace(" ", "-");
        }

        function showAlert() {
            var alertElement = document.getElementById("alert");
            alertElement.style.display = "block";
        }

        function hideAlert() {
            var alertElement = document.getElementById("alert");
            alertElement.style.display = "none";
        }

        function animateResult(strength) {
            var resultElement = document.getElementById("result");

            // Reset animation classes
            resultElement.classList.remove("very-strong", "strong", "moderate", "weak");

            // Trigger reflow to restart animation
            void resultElement.offsetWidth;

            // Apply animation class
            resultElement.classList.add(strength);
        }
    </script>
</body>
</html>
