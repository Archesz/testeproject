from flask_sqlalchemy import SQLAlchemy

# Instância do SQLAlchemy
db = SQLAlchemy()

# Modelo para a tabela "Tarefa"
class Tarefa(db.Model):
    __tablename__ = "tarefas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))

    def to_dict(self):
        """
        Converte o objeto Tarefa para um dicionário,
        facilitando o retorno como JSON.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
        }
