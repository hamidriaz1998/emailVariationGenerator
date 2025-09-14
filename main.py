import os
import sys

from PyQt6.QtCore import Qt, QThread, QTimer, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from email_generator import generate_email_variations, save_variations_to_file


class ThemeManager:
    """Manages light and dark themes for the application"""

    @staticmethod
    def get_light_theme():
        return """
            QMainWindow {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #f5f7fa, stop: 1 #c3cfe2);
                color: #2c3e50;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cccccc;
                border-radius: 8px;
                margin-top: 1ex;
                padding-top: 10px;
                background-color: white;
                color: #2c3e50;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
                font-size: 14px;
            }
            QLineEdit {
                border: 2px solid #ddd;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: white;
                color: #2c3e50;
                selection-background-color: #3498db;
            }
            QLineEdit:focus {
                border-color: #3498db;
                background-color: #f8f9fa;
            }
            QTextEdit {
                border: 2px solid #ddd;
                border-radius: 6px;
                padding: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
                background-color: white;
                color: #2c3e50;
                selection-background-color: #3498db;
            }
            QCheckBox {
                font-size: 13px;
                spacing: 8px;
                color: #2c3e50;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 3px;
                border: 2px solid #bdc3c7;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #3498db;
                border-color: #3498db;
            }
            QLabel {
                color: #2c3e50;
                font-size: 13px;
            }
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                text-align: center;
                background-color: #ecf0f1;
                color: #2c3e50;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                          stop: 0 #3498db, stop: 1 #2980b9);
                border-radius: 6px;
            }
            QMenuBar {
                background-color: white;
                color: #2c3e50;
                border-bottom: 1px solid #ddd;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 4px 8px;
            }
            QMenuBar::item:selected {
                background-color: #3498db;
                color: white;
            }
            QMenu {
                background-color: white;
                color: #2c3e50;
                border: 1px solid #ddd;
            }
            QMenu::item:selected {
                background-color: #3498db;
                color: white;
            }
        """

    @staticmethod
    def get_dark_theme():
        return """
            QMainWindow {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #2c3e50, stop: 1 #1a252f);
                color: #ecf0f1;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #555555;
                border-radius: 8px;
                margin-top: 1ex;
                padding-top: 10px;
                background-color: #34495e;
                color: #ecf0f1;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #ecf0f1;
                font-size: 14px;
            }
            QLineEdit {
                border: 2px solid #555555;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: #2c3e50;
                color: #ecf0f1;
                selection-background-color: #3498db;
            }
            QLineEdit:focus {
                border-color: #3498db;
                background-color: #34495e;
            }
            QTextEdit {
                border: 2px solid #555555;
                border-radius: 6px;
                padding: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
                background-color: #2c3e50;
                color: #ecf0f1;
                selection-background-color: #3498db;
            }
            QCheckBox {
                font-size: 13px;
                spacing: 8px;
                color: #ecf0f1;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 3px;
                border: 2px solid #7f8c8d;
                background-color: #2c3e50;
            }
            QCheckBox::indicator:checked {
                background-color: #3498db;
                border-color: #3498db;
            }
            QLabel {
                color: #ecf0f1;
                font-size: 13px;
            }
            QProgressBar {
                border: 2px solid #7f8c8d;
                border-radius: 8px;
                text-align: center;
                background-color: #34495e;
                color: #ecf0f1;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                          stop: 0 #e74c3c, stop: 1 #c0392b);
                border-radius: 6px;
            }
            QMenuBar {
                background-color: #34495e;
                color: #ecf0f1;
                border-bottom: 1px solid #555555;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 4px 8px;
            }
            QMenuBar::item:selected {
                background-color: #e74c3c;
                color: white;
            }
            QMenu {
                background-color: #34495e;
                color: #ecf0f1;
                border: 1px solid #555555;
            }
            QMenu::item:selected {
                background-color: #e74c3c;
                color: white;
            }
        """

    @staticmethod
    def get_light_button_style():
        return """
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #4CAF50, stop: 1 #45a049);
                border: none;
                color: white;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
                min-height: 20px;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #5CBF60, stop: 1 #4CAF50);
            }
            QPushButton:pressed {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #3d8b40, stop: 1 #2e7d32);
            }
            QPushButton:disabled {
                background: #cccccc;
                color: #666666;
            }
        """

    @staticmethod
    def get_dark_button_style():
        return """
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #e74c3c, stop: 1 #c0392b);
                border: none;
                color: white;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
                min-height: 20px;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #ec7063, stop: 1 #e74c3c);
            }
            QPushButton:pressed {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #a93226, stop: 1 #922b21);
            }
            QPushButton:disabled {
                background: #555555;
                color: #888888;
            }
        """

    @staticmethod
    def get_secondary_button_style(is_dark=False):
        if is_dark:
            return """
                QPushButton {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #3498db, stop: 1 #2980b9);
                    border: none;
                    color: white;
                    padding: 8px 16px;
                    font-size: 12px;
                    border-radius: 6px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #5dade2, stop: 1 #3498db);
                }
            """
        else:
            return """
                QPushButton {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #3498db, stop: 1 #2980b9);
                    border: none;
                    color: white;
                    padding: 8px 16px;
                    font-size: 12px;
                    border-radius: 6px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #5dade2, stop: 1 #3498db);
                }
            """


class AnimatedButton(QPushButton):
    """Custom button with hover animations"""

    def __init__(self, text, parent=None, is_secondary=False):
        super().__init__(text, parent)
        self.is_secondary = is_secondary
        self.is_dark = False
        self.update_style()

    def update_style(self):
        if self.is_secondary:
            self.setStyleSheet(ThemeManager.get_secondary_button_style(self.is_dark))
        else:
            if self.is_dark:
                self.setStyleSheet(ThemeManager.get_dark_button_style())
            else:
                self.setStyleSheet(ThemeManager.get_light_button_style())

    def set_dark_mode(self, is_dark):
        self.is_dark = is_dark
        self.update_style()


class WorkerThread(QThread):
    """Worker thread for generating email variations"""

    finished = pyqtSignal(list)

    def __init__(self, email, include_hyphen_underscore, custom_keywords):
        super().__init__()
        self.email = email
        self.include_hyphen_underscore = include_hyphen_underscore
        self.custom_keywords = custom_keywords

    def run(self):
        variations = generate_email_variations(
            self.email, self.include_hyphen_underscore, self.custom_keywords
        )
        self.finished.emit(variations)


class EmailVariationsUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✉️ Email Variations Generator Pro")
        self.setGeometry(100, 100, 800, 700)
        self.setMinimumSize(600, 500)

        # Theme state
        self.is_dark_mode = False

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        main_widget.setLayout(layout)

        # Header section with title and theme toggle
        header_layout = QHBoxLayout()

        # Title
        self.title_label = QLabel("📧 Email Variations Generator")
        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 10px;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                margin-bottom: 10px;
            }
        """)
        header_layout.addWidget(self.title_label)

        # Theme toggle button
        self.theme_toggle_button = AnimatedButton("🌙 Dark Mode", is_secondary=True)
        self.theme_toggle_button.clicked.connect(self.toggle_theme)
        self.theme_toggle_button.setMaximumWidth(120)
        header_layout.addWidget(self.theme_toggle_button)

        layout.addLayout(header_layout)

        # Input section
        input_group = QGroupBox("📝 Input Configuration")
        input_layout = QVBoxLayout()
        input_group.setLayout(input_layout)

        # Email input
        email_layout = QHBoxLayout()
        email_label = QLabel("Email Address:")
        email_label.setMinimumWidth(120)
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("🔤 e.g., johnsmith@gmail.com")
        self.email_input.textChanged.connect(self.validate_input)
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.email_input)
        input_layout.addLayout(email_layout)

        # Options section
        options_layout = QVBoxLayout()
        self.hyphen_underscore_check = QCheckBox(
            "🔗 Include hyphen/underscore variations"
        )
        self.hyphen_underscore_check.setToolTip(
            "Generate variations with hyphens and underscores instead of dots"
        )
        options_layout.addWidget(self.hyphen_underscore_check)

        # Custom keywords input
        keywords_layout = QHBoxLayout()
        keywords_label = QLabel("Keywords:")
        keywords_label.setMinimumWidth(120)
        self.keywords_input = QLineEdit()
        self.keywords_input.setPlaceholderText(
            "🏷️ e.g., netflix,amazon,shop (leave blank for defaults)"
        )
        keywords_layout.addWidget(keywords_label)
        keywords_layout.addWidget(self.keywords_input)
        options_layout.addLayout(keywords_layout)

        input_layout.addLayout(options_layout)
        layout.addWidget(input_group)

        # Progress bar (initially hidden)
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setTextVisible(True)
        layout.addWidget(self.progress_bar)

        # Generate button
        self.generate_button = AnimatedButton("🚀 Generate Variations")
        self.generate_button.clicked.connect(self.generate_variations)
        self.generate_button.setEnabled(False)
        layout.addWidget(self.generate_button)

        # Output section
        output_group = QGroupBox("📋 Generated Variations")
        output_layout = QVBoxLayout()
        output_group.setLayout(output_layout)

        # Stats label
        self.stats_label = QLabel("No variations generated yet")
        self.stats_label.setStyleSheet("""
            QLabel {
                font-style: italic;
                padding: 5px;
            }
        """)
        output_layout.addWidget(self.stats_label)

        # Output text area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setPlaceholderText(
            "Generated email variations will appear here..."
        )
        output_layout.addWidget(self.output_area)

        layout.addWidget(output_group)

        # Save section
        save_group = QGroupBox("💾 Save Options")
        save_layout = QHBoxLayout()
        save_group.setLayout(save_layout)

        # File path input
        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText(
            "📁 Select output file path (optional - default: email_variations.txt)"
        )
        save_layout.addWidget(self.file_path_input)

        # Browse button
        self.browse_button = AnimatedButton("📂 Browse", is_secondary=True)
        self.browse_button.clicked.connect(self.browse_file)
        save_layout.addWidget(self.browse_button)

        # Save button
        self.save_button = AnimatedButton("💾 Save to File")
        self.save_button.clicked.connect(self.save_variations)
        self.save_button.setEnabled(False)
        save_layout.addWidget(self.save_button)

        layout.addWidget(save_group)

        # Store variations for saving
        self.variations = []
        self.worker = None

        # Animation timer for progress bar
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate_progress)
        self.animation_value = 0

        # Apply initial theme
        self.apply_theme()

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

        # Update button text
        if self.is_dark_mode:
            self.theme_toggle_button.setText("☀️ Light Mode")
        else:
            self.theme_toggle_button.setText("🌙 Dark Mode")

    def apply_theme(self):
        """Apply the current theme to all UI elements"""
        if self.is_dark_mode:
            self.setStyleSheet(ThemeManager.get_dark_theme())
            self.title_label.setStyleSheet("""
                QLabel {
                    font-size: 24px;
                    font-weight: bold;
                    color: #ecf0f1;
                    padding: 10px;
                    background: rgba(52, 73, 94, 0.8);
                    border-radius: 10px;
                    margin-bottom: 10px;
                }
            """)
            self.stats_label.setStyleSheet("""
                QLabel {
                    color: #bdc3c7;
                    font-style: italic;
                    padding: 5px;
                }
            """)
        else:
            self.setStyleSheet(ThemeManager.get_light_theme())
            self.title_label.setStyleSheet("""
                QLabel {
                    font-size: 24px;
                    font-weight: bold;
                    color: #2c3e50;
                    padding: 10px;
                    background: rgba(255, 255, 255, 0.8);
                    border-radius: 10px;
                    margin-bottom: 10px;
                }
            """)
            self.stats_label.setStyleSheet("""
                QLabel {
                    color: #7f8c8d;
                    font-style: italic;
                    padding: 5px;
                }
            """)

        # Update button themes
        self.generate_button.set_dark_mode(self.is_dark_mode)
        self.save_button.set_dark_mode(self.is_dark_mode)
        self.browse_button.set_dark_mode(self.is_dark_mode)
        self.theme_toggle_button.set_dark_mode(self.is_dark_mode)

    def validate_input(self):
        """Enable/disable generate button based on input validation"""
        email = self.email_input.text().strip()
        self.generate_button.setEnabled(bool(email and "@" in email))

    def browse_file(self):
        """Open file dialog to select save location"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Email Variations",
            "email_variations.txt",
            "Text Files (*.txt);;All Files (*)",
        )
        if file_path:
            self.file_path_input.setText(file_path)

    def animate_progress(self):
        """Animate progress bar during generation"""
        self.animation_value = (self.animation_value + 5) % 101
        self.progress_bar.setValue(self.animation_value)

    def generate_variations(self):
        """Generate email variations in a separate thread"""
        email = self.email_input.text().strip()
        include_hyphen_underscore = self.hyphen_underscore_check.isChecked()
        keywords_text = self.keywords_input.text().strip()
        custom_keywords = (
            [k.strip() for k in keywords_text.split(",")] if keywords_text else None
        )

        # Show progress bar and start animation
        self.progress_bar.setVisible(True)
        self.progress_bar.setFormat("Generating variations... %p%")
        self.animation_timer.start(50)
        self.generate_button.setEnabled(False)
        self.generate_button.setText("⏳ Generating...")

        # Start worker thread
        self.worker = WorkerThread(email, include_hyphen_underscore, custom_keywords)
        self.worker.finished.connect(self.on_variations_generated)
        self.worker.start()

    def on_variations_generated(self, variations):
        """Handle completion of variation generation"""
        # Stop animation and hide progress bar
        self.animation_timer.stop()
        self.progress_bar.setVisible(False)
        self.generate_button.setEnabled(True)
        self.generate_button.setText("🚀 Generate Variations")

        # Store variations
        self.variations = variations

        # Display results
        self.output_area.clear()
        if variations == ["Invalid email format"]:
            QMessageBox.critical(
                self,
                "❌ Error",
                "Invalid email format!\n\nPlease enter a valid email address.",
            )
            self.save_button.setEnabled(False)
            self.stats_label.setText("❌ Invalid email format")
            if self.is_dark_mode:
                self.stats_label.setStyleSheet(
                    "QLabel { color: #e74c3c; font-weight: bold; }"
                )
            else:
                self.stats_label.setStyleSheet(
                    "QLabel { color: #e74c3c; font-weight: bold; }"
                )
        else:
            # Display variations with numbering
            numbered_variations = [
                f"{i + 1:3d}. {var}" for i, var in enumerate(variations)
            ]
            self.output_area.setText("\n".join(numbered_variations))

            # Update stats
            self.stats_label.setText(
                f"✅ Generated {len(variations)} unique email variations"
            )
            if self.is_dark_mode:
                self.stats_label.setStyleSheet(
                    "QLabel { color: #2ecc71; font-weight: bold; }"
                )
            else:
                self.stats_label.setStyleSheet(
                    "QLabel { color: #27ae60; font-weight: bold; }"
                )

            self.save_button.setEnabled(True)

            # Show success animation
            self.show_success_message()

    def show_success_message(self):
        """Show a brief success message"""
        self.stats_label.setText(
            f"🎉 Successfully generated {len(self.variations)} variations!"
        )
        QTimer.singleShot(
            3000,
            lambda: self.stats_label.setText(
                f"✅ Generated {len(self.variations)} unique email variations"
            ),
        )

    def save_variations(self):
        """Save variations to file with custom path support"""
        if not self.variations:
            return

        # Get file path
        file_path = self.file_path_input.text().strip()
        if not file_path:
            file_path = "email_variations.txt"

        # Ensure directory exists
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except Exception as e:
                QMessageBox.critical(
                    self, "❌ Error", f"Failed to create directory:\n{str(e)}"
                )
                return

        try:
            # Save variations
            if file_path.endswith(".txt"):
                # Save as numbered list for text files
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("Email Variations Generated\n")
                    f.write("=" * 30 + "\n\n")
                    for i, variation in enumerate(self.variations, 1):
                        f.write(f"{i:3d}. {variation}\n")
                    f.write(f"\nTotal: {len(self.variations)} variations\n")
            else:
                # Save plain format for other file types
                save_variations_to_file(self.variations, file_path)

            # Show success message
            QMessageBox.information(
                self,
                "✅ Success",
                f"Successfully saved {len(self.variations)} variations to:\n{os.path.abspath(file_path)}",
            )

            # Update stats
            self.stats_label.setText(
                f"💾 Saved {len(self.variations)} variations to {os.path.basename(file_path)}"
            )

        except Exception as e:
            QMessageBox.critical(self, "❌ Error", f"Failed to save file:\n{str(e)}")


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Email Variations Generator Pro")
    app.setApplicationVersion("2.0")

    # Set application icon (if available)
    try:
        app.setWindowIcon(QIcon("icon.png"))
    except Exception:
        pass

    window = EmailVariationsUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
