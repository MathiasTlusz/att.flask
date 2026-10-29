from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
db = []

@app.route("/alunos", methods=["GET"])
def listar():
    return jsonify(db)

@app.route("/alunos", methods=["POST"])
def salvar():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")
    obj = {"id": id, "nome": nome, "curso": curso, "idade": idade}
    db.append(obj)
    return jsonify(obj), 201

@app.route("/alunos/<int:id>", methods=["PUT"])
def editar(id):
    dados = request.get_json()
    for obj in db:
        if obj["id"] == id:
            obj["nome"] = dados.get("nome")
            obj["curso"] = dados.get("curso")
            obj["idade"] = dados.get("idade")
            return jsonify(obj), 200
    return jsonify({"erro": "Objeto nao encontrado"}), 404

@app.route("/alunos/<int:id>", methods=["DELETE"])
def remover(id):
    for obj in db:
        if obj["id"] == id:
            db.remove(obj)
            return "", 204
    return jsonify({"erro": "Objeto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
