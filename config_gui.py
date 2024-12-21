import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QWidget, QMessageBox
)
CONFIG_FILE = os.path.expanduser("~/.fa2en_config")
DEFAULT_MAPPING = (
    "ض:q|ص:w|ث:e|ق:r|ف:t|غ:y|ع:u|ه:i|خ:o|ح:p|ج:[|چ:]|پ:\\|ش:a|س:s|ی:d|"
    "ب:f|ل:g|ا:h|ت:j|ن:k|م:l|ک:;|گ:'|ظ:z|ط:x|ز:c|ر:v|ذ:b|د:n|ئ:m|و:,"
)

class MappingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyboard Mapping Editor")
        
        # Default mapping loaded as dictionary
        self.mapping = self.load_mapping_from_config() or self.parse_mapping(DEFAULT_MAPPING)
        
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()

        # Table for mapping
        self.table = QTableWidget(len(self.mapping), 2)
        self.table.setHorizontalHeaderLabels(["Persian", "English"])
        layout.addWidget(self.table)

        # Load mapping into the table
        self.load_mapping_to_table()

        # Buttons
        self.save_button = QPushButton("Save Mapping")
        self.save_button.clicked.connect(self.save_mapping_to_config)
        layout.addWidget(self.save_button)

        self.reset_button = QPushButton("Reset to Default")
        self.reset_button.clicked.connect(self.reset_to_default)
        layout.addWidget(self.reset_button)

        # Main widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def parse_mapping(self, mapping_str):
        """Parse the mapping string into a dictionary."""
        pairs = mapping_str.split('|')
        mapping = {}
        for pair in pairs:
            if ':' in pair:
                k, v = pair.split(':')
                mapping[k] = v
        return mapping

    def generate_mapping_string(self):
        """Generate a string from the current mapping."""
        return '|'.join(f"{k}:{v}" for k, v in self.mapping.items())

    def load_mapping_to_table(self):
        """Load mapping into the table."""
        self.table.setRowCount(len(self.mapping))
        for row, (fa, en) in enumerate(self.mapping.items()):
            self.table.setItem(row, 0, QTableWidgetItem(fa))
            self.table.setItem(row, 1, QTableWidgetItem(en))

    def update_mapping_from_table(self):
        """Update the mapping dictionary based on the table's content."""
        self.mapping.clear()
        for row in range(self.table.rowCount()):
            fa = self.table.item(row, 0)
            en = self.table.item(row, 1)
            if fa and en:
                self.mapping[fa.text()] = en.text()

    def load_mapping_from_config(self):
        """Load mapping from the configuration file."""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as file:
                    content = file.read().strip()
                    return self.parse_mapping(content)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load config: {e}")
        return None

    def save_mapping_to_config(self):
        """Save current mapping into the configuration file."""
        self.update_mapping_from_table()
        try:
            with open(CONFIG_FILE, "w") as file:
                file.write(self.generate_mapping_string())
            QMessageBox.information(self, "Success", "Mapping saved successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save config: {e}")

    def reset_to_default(self):
        """Reset mapping to default values."""
        self.mapping = self.parse_mapping(DEFAULT_MAPPING)
        self.load_mapping_to_table()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MappingApp()
    window.show()
    sys.exit(app.exec_())
