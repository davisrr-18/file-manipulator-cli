# file-manipulator-cli
A Python CLI tool for creating, reading, editing, and deleting text files with error handling.

# Python File Manager CLI
A robust command-line tool built with Python to manage text files. This project demonstrates safe file handling, error management, and interaction with the operating system.

# Key Features
- **Safe Creation:** Prevents accidental overwriting with user confirmation.
- **Append Mode:** Add new content to existing files without losing previous data.
- **Error Handling:** Robust checks for `FileNotFoundError` and unexpected system errors.
- **OS Integration:** Uses the `os` module to verify file paths and remove files from the disk.

# Concepts Applied
- **Context Managers:** Using `with open()` to ensure files are closed correctly.
- **File Modes:** Implementation of `w` (write), `r` (read), and `a` (append).
- **System Calls:** Cross-platform screen clearing (`cls` vs `clear`).

# How to use
1. Clone the repository:
   ```bash
   git clone [https://github.com/davisrr-18/file-manipulator-cli.git]
