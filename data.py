from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import MethodNotAllowed


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route('/showtable', methods=['POST', "GET"])
def showTable():
    return render_template("showTable.html")


@app.route("/api", methods=['GET', 'POST'])
def showApi():
    if request.method == 'POST':
        res = request.get_json()
        
    return render_template('showApi.html')

@app.route("/apijs", methods=["POST", "GET"])
def show_Api():
    if request.method == 'POST':
        res = request.form
        name = request.form.get('name')
        comment = request.form.get("comment")
        return jsonify(res=res, name=name, comment=comment)
    return jsonify({"success":"DOne"})


if __name__ == "__main__":
    app.run(debug=True)


    