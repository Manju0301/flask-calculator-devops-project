from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import operator

app = Flask(__name__)
CORS(app)

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculate(expr):
    parts = expr.split()
    if len(parts) != 3:
        raise ValueError("Expression must be in form: number operator number")
    a, op, b = parts
    a_val, b_val = float(a), float(b)

    if op not in ops:
        raise ValueError(f"Unsupported operator: {op}")

    if op == '/' and b_val == 0:
        raise ValueError("Division by zero is not allowed")

    return ops[op](a_val, b_val)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            text-align: center;
        }
        input, button {
            padding: 10px;
            margin: 8px;
            font-size: 16px;
        }
        #result {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Calculator App</h1>
    <p>Enter expression like: 10 + 5</p>
    <input type="text" id="expression" placeholder="10 + 5">
    <button onclick="calculate()">Calculate</button>
    <div id="result"></div>

    <script>
        async function calculate() {
            const expression = document.getElementById("expression").value;
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ expression })
            });

            const data = await response.json();

            if (data.result !== undefined) {
                document.getElementById("result").innerText = "Result: " + data.result;
            } else {
                document.getElementById("result").innerText = "Error: " + data.error;
            }
        }
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_PAGE)

@app.route('/calculate', methods=['POST'])
def calc():
    data = request.get_json()

    if not data or 'expression' not in data:
        return jsonify({'error': 'Missing expression'}), 400

    try:
        result = calculate(data['expression'])
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)