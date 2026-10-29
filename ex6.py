from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
db = []

@app.route("/carros", methods=["GET"])
def listar():
    return jsonify(db)

@app.route("/carros", methods=["POST"])
def salvar():
    global id
    id = id + 1
    dados = request.get_json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("ano")
    obj = {"id": id, "modelo": modelo, "marca": marca, "ano": ano}
    db.append(obj)
    return jsonify(obj), 201

@app.route("/carros/<int:id>", methods=["PUT"])
def editar(id):
    dados = request.get_json()
    for obj in db:
        if obj["id"] == id:
            obj["modelo"] = dados.get("modelo")
            obj["marca"] = dados.get("marca")
            obj["ano"] = dados.get("ano")
            return jsonify(obj), 200
    return jsonify({"erro": "Objeto nao encontrado"}), 404

@app.route("/carros/<int:id>", methods=["DELETE"])
def remover(id):
    for obj in db:
        if obj["id"] == id:
            db.remove(obj)
            return "", 204
    return jsonify({"erro": "Objeto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
