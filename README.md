# Local Password Manager

Local Password Manager is a Python application built with tkinter. It allows you to generate and manage strong passwords for various websites and securely store them in a JSON file.

## Features

- Generate strong passwords with random characters.
- Save website, username/email, and password information securely.
- Search for stored passwords by website.
- User-friendly graphical user interface (GUI).

## Files

- `main.py`: The Python script containing the password manager application.
- `PasswordLog.json`: A JSON file where the saved website login information is stored.

## How to Use

1. Run `main.py` using Python.
2. Enter the website, username/email, and password.
3. Click the "Generate Password" button to create a strong password.
4. Click the "Add" button to save the website login information to `PasswordLog.json`.
5. Use the "Search" button to find and display saved passwords by website.

## Requirements

- Python 3.x
- tkinter library (usually included with Python)
- pyperclip library (to copy generated passwords to the clipboard)

## Usage Notes

- Keep the `PasswordLog.json` file secure, as it contains your login information.
- Customize the character sets and password length in the `passwordgenerator` function in `main.py` as needed.
- This is a basic password manager for personal use. For more advanced features and security, consider dedicated password management tools.
