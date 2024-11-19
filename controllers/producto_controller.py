from db import db
from models.producto import Producto
from models.heladeria import Heladeria
from flask import Blueprint,render_template, request, flash

# from app import heladeria_mia

producto_bp = Blueprint("producto_bp", __name__,url_prefix= "/producto")

@producto_bp.route("/", methods = ["GET","POST"])
def index():
    # Producto.producto_rentable
    productos = Producto.query.all()
    heladeria = Heladeria.query.filter_by(id = 1).first()
    venta_dia: float = heladeria.venta_dia
    producto_rentable: str = heladeria.producto_mas_rentable
    
    if request.method == "GET":
        return render_template("productos.html"
                               ,productos=productos
                               ,venta_dia = venta_dia
                               ,producto_rentable = producto_rentable
                               )
    else:
        if int(request.form["opcion"]) == 1:
            producto_operar = Producto()
            try:
                resultado: str = producto_operar.vender(int(request.form["id_producto"]))
                flash(resultado)
                db.session.commit()
            except Exception as e:
                flash("¡¡ Oh No !! nos hemos quedado sin {e}")
                
            # flash(resultado)

        if int(request.form["opcion"]) == 2:
            producto_operar = Producto()
            producto_operar.producto_rentable()
            db.session.commit()

        heladeria = Heladeria.query.filter_by(id = 1).first()
        venta_dia: float = heladeria.venta_dia
        producto_rentable: str = heladeria.producto_mas_rentable
        productos = Producto.query.all()
        return render_template("productos.html"
                               ,productos=productos
                               ,venta_dia = venta_dia
                               ,producto_rentable = producto_rentable
                               )
