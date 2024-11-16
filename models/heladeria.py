# from producto import Producto
# from base import Base
# from complemento import Complemento
# from funciones import es_sano
from db import db
from producto import Producto

class Heladeria():

    def __init__(self,productos: list, ingredientes: list) -> None:
        self._productos: list = productos
        self._ingredientes: list = ingredientes
        self._venta_dia: float = 0.0

    def vender(self, id_producto_venta: int) -> bool:

        venta: bool = False
        producto_venta: None
        con_inventario = False


        #busca el producto
        for prod in self._productos:
            
            if prod.id == id_producto_venta:
                venta = True
                producto_venta = prod
                break
        
        #Si encuentra producto revisa que tenga inventario
        if venta is True:
                
            for ingrediente in producto_venta.ingredientes:

                if ingrediente.is_complemento == False:
                    if ingrediente.contador >= 0.2:
                       con_inventario = True
                    else:
                        con_inventario = False
                        venta = False
                        break 
                elif ingrediente.is_complemento == True:
                    if ingrediente.contador >= 1:
                       con_inventario = True
                    else:
                        con_inventario = False
                        venta = False
                        break 

        #Si hay inventario le restamos y hacemos venta mompi
        if con_inventario is True:
                
            for ingrediente in producto_venta.ingredientes:

                if ingrediente.is_complemento == False:
                    ingrediente.modificar_inventario(-0.2)
                elif ingrediente.is_complemento == True:
                    ingrediente.modificar_inventario(-1)
            
            self._venta_dia += producto_venta.precio

        return venta    
                    
    def producto_rentable(self) -> str:

        producto_rentable: str = ""
        Valor_producto: float = 0.0
        producto_actual: float = 0.0

        for producto in self._productos:
            
            if (producto.precio_publico - producto.costo()) > Valor_producto:
                producto_rentable = producto.nombre
                Valor_producto = producto.precio_publico - producto.costo()

        return (f"producto_rentable: {producto_rentable} (${Valor_producto})")

    def mostrar_info(self)-> str:
        lista_ingredientes: str = '\n INGREDIENTES:'
        for ingrediente in self._ingredientes:
            lista_ingredientes += f"\n\t nombre: {ingrediente.nombre} precio: ${ingrediente.precio}  calorias: {ingrediente.calorias}  inventario: {ingrediente.inventario} es_vegetariano: {ingrediente.es_vegetariano} \n"
        return lista_ingredientes

    def reabastecer_ingrediente(self, ingrediente_reabastecer: str) -> bool:
        reabastecido: bool = False
        for ingrediente in self._ingredientes:
            if ingrediente.nombre == ingrediente_reabastecer:
                ingrediente.abastecer()
                reabastecido = True
                break
        return reabastecido

    # def bajar_complemento(self, complemento_bajar: str) -> str:
    #     accion: str = "Ingrediente no encontrado"
    #     for ingrediente in self._ingredientes:
    #         if ingrediente.nombre == complemento_bajar:
    #             if isinstance(ingrediente, Complemento):
    #                 ingrediente.renovar_inventario()
    #                 accion = "\n \t Complemento bajado a 0 Exitosamente !! \n"
    #             else:
    #                 accion = "\n \t Ingrediente no es un complemento !! \n"
    #             break

    #     return accion
    
    # def ingrediente_sano(self, ingredi: str) -> bool:
    #     resultado: str = '\n\tIngrediente NO Encontrado !!'
    #     for ingrediente in self._ingredientes:
    #         if ingrediente.nombre == ingredi:
    #             resultado = "\n\tIngrediente sano" if es_sano(ingrediente.calorias, ingrediente.es_vegetariano) else "\n\tIngrediente NO sano !! OJO !!"
    #             break
    #     return resultado

    #getters and setters
    @property
    def productos(self) -> list:
        return self._productos
    
    @productos.setter
    def productos(self, value:list) -> None:
        if isinstance(value, list):
            self._productos = value
        else:
            raise ValueError('Expected list')
        
    @property
    def ingredientes(self) -> list:
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self, value:list) -> None:
        if isinstance(value, list):
            self._ingredientes = value
        else:
            raise ValueError('Expected list')
        
    @property
    def venta_dia(self) -> float:
        return self._venta_dia
    
    @venta_dia.setter
    def venta_dia(self, value:float) -> None:
        if isinstance(value, float):
            self._venta_dia = value
        else:
            raise ValueError('Expected float')