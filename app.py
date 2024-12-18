from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///tarefas.db'
db = SQLAlchemy(app)

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(100))
    
with app.app_context():
    db.create_all()
    
@app.route("/tarefas", methods=["GET"])
def get_tarefas():
    tarefas = Tarefa.query.all()
    return jsonify([{"id": t.id, "titulo": t.titulo, "descricao": t.descricao} for t in tarefas])

@app.route("/tarefas/<int:id>", methods=["GET"])
def get_tarefa(id):
    tarefa = Tarefa.query.get(id)

    if not tarefa:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    return jsonify({"id": tarefa.id, "titulo": tarefa.titulo, "descricao": tarefa.descricao})

@app.route("/tarefas", methods=["POST"])
def add_tarefa():
    data = request.json
    new_tarefa = Tarefa(titulo=data["titulo"], descricao=data["descricao"])
    db.session.add(new_tarefa)
    db.session.commit()
    
    return jsonify({"message": "Tarefa criada com sucesso!"})

@app.route("/tarefas/<int:id>", methods=["PUT"])
def update_tarefa(id):
    data = request.json
    tarefa = Tarefa.query.get(id)
    if not tarefa:
        return jsonify({"message": "Tarefa não encontrada."}), 404
    
    tarefa.titulo = data["titulo"]
    tarefa.descricao = data["descricao"]
    db.session.commit()
    return jsonify({"message": "Tarefa atualizada com sucesso!"})

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def delete_tarefa(id):
    tarefa = Tarefa.query.get(id)
    if not tarefa:
        return jsonify({"message": "Tarefa não encontrada."}), 404
    
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({"message": "Tarefa deletada com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)