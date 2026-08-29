# 🧮 Smart Calculator

A clean, modern, and responsive web-based calculator built with Python and Flask. It performs basic and advanced mathematical calculations, validates user input, handles errors gracefully, and maintains calculation history during the application runtime.

## 🌐 Live Demo

👉 [Open Smart Calculator](https://simple-calculator-nsv5.onrender.com/)

## 📂 GitHub Repository

👉 [View Source Code on GitHub](https://github.com/misbba/Simple-Calculator-)

---

## 📌 Project Overview

**Smart Calculator** is a responsive web application developed using Python 3 and Flask for the backend, with HTML5, CSS3, and JavaScript for the frontend.

The application provides a simple and user-friendly interface for performing mathematical calculations. It includes input validation, error handling, calculation history, and responsive design for desktop, tablet, and mobile devices.

The application does not require a database. Calculation history is maintained in memory during the application runtime.

---

## ✨ Features

### Basic Operations

* ➕ Addition (`+`)
* ➖ Subtraction (`-`)
* ✖️ Multiplication (`×`)
* ➗ Division (`÷`)

### Advanced Operations

* % Modulus (`%`)
* 🔢 Power (`^`)
* ➗ Floor Division (`//`)
* √ Square Root (`√`)
* 📊 Percentage (`% of`)

### Additional Features

* Decimal number support
* Clean result formatting
* Input validation
* Error handling
* Calculation history
* Clear history functionality
* Responsive user interface
* Mobile, tablet, and desktop support
* Modern glassmorphic UI design
* Beginner-friendly Python and Flask architecture

---

## 🛠️ Technologies Used

### Backend

* Python 3
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript (ES6)
* Fetch API

### Testing

* Python unittest

### Deployment

* GitHub
* Render
* Gunicorn

---

## 📂 Project Structure

```text
SmartCalculator/
│
├── app.py
├── calculator.py
├── test_app.py
├── test_calculator.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

### File Description

| File                   | Description                                                |
| ---------------------- | ---------------------------------------------------------- |
| `app.py`               | Flask application, routes, requests, and application logic |
| `calculator.py`        | Mathematical operations and result formatting              |
| `test_app.py`          | Tests for Flask application functionality                  |
| `test_calculator.py`   | Unit tests for calculator operations                       |
| `requirements.txt`     | Required Python packages                                   |
| `.gitignore`           | Files excluded from Git                                    |
| `README.md`            | Project documentation                                      |
| `templates/index.html` | Calculator web interface                                   |
| `static/style.css`     | Website styling and responsive design                      |
| `static/script.js`     | Frontend interactions and API requests                     |

---

## ⚙️ Installation

Follow these steps to run the project locally on Windows.

### 1. Clone the repository

```bash
git clone https://github.com/misbba/Simple-Calculator-.git
```

### 2. Open the project folder

```bash
cd Simple-Calculator-
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows Command Prompt:

```bash
venv\Scripts\activate
```

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask development server:

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧪 Testing

### Automated Unit Tests

Run the calculator unit tests:

```bash
python -m unittest test_calculator.py
```

Run the application tests:

```bash
python -m unittest test_app.py
```

---

## 📊 Manual Test Cases

| First Number | Second Number | Operation             | Expected Result |
| -----------: | ------------: | --------------------- | --------------: |
|           10 |            20 | Addition (`+`)        |              30 |
|           20 |             5 | Subtraction (`-`)     |              15 |
|            5 |             4 | Multiplication (`×`)  |              20 |
|           20 |             5 | Division (`÷`)        |               4 |
|           10 |             3 | Modulus (`%`)         |               1 |
|            2 |             5 | Power (`^`)           |              32 |
|           20 |             3 | Floor Division (`//`) |               6 |
|           25 |             — | Square Root (`√`)     |               5 |
|           10 |           500 | Percentage (`% of`)   |              50 |

---

## ⚠️ Error Handling

The application safely handles invalid operations and user inputs.

| Test Case     | Expected Response                                     |
| ------------- | ----------------------------------------------------- |
| `10 ÷ 0`      | Cannot divide by zero                                 |
| `10 % 0`      | Cannot calculate modulus with zero                    |
| `10 // 0`     | Cannot perform floor division by zero                 |
| `√(-25)`      | Cannot calculate the square root of a negative number |
| Empty input   | Please enter a valid number                           |
| Invalid input | Please enter a valid number                           |

---

## 🌐 Deployment

The application is deployed using **Render**.

### Build Command

```text
pip install -r requirements.txt
```

### Start Command

```text
gunicorn app:app
```

### Environment Variables

No environment variables are required for the current version of the application.

### Live Application

👉 [Open the Live Smart Calculator](https://simple-calculator-nsv5.onrender.com/)

---

## 🔗 Project Links

**GitHub Repository:**
https://github.com/misbba/Simple-Calculator-

**Live Application:**
https://simple-calculator-nsv5.onrender.com/

---

## 🚀 Future Enhancements

* 🔬 Scientific calculator mode
* Trigonometric functions
* Logarithmic calculations
* 🌙 Dark / Light theme switcher
* 💾 Persistent calculation history
* ⌨️ Full physical keyboard support
* 📏 Unit converter
* 💱 Live currency exchange rate converter
* 📱 Progressive Web App support

---

## 👩‍💻 Author

**Misbbahoonnishaa A**

Developed as a Python and Flask web application project.

---

⭐ If you find this project useful, feel free to explore the repository and try the live application.
