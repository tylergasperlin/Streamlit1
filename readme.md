# My Streamlit Project

This project is a simple Streamlit app designed for quick prototyping and development of data-driven web applications using pure Python. Follow the instructions below to set up your environment and start the project.

## Prerequisites

- **Python 3.7+**: Ensure that Python is installed on your system.
- **Git**: Installed for version control.
- **A Code Editor (e.g., VS Code)**: Configure it to use the correct Python interpreter (i.e., your virtual environment).

## Setup Instructions

Clone the repository:
```bash
git clone <repository-url>
cd <repository-folder>
```

Create and activate a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

Install dependencies from `requirements.txt` (with the virtual environment activated):
```bash
pip install -r requirements.txt
```

Run the Streamlit app:
```bash
streamlit run app.py
```
This will launch the app in your default web browser.

If using VS Code, ensure it is configured to use your virtual environment’s Python interpreter:
- Open the Command Palette (`Cmd+Shift+P` on macOS or `Ctrl+Shift+P` on Windows/Linux).
- Select **Python: Select Interpreter** and choose the interpreter from your `venv` folder.

## Project Structure

```
my_project/
├── app.py           # Main Streamlit application
├── README.md        # This README file
├── .gitignore       # Git ignore file
├── requirements.txt # List of dependencies
└── venv/            # Virtual environment folder (should be ignored by Git)
```

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Git Documentation](https://git-scm.com/doc)

