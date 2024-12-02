# SRT Translator

A desktop application that translates SRT subtitle files from any language to Greek. Built with PyQt6 for a user-friendly interface and Google Translate API for translations.

## Features

- Simple and intuitive graphical user interface
- Select and translate SRT files with a few clicks
- Progress bar to track translation progress
- Automatic detection of source language
- Creates a new file with "_greek" suffix for translated subtitles
- Preserves original SRT timing and formatting

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PyQt6
- googletrans 3.1.0a0

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/srt-translator.git
cd srt-translator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python srt_translator.py
```

2. Click "Select SRT File" to choose your subtitle file
3. Click "Translate to Greek" to start the translation
4. A new file will be created in the same directory as your original file, with "_greek" added to the filename

## Notes

- The application uses Google Translate API through the `googletrans` library
- Internet connection is required for translation
- Translation quality depends on Google Translate's capabilities
- The application preserves all timing information from the original subtitles

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
