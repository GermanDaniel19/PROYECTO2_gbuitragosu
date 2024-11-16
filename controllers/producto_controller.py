# from db import db
from models.producto import Producto
from flask import Blueprint,render_template, request
# from app import heladeria_mia

producto_bp = Blueprint("producto_bp", __name__,url_prefix= "/producto")

@producto_bp.route("/", methods = ["GET","POST"])
def index():
    productos = Producto.query.all()
    # if request.method == "GET":
    #     return render_template("productos.html",productos=productos)
    # else:
    #     return f"hello producto {request.form["input_id_venta"]} {heladeria_mia.venta_dia}"
    return render_template("productos.html",productos=productos)