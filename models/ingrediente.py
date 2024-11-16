from db import db

class Ingrediente(db.Model):
    __tablename__ = "ingredientes"
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    nombre = db.Column(db.String(50), nullable = False)
    contador = db.Column(db.Float, nullable = False)
    calorias = db.Column(db.Integer, nullable = False)
    precio = db.Column(db.Float, nullable = False)
    vegetariano = db.Column(db.Integer, nullable = False)
    sabor = db.Column(db.String(50), nullable = True)
    is_complemento = db.Column(db.Boolean, nullable = True)
    

    def modificar_inventario(self,value):
        self.contador += value


