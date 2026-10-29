from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
db = []

@app.route("/jogos", methods=["GET"])
def listar():
    return jsonify(db)

@app.route("/jogos", methods=["POST"])
def salvar():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")
    obj = {"id": id, "nome": nome, "genero": genero, "ano": ano}
    db.append(obj)
    return jsonify(obj), 201

@app.route("/jogos/<int:id>", methods=["PUT"])
def editar(id):
    dados = request.get_json()
    for obj in db:
        if obj["id"] == id:
            obj["nome"] = dados.get("nome")
            obj["genero"] = dados.get("genero")
            obj["ano"] = dados.get("ano")
            return jsonify(obj), 200
    return jsonify({"erro": "Objeto nao encontrado"}), 404

@app.route("/jogos/<int:id>", methods=["DELETE"])
def remover(id):
    for obj in db:
        if obj["id"] == id:
            db.remove(obj)
            return "", 204
    return jsonify({"erro": "Objeto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
