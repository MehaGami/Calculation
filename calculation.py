import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

class Calculation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculation")
        self.resize(400, 300)

        self.label = QLabel("")
        self.label_number1 = QLabel("First number:")
        self.label_number2 = QLabel("Second number:")
        self.label_operation = QLabel("Operation (+, -, *, /):")
        
        self.line_number1 = QLineEdit()
        self.line_number1.setFixedWidth(200)  

        self.line_number2 = QLineEdit()
        self.line_number2.setFixedWidth(200)  

        self.line_operation = QLineEdit()
        self.line_operation.setFixedWidth(200)
        
        self.button = QPushButton("Result")

        row1_layout = QHBoxLayout()
        row1_layout.addWidget(self.label_number1)
        row1_layout.addWidget(self.line_number1)

        row2_layout = QHBoxLayout()
        row2_layout.addWidget(self.label_number2)
        row2_layout.addWidget(self.line_number2)

        row3_layout = QHBoxLayout()
        row3_layout.addWidget(self.label_operation)
        row3_layout.addWidget(self.line_operation)

        layout = QVBoxLayout()
        layout.addLayout(row1_layout)
        layout.addLayout(row2_layout)
        layout.addLayout(row3_layout)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        layout.addWidget(self.label)
        layout.setAlignment(self.label, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(self.button, Qt.AlignmentFlag.AlignCenter) 

        self.setLayout(layout)

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        try:
            number1_text = self.line_number1.text()
            if not number1_text.isdigit():
                raise ValueError("First input is not an integer.")
            number1 = int(number1_text)
    
            number2_text = self.line_number2.text()
            if not number2_text.isdigit():
                raise ValueError("Second input is not an integer.")
            number2 = int(number2_text)

            operation = self.line_operation.text().strip()
            if operation not in ["+", "-", "*", "/"]:
                raise ValueError("Invalid operation(use +, -, *, or /.)")
            
            result = self.calculate(number1, number2, operation)
            self.label.setText(f"Result: {result}")
            self.label.setStyleSheet("""
                color: white;
                background-color: #4CAF50;  
                border: 2px solid #388E3C; 
                border-radius: 10px;  
                padding: 15px;
                font-weight: bold;
            """)
 
        except ValueError as e:
            self.label.setText(f"Error: {e}")
            self.label.setStyleSheet("""
                color: white;
                background-color: #F44336;  
                border: 2px solid #D32F2F; 
                border-radius: 10px;  
                padding: 15px;
                font-weight: bold;
            """)
        except Exception as e:
            self.label.setText(f"Unexpected error: {e}")
            self.label.setStyleSheet("""
                color: white;
                background-color: #F44336; 
                border: 2px solid #D32F2F; 
                border-radius: 10px;  
                padding: 15px;
                font-weight: bold;
            """)
            
    def calculate (self, number1, number2, operation):
        match operation:
            case "+" :
                result = number1 + number2
            case "-" :
                result = number1 - number2
            case "*" :
                result = number1 * number2
            case "/" : 
                result = number1 / number2
        return result

app = QApplication(sys.argv)
window = Calculation()
window.show()
sys.exit(app.exec())


