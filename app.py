"""
app.py - Smart Calculator Flask Application

Handles routes, user input validation, calculation requests,
in-memory calculation history, and view rendering.
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
import calculator

app = Flask(__name__)

# Global in-memory list to store calculation history during runtime
HISTORY = []

# Operation mapping to human-readable symbols and functions
OPERATIONS = {
    'add': {'name': 'Addition', 'symbol': '+', 'func': calculator.add},
    'subtract': {'name': 'Subtraction', 'symbol': '-', 'func': calculator.subtract},
    'multiply': {'name': 'Multiplication', 'symbol': '×', 'func': calculator.multiply},
    'divide': {'name': 'Division', 'symbol': '÷', 'func': calculator.divide},
    'modulus': {'name': 'Modulus', 'symbol': '%', 'func': calculator.modulus},
    'power': {'name': 'Power', 'symbol': '^', 'func': calculator.power},
    'floor_divide': {'name': 'Floor Division', 'symbol': '//', 'func': calculator.floor_divide},
    'square_root': {'name': 'Square Root', 'symbol': '√', 'func': calculator.square_root},
    'percentage': {'name': 'Percentage', 'symbol': '% of', 'func': calculator.percentage}
}

@app.route('/', methods=['GET'])
def index():
    """Renders the main calculator home page."""
    return render_template(
        'index.html',
        history=HISTORY,
        result=None,
        error=None,
        num1='',
        num2='',
        selected_op='add'
    )

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Processes calculator requests, validates input, calls calculator functions,
    updates calculation history, and returns results (JSON or HTML).
    """
    # Determine if request is AJAX/JSON
    is_json = request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json

    if request.is_json:
        data = request.get_json()
        num1_str = str(data.get('num1', '')).strip()
        num2_str = str(data.get('num2', '')).strip()
        operation = data.get('operation', 'add')
    else:
        num1_str = request.form.get('num1', '').strip()
        num2_str = request.form.get('num2', '').strip()
        operation = request.form.get('operation', 'add')

    # 1. Validate Operation
    if operation not in OPERATIONS:
        error_msg = "Invalid operation selected."
        if is_json:
            return jsonify({'success': False, 'error': error_msg}), 400
        return render_template('index.html', history=HISTORY, error=error_msg, num1=num1_str, num2=num2_str, selected_op=operation)

    # 2. Validate num1 (Required for all operations)
    if not num1_str:
        error_msg = "Please enter a valid number."
        if is_json:
            return jsonify({'success': False, 'error': error_msg}), 400
        return render_template('index.html', history=HISTORY, error=error_msg, num1=num1_str, num2=num2_str, selected_op=operation)

    try:
        num1 = float(num1_str)
    except ValueError:
        error_msg = "Please enter a valid number."
        if is_json:
            return jsonify({'success': False, 'error': error_msg}), 400
        return render_template('index.html', history=HISTORY, error=error_msg, num1=num1_str, num2=num2_str, selected_op=operation)

    # 3. Validate num2 (Required for all operations EXCEPT square_root)
    num2 = None
    if operation != 'square_root':
        if not num2_str:
            error_msg = "Please enter a valid second number."
            if is_json:
                return jsonify({'success': False, 'error': error_msg}), 400
            return render_template('index.html', history=HISTORY, error=error_msg, num1=num1_str, num2=num2_str, selected_op=operation)
        
        try:
            num2 = float(num2_str)
        except ValueError:
            error_msg = "Please enter a valid second number."
            if is_json:
                return jsonify({'success': False, 'error': error_msg}), 400
            return render_template('index.html', history=HISTORY, error=error_msg, num1=num1_str, num2=num2_str, selected_op=operation)

    # 4. Perform Calculation
    try:
        op_meta = OPERATIONS[operation]
        func = op_meta['func']

        if operation == 'square_root':
            raw_result = func(num1)
        else:
            raw_result = func(num1, num2)

        formatted_result = calculator.format_result(raw_result)
        formatted_num1 = calculator.format_result(num1)
        
        # Build human-readable equation string
        if operation == 'square_root':
            equation = f"√{formatted_num1} = {formatted_result}"
        elif operation == 'percentage':
            formatted_num2 = calculator.format_result(num2)
            equation = f"{formatted_num1}% of {formatted_num2} = {formatted_result}"
        else:
            formatted_num2 = calculator.format_result(num2)
            equation = f"{formatted_num1} {op_meta['symbol']} {formatted_num2} = {formatted_result}"

        # Store in calculation history (newest first)
        HISTORY.insert(0, equation)

        if is_json:
            return jsonify({
                'success': True,
                'result': str(formatted_result),
                'equation': equation,
                'history': HISTORY
            })

        return render_template(
            'index.html',
            history=HISTORY,
            result=str(formatted_result),
            equation=equation,
            error=None,
            num1=num1_str,
            num2=num2_str if operation != 'square_root' else '',
            selected_op=operation
        )

    except ValueError as e:
        error_msg = str(e)
        if is_json:
            return jsonify({'success': False, 'error': error_msg}), 400
        return render_template('index.html', history=HISTORY, error=error_msg, num1=num1_str, num2=num2_str, selected_op=operation)
    except Exception:
        error_msg = "An unexpected calculation error occurred."
        if is_json:
            return jsonify({'success': False, 'error': error_msg}), 500
        return render_template('index.html', history=HISTORY, error=error_msg, num1=num1_str, num2=num2_str, selected_op=operation)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clears the runtime calculation history."""
    global HISTORY
    HISTORY.clear()
    
    is_json = request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json
    if is_json:
        return jsonify({'success': True, 'history': []})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Runs local Flask development server
    app.run(host='127.0.0.1', port=5000, debug=True)
