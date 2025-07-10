from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'calc_secret'

@app.route("/", methods=["GET", "POST"])
def index():
    if "expression" not in session:
        session["expression"] = ""

    if request.method == "POST":
        btn = request.form["btn"]
        
        if btn == "C":
            session["expression"] = session["expression"][:-1]
        elif btn == "AC":
            session["expression"] = ""
        elif btn == "=":
            try:
                session["expression"] = str(eval(session["expression"]))
            except:
                session["expression"] = "Error"
        else:
            session["expression"] += btn

        return redirect(url_for('index'))

    return render_template("index.html", expression=session["expression"])

if __name__ == "__main__":
    app.run(debug=True)
