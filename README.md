Here's a comprehensive README.md for your project:

```markdown
# FA2EN - Persian to English Text Converter 🔄

[![Bash Script](https://img.shields.io/badge/language-bash-green.svg)](https://www.gnu.org/software/bash/)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A powerful tool for converting Persian text to English and vice versa, with customizable keyboard mapping support.

## 🌟 Features

- 🔄 Bidirectional text conversion (Persian ↔️ English)
- ⚙️ Customizable keyboard mapping
- 🎯 Interactive mode for real-time conversion
- 🛠️ GUI configuration tool
- 📦 Backup and restore configuration
- ✅ Configuration validation

## 🚀 Installation

### Prerequisites

- Python 3.6+
- PyQt5 (for GUI configuration tool)
- Bash shell

### Basic Installation

```bash
# Clone the repository
git clone https://github.com/MG-530/fa2en.git

# Navigate to the project directory
cd fa2en

# Make the script executable
chmod +x fa2en.sh

# Optional: Add to PATH for system-wide access
sudo ln -s "$(pwd)/fa2en.sh" /usr/local/bin/fa2en
```

## 🎮 Usage

### Command Line Interface
Bash Script (fa2en.sh)

    Convert text: Automatically convert text using the specified mapping.
    Edit configuration: Open and modify the mapping file in your preferred editor.
    Validate configuration: Ensure the config file format is correct.
    Test mapping: Quickly test the mapping in the terminal.
    Interactive mode: Continuously input and convert text until exited.
    Backup configuration: Create a timestamped backup of the mapping file.
    
```bash
# Basic text conversion
fa2en "Your text here"

# Interactive mode
fa2en -i

# Edit configuration
fa2en -c

# Test mapping
fa2en -t

# Validate configuration
fa2en -v

# Backup configuration
fa2en -b
```

### GUI Configuration Tool

```bash
python3 config_gui.py
```
Python GUI (mapping_app.py)

    Edit and save keyboard mappings visually.
    Reset mappings to default values.
    Save and load mappings from configuration files.


    
## ⚙️ Configuration

The default configuration file is stored at `~/.fa2en_config`. You can modify it using:

1. GUI Configuration Tool
2. Direct editing (`fa2en -c`)
3. Manual editing of `~/.fa2en_config`

### Configuration Format

```
ض:q|ص:w|ث:e|ق:r|...
```

Each mapping is defined as `persian_char:english_char` pairs, separated by `|`.

## 🔧 Adding to Bash Scripts

### Method 1: Source the Script

```bash
#!/bin/bash
source /path/to/fa2en.sh

# Use functions directly
convert_text "Your text here"
```

### Method 2: Use as Command

```bash
#!/bin/bash
# Make sure fa2en is in PATH
result=$(fa2en "Your text here")
echo "$result"
```

## 🐛 Troubleshooting

### Common Issues

1. **Permission Denied**
   ```bash
   chmod +x fa2en.sh
   ```

2. **Configuration File Issues**
   ```bash
   fa2en -v  # Validate configuration
   fa2en -b  # Create backup
   ```

3. **GUI Tool Doesn't Launch**
   ```bash
   pip install PyQt5
   ```

## 📞 Support

- Create an issue for bug reports
- Start a discussion for feature requests
- Check existing issues before creating new ones

## 🙏 Acknowledgments

- Contributors and maintainers
- PyQt5 team
- Open source community

---

<p align="center">
  Made with ❤️ by MG
</p>
```