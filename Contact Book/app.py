from flask import Flask, render_template, request, redirect

app = Flask(__name__)
contacts = []

@app.route("/")
def index():
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["POST"])
def add():
    contact = {
        "name": request.form["name"],
        "phone": request.form["phone"],
        "email": request.form["email"],
        "address": request.form["address"]
    }
    contacts.append(contact)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    contacts.pop(index)
    return redirect("/")

@app.route("/update/<int:index>", methods=["GET", "POST"])
def update(index):
    if request.method == "POST":
        contacts[index] = {
            "name": request.form["name"],
            "phone": request.form["phone"],
            "email": request.form["email"],
            "address": request.form["address"]
        }
        return redirect("/")
    return render_template("update.html", contact=contacts[index], index=index)

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"].lower()
    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    return render_template("index.html", contacts=results)

if __name__ == "__main__":
    app.run(debug=True)
