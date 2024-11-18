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

            ingrediente_consultar = Ingrediente()
            resultado: str = ingrediente_consultar.es_sano(int(request.form["id_ingrediente"]))
            flash(resultado)
    
            return render_template("ingredientes.html", ingredientes = ingredientes)

        #Bajar complemento a 0
        elif int(request.form["opcion"]) == 3:
            
            ingrediente_consultar = Ingrediente()

            resultado: str = ingrediente_consultar\
                .bajar_complemento(int(request.form["id_ingrediente"]))
            
            db.session.commit()
            flash(resultado)

            return render_template("ingredientes.html", ingredientes = ingredientes)
        
        #Reabastecer
        elif int(request.form["opcion"]) == 2:

            ingrediente_consultar = Ingrediente()

            resultado: str = ingrediente_consultar\
                .reabastecer(int(request.form["id_ingrediente"]))
            
            # ingrediente_actualizar = Ingrediente.query\
            #     .filter_by(id = request.form["id_ingrediente"] )\
            #     .first()
            
            # if isinstance(ingrediente_actualizar,Ingrediente):

            #     if ingrediente_actualizar.is_complemento == True:
            #         ingrediente_actualizar.contador += 10
            #     else: 
            #         ingrediente_actualizar.contador += 5

            flash(resultado)
            db.session.commit()                
            
            return render_template("ingredientes.html",ingredientes = ingredientes)
        
        else: 
            return render_template("ingredientes.html",ingredientes = ingredientes)

            