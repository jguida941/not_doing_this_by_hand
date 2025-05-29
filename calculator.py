from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QComboBox
)
from collections import Counter
import sys

def prime_factors(n):
    i = 2
    factors = Counter()
    while i * i <= n:
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] += 1
    return factors

def gcd_by_factors(a, b):
    fa = prime_factors(a)
    fb = prime_factors(b)
    common = fa.keys() & fb.keys()
    gcd_factors = {p: min(fa[p], fb[p]) for p in common}
    result = 1
    for p, exp in gcd_factors.items():
        result *= p ** exp
    return gcd_factors, result

def lcm_by_factors(a, b):
    fa = prime_factors(a)
    fb = prime_factors(b)
    all_keys = fa.keys() | fb.keys()
    lcm_factors = {p: max(fa[p], fb[p]) for p in all_keys}
    result = 1
    for p, exp in lcm_factors.items():
        result *= p ** exp
    return lcm_factors, result

def pretty_print_factors(label, factors):
    return f"{label} = " + " · ".join([f"{p}^{e}" for p, e in sorted(factors.items())])

# Export factors in submission format: p1^e1 * p2^e2 * ...
def export_factors_to_submission_format(factors):
    return " * ".join([f"{p}^{e}" for p, e in sorted(factors.items())])

class GcdLcmApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GCD / LCM Calculator with Prime Factorization")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Create a QFrame container for styling/glow
        from PyQt6.QtWidgets import QFrame
        self.frame_container = QFrame()
        self.frame_container.setObjectName("frame_container")
        frame_container_layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.input_a = QLineEdit()
        self.input_a.setPlaceholderText("Enter first number")
        self.input_b = QLineEdit()
        self.input_b.setPlaceholderText("Enter second number")
        input_layout.addWidget(self.input_a)
        input_layout.addWidget(self.input_b)

        self.mode_select = QComboBox()
        self.mode_select.addItems(["GCD", "LCM"])

        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)

        self.calc_button = QPushButton("Compute")
        self.calc_button.clicked.connect(self.compute)

        # Add widgets to frame_container_layout instead of layout
        frame_container_layout.addLayout(input_layout)
        frame_container_layout.addWidget(self.mode_select)
        frame_container_layout.addWidget(self.calc_button)
        frame_container_layout.addWidget(self.result_output)
        self.frame_container.setLayout(frame_container_layout)

        layout.addWidget(self.frame_container)

        self.setStyleSheet("""
QWidget {
    background-color: #1c1c1e;
    color: white;
    font-size: 16px;
    border: 2px solid #ff453a;
    border-radius: 10px;
}

QFrame#frame_container {
    border: 2px solid #ff453a;
    border-radius: 10px;
    background-color: #1c1c1e;
    /* Glowing effect: use a colored border and (optionally) a gradient or shadow-like illusion */
    /* For more intense glow, can use outline or extra border layers if supported */
}

QLineEdit, QTextEdit {
    background-color: #2c2c2e;
    border: 1px solid #444;
    padding: 6px;
    color: white;
    border-radius: 6px;
}

QComboBox {
    background-color: #2c2c2e;
    border: 1px solid #444;
    padding: 4px;
    color: white;
    border-radius: 4px;
}

QPushButton {
    background-color: #1c1c1e;
    border: 2px solid #0a84ff;
    color: #0a84ff;
    font-weight: bold;
    padding: 8px 16px;
    border-radius: 8px;
    transition: all 0.3s ease-in-out;
}

QPushButton:hover {
    background-color: #0a84ff;
    color: black;
    border-color: #66aaff;
}

QPushButton:pressed {
    background-color: #0050a0;
    color: white;
    border-color: #003366;
}
        """)
        self.setLayout(layout)

    def compute(self):
        try:
            a = int(self.input_a.text())
            b = int(self.input_b.text())
            mode = self.mode_select.currentText()

            fa = prime_factors(a)
            fb = prime_factors(b)

            output = []
            output.append(pretty_print_factors(f"{a}", fa))
            output.append(pretty_print_factors(f"{b}", fb))

            if mode == "GCD":
                result_factors, value = gcd_by_factors(a, b)
                output.append(pretty_print_factors(f"GCD({a}, {b})", result_factors))
                output.append(f"GCD value: {value}")
                output.append("Submission format: " + export_factors_to_submission_format(result_factors))
            else:
                result_factors, value = lcm_by_factors(a, b)
                output.append(pretty_print_factors(f"LCM({a}, {b})", result_factors))
                output.append(f"LCM value: {value}")
                output.append("Submission format: " + export_factors_to_submission_format(result_factors))

            self.result_output.setText("\n".join(output))
        except ValueError:
            self.result_output.setText("Please enter valid integers.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GcdLcmApp()
    window.show()
    sys.exit(app.exec())