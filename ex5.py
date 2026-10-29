from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
db = []

@app.route("/produtos", methods=["GET"])
def listar():
    return jsonify(db)

@app.route("/produtos", methods=["POST"])
def salvar():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    obj = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    db.append(obj)
    return jsonify(obj), 201

@app.route("/produtos/<int:id>", methods=["PUT"])
def editar(id):
    dados = request.get_json()
    for obj in db:
        if obj["id"] == id:
            obj["nome"] = dados.get("nome")
            obj["preco"] = dados.get("preco")
            obj["categoria"] = dados.get("categoria")
            return jsonify(obj), 200
    return jsonify({"erro": "Objeto nao encontrado"}), 404

@app.route("/produtos/<int:id>", methods=["DELETE"])
def remover(id):
    for obj in db:
        if obj["id"] == id:
            db.remove(obj)
            return "", 204
    return jsonify({"erro": "Objeto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
