from db import db
from sqlalchemy.orm import relationship
from models.ingrediente_producto import ingredientes_productos
from models.heladeria import Heladeria

class Producto(db.Model):
    __tablename__ = "productos"
    id_producto = db.Column(db.Integer, primary_key = True, nullable = False)
    nombre = db.Column(db.String(50), nullable = False)
    precio = db.Column(db.Float, nullable = False)
    volumen_oz = db.Column(db.Integer, nullable = True)
    tipo_vaso = db.Column(db.String(30), nullable = True)
    is_copa = db.Column(db.Boolean, nullable = False)
    ingredientes = relationship("Ingrediente", secondary = ingredientes_productos, backref = "Producto" )

    def vender(self, id_producto: int) -> str:
        
        resultado:str = "No se encuentra el producto"
        con_inventario: bool = False
        producto_venta = Producto.query.filter_by(id_producto = id_producto).first()


        if isinstance(producto_venta, Producto) == True:


            for ingrediente in producto_venta.ingredientes:
                if ingrediente.is_complemento == False and ingrediente.contador >= 0.2:
                    con_inventario = True
                elif ingrediente.is_complemento == True and ingrediente.contador >= 1.0:
                    con_inventario = True
                else:
                    con_inventario = False
                    raise ValueError(f"{ingrediente.nombre}")
                    break

            if con_inventario == True:
                for ingrediente in producto_venta.ingredientes:
                    if ingrediente.is_complemento == False \
                    and ingrediente.contador >= 0.2:

                        ingrediente.contador -= 0.2

                    elif ingrediente.is_complemento == True \
                    and ingrediente.contador >= 1.0:
                        
                        ingrediente.contador -= 1.0

                heladeria = Heladeria.query.filter_by(id = 1).first()
                heladeria.venta_dia += producto_venta.precio


                resultado:str = "¡¡¡¡ Producto Vendido !!!!!"

        return resultado
                
    def producto_rentable(self) -> None:
        productos = Producto.query.all()
        heladeria = Heladeria.query.filter_by(id=1).first()
        producto_rentable: str = ""
        valor_producto_rentable: float = 0.0
        valor_producto: float = 0.0

        print("Clase rentable")
        print(productos)
        for producto in productos:
            valor_producto = 0.0
            # print("el for 64")
            # print(producto.__dict__)
            for ingrediente in producto.ingredientes:
                valor_producto += ingrediente.precio

            if valor_producto >= valor_producto_rentable:
                valor_producto_rentable = valor_producto
                producto_rentable = producto.nombre
                

        heladeria.producto_mas_rentable = producto_rentable




            