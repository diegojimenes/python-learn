from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    data = request.get_json()
    total = 0
    for produto in data["produtos"]:
        total = total + produto["preco"]

    return jsonify({"total": total})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)