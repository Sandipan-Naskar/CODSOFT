from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    result = ''
    if request.method == "POST":
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            op = request.form['operation']
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2 if num2 != 0 else 'Error (Divide by 0)'
            else:
                result = 'Invalid Operation'
        except:
            result = 'Invalid Input'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
