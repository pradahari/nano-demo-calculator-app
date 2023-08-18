from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    if request.method == "POST":
       first_name = int(request.form.get("first"))
       last_name = int(request.form.get("second"))
       return jsonify({"request": first_name + last_name})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    if request.method == "POST":
       first_name = int(request.form.get("first"))
       last_name = int(request.form.get("second"))
       return jsonify({"request": first_name - last_name})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
