import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton, QComboBox, QFrame, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

class PartitionTool(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Creality K1 Series Partition Tool")
        self.setMinimumWidth(500)
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; }
            QLabel { color: #e0e0e0; font-size: 14px; }
            QLineEdit { 
                background-color: #2d2d2d; 
                color: white; 
                border: 1px solid #3f3f3f; 
                border-radius: 4px; 
                padding: 8px; 
            }
            QLineEdit:focus { border: 1px solid #3d92ff; }
            QComboBox { 
                background-color: #2d2d2d; 
                color: white; 
                padding: 8px; 
                border: 1px solid #3f3f3f; 
            }
            QPushButton { 
                background-color: #3d92ff; 
                color: white; 
                font-weight: bold; 
                border-radius: 4px; 
                padding: 12px; 
                margin-top: 10px;
            }
            QPushButton:hover { background-color: #529fff; }
            QPushButton:pressed { background-color: #2a75d6; }
            #header { font-size: 18px; font-weight: bold; color: #3d92ff; }
            QFrame#card { 
                background-color: #252525; 
                border-radius: 8px; 
                padding: 15px; 
            }
        """)

        # Main Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Header
        header = QLabel("Partition File Generator")
        header.setObjectName("header")
        layout.addWidget(header)

        # Content Card
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        
        # Model Selection
        card_layout.addWidget(QLabel("Printer Model"))
        self.model_combo = QComboBox()
        self.model_combo.addItems(["K1", "K1C", "K1 Max"])
        card_layout.addWidget(self.model_combo)

        # Serial Number Input
        card_layout.addWidget(QLabel("Serial Number (14 Hex Digits)"))
        self.sn_input = QLineEdit()
        self.sn_input.setPlaceholderText("e.g. CB153CBA4BC8A6")
        self.sn_input.setMaxLength(14)
        card_layout.addWidget(self.sn_input)

        # MAC Address Input
        card_layout.addWidget(QLabel("MAC Address (12 Hex Digits)"))
        self.mac_input = QLineEdit()
        self.mac_input.setPlaceholderText("e.g. EB850E76F140")
        self.mac_input.setMaxLength(12)
        card_layout.addWidget(self.mac_input)

        # Board Code (Optional/Default)
        card_layout.addWidget(QLabel("Board Code"))
        self.board_input = QLineEdit()
        self.board_input.setText("CR4CU220812S12")
        card_layout.addWidget(self.board_input)

        layout.addWidget(card)

        # Action Button
        self.generate_btn = QPushButton("Generate .img Files")
        self.generate_btn.clicked.connect(self.generate_files)
        layout.addWidget(self.generate_btn)

        # Status Footer
        self.status_label = QLabel("Files will be saved to the current directory.")
        self.status_label.setStyleSheet("font-size: 11px; color: #888;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

    def generate_files(self):
        sn = self.sn_input.text().strip().upper()
        mac = self.mac_input.text().strip().upper()
        model = self.model_combo.currentText()
        board = self.board_input.text().strip()

        # Validation
        if len(sn) != 14 or len(mac) != 12:
            QMessageBox.critical(self, "Error", "Invalid Length!\nSN must be 14 chars, MAC must be 12 chars.")
            return

        try:
            # 1. Generate ota.img
            # "ota:kernel\n\n"
            ota_content = "ota:kernel\n\n"
            with open("ota.img", "wb") as f:
                f.write(ota_content.encode('ascii'))

            # 2. Generate sn_mac.img
            # Format: SN;MAC;MODEL;BOARD;;;;;
            sn_mac_content = f"{sn};{mac};{model};{board};;;;;"
            with open("sn_mac.img", "wb") as f:
                f.write(sn_mac_content.encode('ascii'))

            QMessageBox.information(self, "Success", f"Files generated successfully!\n\nSaved to: {os.getcwd()}")
        
        except Exception as e:
            QMessageBox.critical(self, "System Error", f"Could not write files: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PartitionTool()
    window.show()
    sys.exit(app.exec())
