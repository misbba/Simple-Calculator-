# 🧮 Smart Calculator

A clean, modern, responsive full-stack Python web application that performs basic and advanced mathematical calculations, validates user input, handles errors gracefully, maintains runtime calculation history, and is deployment-ready for GitHub and Render.

---

## 📌 Project Overview

**Smart Calculator** is built using Python 3 and Flask on the backend with vanilla HTML5, CSS3, and JavaScript on the frontend. It is designed to be beginner-friendly, highly accessible, and visually impressive. The application operates without requiring a database, storing calculation history in-memory during application runtime.

---

## ✨ Features

- **Basic Operations**: Addition (`+`), Subtraction (`-`), Multiplication (`×`), Division (`÷`)
- **Advanced Operations**: 
  - Modulus (`%`)
  - Power (`^`)
  - Floor Division (`//`)
  - Square Root (`√`)
  - Percentage (`% of`, e.g. 10% of 500 = 50)
- **Decimal Precision Handling**: Formats results neatly (e.g. `30.0` displays as `30`).
- **Robust Input Validation**: Validates empty inputs, invalid character inputs, and out-of-range operations.
- **Graceful Error Handling**: Displays friendly messages for division by zero, negative square roots, etc.
- **Calculation History**: Maintains a live log of calculations performed during the runtime session.
- **Clear History Feature**: Allows users to clear calculation history with confirmation.
- **Responsive UI**: Glassmorphic dark card design optimized for Mobile, Tablet, and Desktop screens.

---

## 🛠️ Technologies Used

- **Backend**: Python 3, Flask
- **WSGI Production Server**: Gunicorn
- **Frontend**: HTML5, CSS3 (Vanilla Design System), JavaScript (ES6 Fetch API)
- **Deployment Targets**: GitHub, Render

---

## 📂 Project Structure

```text
SmartCalculator/
│
├── app.py              # Flask server, routes, request parsing, history state
├── calculator.py       # Core mathematical operations & result formatting functions
├── test_calculator.py  # Unit tests for mathematics logic and edge cases
├── requirements.txt    # Python dependencies (Flask, Gunicorn)
├── .gitignore          # Excludes temporary files, pycache, and virtual environments
├── README.md           # Project documentation and deployment guide
│
├── templates/
│   └── index.html      # Semantic HTML5 template with calculator UI layout
│
└── static/
    ├── style.css       # Custom modern CSS styles, animations, and media queries
    └── script.js       # Client-side JavaScript for AJAX requests & dynamic UI
```

---

## ⚙️ Installation

Follow these beginner-friendly steps to set up the project on your local Windows computer:

1. **Open your terminal or command prompt** inside the project folder:
   ```cmd
   cd SmartCalculator
   ```

2. **Create a virtual environment**:
   ```cmd
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows (Command Prompt):
     ```cmd
     venv\Scripts\activate
     ```
   - On Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

4. **Install the required packages**:
   ```cmd
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Application

Start the Flask development web server:

```cmd
python app.py
```

Once started, open your web browser and navigate to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Testing

### Automated Unit Tests
Run the included unit test suite to verify all mathematical functions and error states:

```cmd
python -m unittest test_calculator.py
```

### Manual Test Cases & Expected Results

| First Number | Second Number | Operation | Expected Result |
| :--- | :--- | :--- | :--- |
| `10` | `20` | Addition (`+`) | `30` |
| `20` | `5` | Subtraction (`-`) | `15` |
| `5` | `4` | Multiplication (`×`) | `20` |
| `20` | `5` | Division (`÷`) | `4` |
| `10` | `3` | Modulus (`%`) | `1` |
| `2` | `5` | Power (`^`) | `32` |
| `20` | `3` | Floor Division (`//`) | `6` |
| `25` | *(Disabled)* | Square Root (`√`) | `5` |
| `10` | `500` | Percentage (`% of`) | `50` |

### Error Handling Verification
- `10 ÷ 0` → Displays *"Cannot divide by zero."*
- `10 % 0` → Displays *"Cannot calculate modulus with zero."*
- `10 // 0` → Displays *"Cannot perform floor division by zero."*
- `√(-25)` → Displays *"Cannot calculate the square root of a negative number."*
- `(empty input)` → Displays *"Please enter a valid number."*

---

## 🌐 GitHub & Deployment Guide

### Step 1: Upload to GitHub

Initialize your repository and push to GitHub using the following Git commands:

```cmd
git init
git add .
git commit -m "Initial Smart Calculator project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
*(Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository link)*

### Step 2: Deploy to Render

1. Log in to [Render](https://render.com/).
2. Click **New +** → select **Web Service**.
3. Connect your GitHub repository.
4. Fill in the deployment parameters:
   - **Name**: `smart-calculator`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click **Create Web Service**.

**Live Demo**:
[Add Render URL after deployment]

---

## 🚀 Future Enhancements

- 🔬 Scientific calculator mode (trigonometry, logarithms)
- 🌙 Dark / Light theme switcher
- 💾 Persistent history storage using a database (SQLite / PostgreSQL)
- ⌨️ Full physical keyboard shortcut support
- 📏 Unit converter module (length, weight, temperature)
- 💱 Live currency exchange rate converter
