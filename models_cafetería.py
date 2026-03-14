class Persona(): #clase padre
    def __init__(self, id_persona,nom,email):
        self.id_persona=id_persona
        self.nombre=nom
        self.email=email
        self.sesion_activa=True

    def login(self, nom_ing, id_ing):
        if self.nombre==nom_ing and self.id_persona==id_ing:
            self.sesion_activa=True
            return True
        else:
            return False

    def cerrar_sesion(self):
        if self.sesion_activa==True:
            self.sesion_activa=False
            print("Su sesión se ha cerrado")
        else:
            print("No hay cuenta que cerrar.")

    def actualizar_perfil(self, nuev_email=None):
        if nuev_email:
            self.email=nuev_email

class Cliente(Persona):
    def __init__(self,id_persona,nom,email,punt_fid):
        super().__init__(id_persona,nom,email)
        self.puntos_fidelidad=punt_fid
        self.historial_pedidos=[]

    def realizar_pedidos(self, pedido):
        self.historial_pedidos.append(pedido)

    def consultar_historial(self):
        if len(self.historial_pedidos)==0:
            print("No hay pedidos registrados")
        else:
            for p in self.historial_pedidos:
                print(f"Pedido: {p.id_pedido} | Estado: {p.estado}")

    def canjear_puntos(self, puntos):
        if puntos <= self.puntos_fidelidad:
            self.puntos_fidelidad-=puntos
            print("Sus puntos han sido canjeados exitosamente")
        else:
            print("No tienes suficientes putnos")

class Empleado(Persona):
    def __init__(self,id_persona,nom,email,id_empl,rol):
        super().__init__(id_persona,nom,email)
        self.id_empleado=id_empl
        self.rol=rol #BARISTA, MESERO, GERENTE

    def actualizar_inventario(self, inventario_obj, nombre_producto,cantidad):
        inventario_obj.agregar_stock(nombre_producto, cantidad)

    def cambiar_estado_pedido(self, pedido,nuevo_estado):
        pedido.estado=nuevo_estado
        print(f"Pedido {pedido.id_pedido} actualizado a {nuevo_estado}")

class Producto_base():
    def __init__(self, id_produc, nom_prod,precio_base):
        self.id_productos=id_produc
        self.nombre_prod=nom_prod
        self.precio_base=precio_base

class Bebida(Producto_base):
    def __init__(self,id_produc,nom_prod,precio_base,tamaño,temp):
        super().__init__(id_produc, nom_prod,precio_base)
        self.tamaño=tamaño
        self.temperatura=temp #FRIA, CALIENTE
        self.modificadores=[]

    def agregar_extra(self, extra, precio):
        self.modificadores.append((extra,precio))

    def calcular_precio_final(self):
        total=self.precio_base
        for extra in self.modificadores:
            total+=extra[1]
        return total
    
class Postre(Producto_base):
    def __init__(self,id_produc, nom_prod,precio_base,es_vegano,sin_gluten):
        super().__init__(id_produc, nom_prod,precio_base)
        self.es_vegano=es_vegano
        self.sin_gluten=sin_gluten

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, nombre_prod, cantidad):
        self.stock[nombre_prod] = self.stock.get(nombre_prod, 0) + cantidad

    def tiene_stock(self, nombre_prod):
        return self.stock.get(nombre_prod, 0) > 0

    def reducir_stock(self, nombre_prod):
        if self.tiene_stock(nombre_prod):
            self.stock[nombre_prod] -= 1
            return True
        return False

class Pedido():
    def __init__(self,id_ped):
        self.id_pedido=id_ped
        self.estado="PENDIENTE"
        self.productos=[]
        self.total=0

    def calcular_total(self):
        total=0
        for p in self.productos:
            if hasattr(p, "calcular_precio_final"):
                total+=p.calcular_precio_final()
            else:
                total+=p.precio_base
        self.total=total
        return total
    
    def agregar_producto(self,producto):
        self.productos.append(producto)

    def validar_stock(self, invent_sistema):
        for p in self.productos:
            if not invent_sistema.tiene_stock(p.nombre_prod):
                print(f"NO hay stock de {p.nombre_prod}")
                return False
        
        print("Stock validado: Todos los productos están disponibles.")
        return True