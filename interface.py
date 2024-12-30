from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QLabel, QFileDialog
from PySide6.QtGui import QFont, QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CRUD Interface")
        self.setGeometry(100, 100, 800, 600)

        # Create buttons
        self.create_button = QPushButton("Create")
        self.update_button = QPushButton("Update")
        self.delete_button = QPushButton("Delete")
        self.edit_button = QPushButton("Edit")
        self.image_button = QPushButton("Image")

        # Set button styles
        button_font = QFont("Arial", 14)
        self.create_button.setFont(button_font)
        self.update_button.setFont(button_font)
        self.delete_button.setFont(button_font)
        self.edit_button.setFont(button_font)
        self.image_button.setFont(button_font)

        # Apply CSS styles
        self.create_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;")
        self.update_button.setStyleSheet("background-color: #2196F3; color: white; padding: 10px; border-radius: 5px;")
        self.delete_button.setStyleSheet("background-color: #f44336; color: white; padding: 10px; border-radius: 5px;")
        self.edit_button.setStyleSheet("background-color: #FFC107; color: white; padding: 10px; border-radius: 5px;")
        self.image_button.setStyleSheet("background-color: #9C27B0; color: white; padding: 10px; border-radius: 5px;")

        # Set up button layout
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.image_button)
        button_layout.addStretch()

        # Create log box
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setFont(QFont("Courier", 12))
        self.log_box.setStyleSheet("background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;")

        # Create label
        self.label = QLabel("Logs:")
        self.label.setFont(QFont("Arial", 14))
        self.label.setStyleSheet("padding: 10px;")

        # Create image label
        self.image_label = QLabel()
        self.image_label.setStyleSheet("padding: 10px;")
        self.image_label.setAlignment(Qt.AlignCenter)

        # Set up right layout
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.label)
        right_layout.addWidget(self.log_box)
        right_layout.addWidget(self.image_label)

        # Set up main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(right_layout)

        # Set up central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Connect button signals to slots
        self.create_button.clicked.connect(self.create_action)
        self.update_button.clicked.connect(self.update_action)
        self.delete_button.clicked.connect(self.delete_action)
        self.edit_button.clicked.connect(self.edit_action)
        self.image_button.clicked.connect(self.show_image)

    def create_action(self):
        self.log_box.append("Create button clicked!")

    def update_action(self):
        self.log_box.append("Update button clicked!")

    def delete_action(self):
        self.log_box.append("Delete button clicked!")

    def edit_action(self):
        self.log_box.append("Edit button clicked!")

    def show_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=Qt.KeepAspectRatio))
            self.log_box.append(f"Image loaded: {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())