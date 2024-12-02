import sys
import re
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                            QVBoxLayout, QLabel, QProgressBar, QFileDialog,
                            QMessageBox)
from PyQt6.QtCore import Qt
from googletrans import Translator

class SRTTranslator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.selected_file = None
        
    def initUI(self):
        self.setWindowTitle('SRT Translator to Greek')
        self.setGeometry(100, 100, 500, 300)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Create widgets
        self.select_button = QPushButton('Select SRT File', self)
        self.select_button.clicked.connect(self.select_file)
        
        self.file_label = QLabel('No file selected', self)
        self.file_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.progress = QProgressBar(self)
        self.progress.setMaximum(100)
        self.progress.setMinimum(0)
        
        self.translate_button = QPushButton('Translate to Greek', self)
        self.translate_button.clicked.connect(self.translate_srt)
        self.translate_button.setEnabled(False)
        
        self.status_label = QLabel('', self)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add widgets to layout
        layout.addWidget(self.select_button)
        layout.addWidget(self.file_label)
        layout.addWidget(self.progress)
        layout.addWidget(self.translate_button)
        layout.addWidget(self.status_label)
        
        # Add stretch to center widgets vertically
        layout.addStretch()
        
    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select SRT File",
            "",
            "SRT files (*.srt);;All Files (*)"
        )
        
        if filename:
            self.selected_file = filename
            self.file_label.setText(f"Selected: {filename}")
            self.translate_button.setEnabled(True)
            
    def translate_srt(self):
        if not self.selected_file:
            return
            
        try:
            # Create translator instance
            translator = Translator()
            
            # Read the original file
            with open(self.selected_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Parse the SRT content
            pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3})\n((?:.*\n)*?\n)'
            subtitles = re.findall(pattern, content + '\n')
            total_subs = len(subtitles)
            
            # Prepare the output file name
            output_filename = self.selected_file[:-4] + '_greek.srt'
            
            with open(output_filename, 'w', encoding='utf-8') as out_file:
                for idx, (number, timestamp, text) in enumerate(subtitles):
                    # Update progress
                    progress = int((idx + 1) / total_subs * 100)
                    self.progress.setValue(progress)
                    QApplication.processEvents()  # Keep UI responsive
                    
                    # Translate the text (removing any newlines for translation)
                    text_to_translate = text.strip()
                    if text_to_translate:
                        translated_text = translator.translate(
                            text_to_translate,
                            dest='el'  # 'el' is the language code for Greek
                        ).text
                    else:
                        translated_text = ""
                    
                    # Write to output file
                    out_file.write(f"{number}\n")
                    out_file.write(f"{timestamp}\n")
                    out_file.write(f"{translated_text}\n\n")
            
            self.status_label.setText(f"Translation completed! Saved as: {output_filename}")
            QMessageBox.information(
                self,
                "Success",
                f"Translation completed!\nSaved as: {output_filename}"
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An error occurred: {str(e)}"
            )
        finally:
            self.progress.setValue(0)

def main():
    app = QApplication(sys.argv)
    translator = SRTTranslator()
    translator.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
