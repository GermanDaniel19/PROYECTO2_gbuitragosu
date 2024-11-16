from db import db
from sqlalchemy.orm import relationship
from models.ingrediente_producto import ingredientes_productos

class Producto(db.Model):
    __tablename__ = "productos"
    id_producto = db.Column(db.Integer, primary_key = True, nullable = False)
    nombre = db.Column(db.String(50), nullable = False)
    precio = db.Column(db.Float, nullable = False)
    volumen_oz = db.Column(db.Integer, nullable = True)
    tipo_vaso = db.Column(db.String(30), nullable = True)
    is_copa = db.Column(db.Boolean, nullable = False)
    ingredientes = relationship("Ingrediente", secondary = ingredientes_productos, backref = "Producto" )