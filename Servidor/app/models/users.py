import datetime
from app import db

class Users(db.model):
    id = db.Collum(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Collum(db.String(20), unique=True, nullable=False)
    email = db.Collum(db.String(60), unique=True, nullable=False)
    senha = db.Collum(db.String(20), nullable=False)
    nome = db.Collum(db.String(60))
    criado_em = db.Collum(db.DateTime, default=datetime.datetime.now())
