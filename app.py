from flask import Flask, Blueprint,render_template, request
from db import db, init_db
from models.ingrediente import Ingrediente
from models.producto import Producto
from models.heladeria import Heladeria
from controllers.ingrediente_controller import ingrediente_bp
from controllers.producto_controller import producto_bp
# from models.heladeria import Heladeria


app = Flask(__name__,template_folder="views")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/heladeria"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'mi_clave_secreta'

db.init_app(app)
init_db(app) ### Es el comando que crea los objetos


@app.route("/")
def index():
    # ingrediente1 = Ingrediente(nombre = "chupiplum",contador = 10.0, calorias = 213, precio = 15.2, vegetariano = 1, sabor = None, is_complemento = True)
    # producto1 = Producto(nombre = "producto 1", precio = 2.50, volumen_oz = 10, tipo_vaso = None, is_copa = False )

    heladeria = Heladeria(nombre = "Heladeria German" ,producto_mas_rentable = "", venta_dia = 0.0)
    db.session.add(heladeria)

    helado_de_fresa = Ingrediente(nombre = "Helado de Fresa",contador = 10.0, calorias = 150, precio = 1200.0, vegetariano = False, sabor = "Fresa", is_complemento = False)
    helado_de_mandarina = Ingrediente( nombre = "Helado de mandarina",contador = 10.0, calorias = 100, precio = 1100.0, vegetariano = False, sabor = "Mandarina", is_complemento = False)
    chispas_de_chocolate = Ingrediente( nombre = "Chispas de chocolate",contador = 10.0, calorias = 40, precio = 2500.0, vegetariano = False, sabor = "Chocolate", is_complemento = False)
    mani_japones = Ingrediente( nombre = "Mani Japonés",contador = 10.0, calorias = 2, precio = 2900.0, vegetariano = False, sabor = None, is_complemento = True)
    crema_de_leche = Ingrediente( nombre = "Crema de leche",contador = 10.0, calorias = 80, precio = 120.0, vegetariano = False, sabor = "Leche", is_complemento = False)
    chispitas = Ingrediente( nombre = "Chispitas",contador = 10.0, calorias = 2, precio = 850.0, vegetariano = False, sabor = None, is_complemento = True)
    cerezas = Ingrediente( nombre = "Cerezas",contador = 10.0, calorias = 16, precio = 790.0, vegetariano = False, sabor = None, is_complemento = True)
    dulce_mora = Ingrediente( nombre = "Dulce de mora",contador = 10.0, calorias = 22, precio = 510.0, vegetariano = False, sabor = None, is_complemento = True)
    mym = Ingrediente( nombre = "M&Ms",contador = 10.0, calorias = 57, precio = 250.0, vegetariano = False, sabor = None, is_complemento = True)

    samurai_de_fresas = Producto(nombre = "Samurai de fresas", precio = 4900.50, volumen_oz = None, tipo_vaso = "Vaso de plástico", is_copa = True)
    samurai_de_mandarinas = Producto(nombre = "Samurai de mandarinas", precio = 2500.50, volumen_oz = None, tipo_vaso = "Vaso de vidrio", is_copa = True )
    malteada_choco_espacial = Producto(nombre = "Malteda chocoespacial", precio = 11000.50, volumen_oz = 300, tipo_vaso = None, is_copa = False )
    cupi_helado = Producto(nombre = "Cupihelado", precio = 3200.50, volumen_oz = None, tipo_vaso = "Vaso de plástico", is_copa = True )

    #Ingredientes
    db.session.add(helado_de_fresa)
    db.session.add(helado_de_mandarina)
    db.session.add(chispas_de_chocolate)
    db.session.add(mani_japones)
    db.session.add(crema_de_leche)
    db.session.add(chispitas)
    db.session.add(cerezas)
    db.session.add(dulce_mora)
    db.session.add(mym)
    db.session.commit()
    #Productos
    db.session.add(samurai_de_fresas)
    db.session.add(samurai_de_mandarinas)
    db.session.add(malteada_choco_espacial)
    db.session.add(cupi_helado)

    db.session.commit()
    #ingredientes vs productos
    samurai_de_fresas.ingredientes.append(helado_de_fresa)
    samurai_de_fresas.ingredientes.append(chispas_de_chocolate)
    samurai_de_fresas.ingredientes.append(mani_japones)
    samurai_de_mandarinas.ingredientes.append(helado_de_mandarina)
    samurai_de_mandarinas.ingredientes.append(mym)
    samurai_de_mandarinas.ingredientes.append(dulce_mora)
    malteada_choco_espacial.ingredientes.append(helado_de_fresa)
    malteada_choco_espacial.ingredientes.append(chispas_de_chocolate)
    malteada_choco_espacial.ingredientes.append(crema_de_leche)
    cupi_helado.ingredientes.append(helado_de_mandarina)
    cupi_helado.ingredientes.append(chispas_de_chocolate)
    cupi_helado.ingredientes.append(chispitas)

    db.session.commit()
    
    # heladeria_mia = Heladeria([samurai_de_fresas,samurai_de_mandarinas,samurai_de_mandarinas],
    #                           [helado_de_fresa,helado_de_mandarina,chispas_de_chocolate
    #                            ,mani_japones,crema_de_leche,chispitas,
    #                            cerezas,cerezas,dulce_mora,mym])
    # return "hello world"
    return render_template('index.html')
 
# app.register_blueprint(perro_bp)
app.register_blueprint(ingrediente_bp)
app.register_blueprint(producto_bp)

@app.route("/ingredientes", methods=["GET","POST"])
def ingredientes_home():
    return render_template('ingredientes.html')

# @app.route("/producto", methods=["GET","POST"])
# def productos_home():
    


if __name__ == "__main__": 
    app.run(debug=True)

