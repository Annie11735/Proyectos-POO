from models_cafetería import *

#objeto de la clase usuario
c1=Cliente(2757, "Suzume", "suzu.michiracha@gamil.com", 90)
c2=Cliente(2752, "Jonas", "jonas.juar@gamil.com", 90)
c3=Cliente(2810, "Nala", "nalaaa@gmail.com", 90)
c4=Cliente(2808, "Bixby", "bixby@gmail.com", 50)
c5=Cliente(4975, "Bo", "boby@gmail.com", 95)
c6=Cliente(4858, "Ottis", "totis118@gmail.com", 20)
c7=Cliente(5911, "Potts", "pottsy@gmail.com", 60)
c8=Cliente(6108, "Jino", "jino@gmail.com", 80)
c9=Cliente(1858, "Rooni", "ronnii@gmail.com", 40)
c10=Cliente(1627, "Lucky", "luuck@gmail.com", 50)

#objetos de la clase empleado
emp1=Empleado(1708, "Jungkook", "jk@gmail.com", 1,"GERENTE")
emp2=Empleado(5258, "Taeyung", "kim.tae@gmail.com", 2, "GERENTE")
emp3=Empleado(5869, "Namjoom", "nam.rm@gmail.com", 3, "BARISTA")
emp4=Empleado(4567, "Seo-jin", "handsome_worldwide@gmail", 4, "BARISTA")
emp5=Empleado(8162, "Yoongi", "agust.d@gmail.com", 5, "MESERO")
emp6=Empleado(5029, "Jimin", "jimin@gmail.com", 6, "MESERO")
emp7=Empleado(9105, "Ho-Seok", "j.hope@gmail.com", 7, "MESERO")
emp8=Empleado(5158, "Yoonchae", "yoon@gmail.com", 8, "MESERO")
emp9=Empleado(4785, "Manon", "manon@gmail.com", 9,"BARISTA")
emp10=Empleado(5286, "Lara", "laraaa@gmail.com", 10, "BARISTA")

#objetos de la clase Bebidas
b1=Bebida(1, "Red Velvet Latte", 88,"Venti", "Frío")
b2=Bebida(2, "Pink Drink", 90,"Venti", "Frío")
b3=Bebida(3, "Matcha Cream Frappuccino", 90,"Venti", "Frío")
b4=Bebida(4, "Caramel Frappuccino", 85,"Venti", "Frío")
b5=Bebida(5, "Cajeta Cream Frappuccino",75,"Venti", "Frío")
b6=Bebida(6, "Chocolate Mexicano", 95,"Venti", "Caliente")
b7=Bebida(7, "Flat White", 80,"Venti", "Caliente")
b8=Bebida(8, "Espresso", 65,"Venti", "Caliente")
b9=Bebida(9, "Espresso Americano", 70,"Venti", "Caliente")
b10=Bebida(10, "Mocha Blanco", 80,"Venti", "Caliente")

#objetos de la clase Postre
pos1 = Postre(11, "Cheescake de queso con zarzamora", 45, False, False)
pos2 = Postre(12, "Brownie de Chocolate", 50, False, False)
pos3 = Postre(13, "Galleta de Avena y Pasas", 35, True, False) # Es vegano
pos4 = Postre(14, "Cheesecake de Fresa", 65, False, True)  # Sin gluten
pos5 = Postre(15, "Croissant de Mantequilla", 40, False, False)
pos6 = Postre(16, "Rebanada de Pastel Red Velvet", 75, False, False)
pos7 = Postre(17, "Tarta de Manzana", 60, True, False) # Es vegano
pos8 = Postre(18, "Pastel de chocolate", 30, False, True) # Sin gluten
pos9 = Postre(19, "Dona Glaseada", 25, False, False)
pos10 = Postre(20, "Macaron de Pistacho", 45, False, True) # Sin gluten

print("---------------- -------------------------------------------------")
print("                    REPORTE DE BASE DE DATOS                      ")
print("------------------------------------------------------------------")

print("\n✧ ✧ ✧ ✧ Empleados registrados ✧ ✧ ✧ ✧")
empl=[emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9,emp10]
for e in empl:
    print(f"Id: {e.id_empleado} | Nombre: {e.nombre} | Rol: {e.rol}")

print("\n✧ ✧ ✧ ✧ Usuarios registrados ✧ ✧ ✧ ✧")
clientes=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
for c in clientes:
    print(f"Nombre: {c.nombre} | Puntos de fidelidad: {c.puntos_fidelidad}") 

print("\n✧ ✧ ✧ ✧ Menú ✧ ✧ ✧ ✧")
print("\nBebidas")
bebidas=[b1, b2,b3,b4,b5,b6,b7,b8,b9,b10]
for b in bebidas:
    print(f"Bebida: {b.nombre_prod} | Precio: {b.precio_base} | Tamaño: {b.tamaño}")

print("\nPostres")
postres=[pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos7,pos8,pos9,pos10]
for p in postres:
    print(f"Postre: {p.nombre_prod} | Precio: {p.precio_base}")

tannies_inventario=Inventario() 
#stock inicial bebidas
for b in bebidas:
    tannies_inventario.agregar_stock(b.nombre_prod, 10)

#stock inicial postres
for p in postres:
    tannies_inventario.agregar_stock(p.nombre_prod, 10)


print("\n✮ ✮ ✮ ✮ Bienvenid@ al sistema de la cafetería Tannies ✮ ✮ ✮ ✮")
print("¿Cómo desea ingresar?")
print("1. Empleado")
print("2. Cliente")
print("3. Salir")
rol_acceso=input("Seleccione una opción para continuar: ")

if rol_acceso=="1":
    print("ACCESO A EMPLEADOS")
    id_empl=int(input("Ingrese si ID: "))
    empleado_activo=None
    for e in empl:
        if e.id_empleado==id_empl:
            empleado_activo=e
            break

    if empleado_activo:
        print(f"\nAcceso de Empleado: {empleado_activo.nombre} | Rol: {empleado_activo.rol}")
        
        while True:
            print("\n✧ ✧ ✧ ✧ MENÚ DE OPCIONES (EMPLEADO) ✧ ✧ ✧ ✧")
            print("1. Actualizar inventario")
            print("2. Cambiar estados de pedidos")
            print("3. Cerrar Sesión")

            op_e=input("\nSeleccione acción: ")

            if op_e=="1":
                print("\nInventario actual:")
                for producto, cantidad in tannies_inventario.stock.items():
                    print(f"{producto} | Stock: {cantidad}")

                nombre=input("Ingrese el nombre del producto: ")
                cantidad=int(input("Cantidad a agregar: "))

                empleado_activo.actualizar_inventario(tannies_inventario,nombre,cantidad)

                print("\nInventario actualizado:")
                for producto, cantidad in tannies_inventario.stock.items():
                    print(f"{producto} | Stock: {cantidad}")

            elif op_e=="2":
                id_pedido=int(input("Ingrese el ID del pedido: "))
                nuevo_estado=input("Nuevo estado (PENDIENTE / PREPARANDO / ENTREGADO): ")

                pedido_encontrado=None


                for c in clientes:
                    for ped in c.historial_pedidos:
                        if ped.id_pedido==id_pedido:
                            pedido_encontrado=ped
                            break

                if pedido_encontrado:
                    empleado_activo.cambiar_estado_pedido(pedido_encontrado,nuevo_estado)
                else:
                    print("Pedido no encontrado")

            elif op_e=="3":
                empleado_activo.cerrar_sesion()
                break
            else:
                print("Opción no válida.")

elif rol_acceso=="2":
    print("✮ ✮ ✮ ✮ Bienvenido✮ ✮ ✮ ✮ ")
    id_clien=int(input("Ingrese si ID: "))
    usuario_activo=None
    for u in clientes:
        if u.id_persona==id_clien:
            usuario_activo=u
            break
        else:
            print("ID incorrecto")
            break

    if usuario_activo:
        print(f"Access de cliente: {usuario_activo.nombre}")
        while True:
            print("\n✮ ✮ ✮ ✮ MENÚ DE ACCIONES ✮ ✮ ✮ ✮ ")
            print("1. Realizar un pedido")
            print("2. Canjear puntos")
            print("3. Ver historial de pedidos")
            print("4. Cerrar Sesión")

            opcion=input("\nSeleccione una opción:")
            if opcion=="1":
                pedido_nuevo=Pedido(len(usuario_activo.historial_pedidos)+1)

                print("\nBebidas disponibles:")
                for i,b in enumerate(bebidas):
                    print(i+1,b.nombre_prod,b.precio_base)

                print("\nPostres disponibles:")
                for i,p in enumerate(postres):
                    print(i+1,p.nombre_prod,p.precio_base)

                while True:

                    tipo=input("\n¿Agregar bebida (b), postre (p) o terminar (t)? ")

                    if tipo=="b":
                        num=int(input("Seleccione bebida #: "))
                        pedido_nuevo.agregar_producto(bebidas[num-1])

                    elif tipo=="p":
                        num=int(input("Seleccione postre #: "))
                        pedido_nuevo.agregar_producto(postres[num-1])

                    elif tipo=="t":
                        break
                        
                if pedido_nuevo.validar_stock(tannies_inventario):
                    for p in pedido_nuevo.productos:
                        tannies_inventario.reducir_stock(p.nombre_prod)

                    usuario_activo.realizar_pedidos(pedido_nuevo)

                    print("Pedido realizado con éxito")
                    print("Total a pagar:", pedido_nuevo.calcular_total())

                else:
                    print("No se puede realizar el pedido por falta de stock.")

            elif opcion=="2":
                puntos=int(input("¿Cuántos puntos desea canjear? "))
                usuario_activo.canjear_puntos(puntos)

            elif opcion=="3":
                print("Aqui puedes ver tu historial de pedidos")
                usuario_activo.consultar_historial()
            
            elif opcion=="4":
                usuario_activo.cerrar_sesion()
                break
            else:
                print("Opción inválida")

elif rol_acceso=="3": 
    print("Su sesión se ha cerrado")
    
else:
    print("Opción inválida")