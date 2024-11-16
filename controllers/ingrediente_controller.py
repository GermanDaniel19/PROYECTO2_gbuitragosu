# from db import db
from models.ingrediente import Ingrediente
from flask import Blueprint,render_template, request, flash
from db import db


ingrediente_bp = Blueprint("ingrediente_bp",__name__,url_prefix="/ingredientes")

@ingrediente_bp.route("/", methods = ["GET","POST"])
def index():
    ingredientes = Ingrediente.query.all()
    if request.method == "GET":
        return render_template("ingredientes.html", ingredientes = ingredientes)
    else:
        if int(request.form["opcion"]) == 1:
            ingrediente_actualizar = Ingrediente.query\
                .filter_by(id = request.form["id_ingrediente"] )\
                .first()
            
            if isinstance(ingrediente_actualizar,Ingrediente):
                if ingrediente_actualizar.calorias < 100 \
                    or ingrediente_actualizar.vegetariano == True:

                    flash(f"Ingrediente {ingrediente_actualizar.nombre} es SANO !!!")
                
                else: 
                    flash(f"Ingrediente {ingrediente_actualizar.nombre} NO es sano")
            
            else: 
                flash("no se encuentra el ingrediente")
    
            return render_template("ingredientes.html", ingredientes = ingredientes)

        #Bajar complemento a 0
        elif int(request.form["opcion"]) == 3:
            
            ingrediente_actualizar = Ingrediente.query\
                .filter_by(id = request.form["id_ingrediente"], is_complemento = True )\
                .first()
            if isinstance(ingrediente_actualizar,Ingrediente):
                ingrediente_actualizar.contador = 0.0
                db.session.commit()
                flash("Producto guardado exitosamente")
            else: flash("Producto no existe o no es complemento")
            
            return render_template("ingredientes.html", ingredientes = ingredientes)
        
        #Reabastecer
        elif int(request.form["opcion"]) == 2:
            ingrediente_actualizar = Ingrediente.query\
                .filter_by(id = request.form["id_ingrediente"] )\
                .first()
            
            if isinstance(ingrediente_actualizar,Ingrediente):

                if ingrediente_actualizar.is_complemento == True:
                    ingrediente_actualizar.contador += 10
                else: 
                    ingrediente_actualizar.contador += 5

                flash(f"ingrediente {ingrediente_actualizar.nombre} reabastecido con exito")
                db.session.commit()                
            
            return render_template("ingredientes.html",ingredientes = ingredientes)
        
        else: 
            return render_template("ingredientes.html",ingredientes = ingredientes)

            