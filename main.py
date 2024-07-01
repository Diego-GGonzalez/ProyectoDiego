from urllib.request import urlopen
import json
import random
from equipo import Equipo
from estadio import Estadio, Restaurante, Productos
from partidos import Partido
from cliente import Cliente

# Esta función se encarga de reiniciar los archivos de texto utilizados para guardar la información.
# Se utiliza para borrar los contenidos de los archivos y volver a cargar la información desde la API.
def reiniciar():
    open("equipos.txt", "w")
    open("estadios.txt", "w")
    open("partidos.txt", "w")
    open("clientes.txt", "w")

def guardar(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos):
    
    #Esta funcion se encarga de guardar la informacion de los equipos, estadios, partidos y clientes en archivos de texto.
    #Recibe como parametros los listas de objetos de cada categoria y devuelve None.
    #La informacion se guarda en archivos de texto con el nombre de la categoria y cada objeto se guarda en una linea.
    
    with open("equipos.txt", "w") as file:
        file.write(str([z.guardar() for z in equipos_todos]))
    with open("estadios.txt", "w") as file:
        file.write(str([z.guardar() for z in estadios_todos]))
    with open("partidos.txt", "w") as file:
        file.write(str([z.guardar() for z in partidos_todos]))
    with open("clientes.txt", "w") as file:
        file.write(str([z.guardar() for z in clientes_todos]))
        
def gestion_info(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos): 
    # esta funcion va a descargar la informacion de la api en objetos para asi poder filtrarla y trabajar con ella 
    try:
        with open("equipos.txt", "r") as file:
            data = file.read()
            
        if len(data) == 0:
            
            url = urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
            data = json.loads(url.read())   
            for dato in data : 
                new_equipo = Equipo(dato["id"],dato["code"],dato["name"],dato["group"])

                equipos_todos.append(new_equipo)
            guardar_equipos=[z.guardar() for z in equipos_todos]
            with open("equipos.txt", "w") as file:
                file.write(str(guardar_equipos))
                
        else:
            for x in eval(data):
                new_equipo = Equipo(x["id_equipo"],x["codigo"],x["nombre_equipo"],x["grupo"])
                equipos_todos.append(new_equipo)
                
    except Exception as e:
        print(e)
        
        
    try:
        with open("estadios.txt", "r") as file:
            data = file.read()
            
        if len(data) == 0:
            url_estadios = urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
            data = json.loads(url_estadios.read()) 
            for dato in data : 
                restaurante = []
                for x in dato["restaurants"]: 
                    productos=[]
                    for y in x["products"]:
                        new_producto = Productos(y["name"],y["quantity"],y["price"],y["stock"],y["adicional"])
                        productos.append(new_producto)
                    new_restaurante = Restaurante(x["name"], productos)
                    restaurante.append(new_restaurante)
                    restaurantes_todos.append(new_restaurante)
                new_estadio = Estadio(dato["id"], dato["name"], dato["city"], dato["capacity"], restaurante)
                estadios_todos.append(new_estadio)
            guardar_estadios=[z.guardar() for z in estadios_todos]
            with open("estadios.txt", "w") as file:
                file.write(str(guardar_estadios))

        else:
            for x in eval(data):
                restaurante=[]
                for y in x["restaurantes"]: 
                    product = []
                    for z in y["producto"]:
                        new_producto = Productos(z["nombre"],z["cantidad"],z["precio"],z["stock"],z["tipo"])
                        product.append(new_producto)
                    new_restaurante = Restaurante(y["nombre"],product)
                    restaurante.append(new_restaurante)
                    restaurantes_todos.append(new_restaurante)
                new_estadio = Estadio(x["id_estadio"],x["nombre_estadio"],x["ciudad"],x["capacidad"],restaurante)
                estadios_todos.append(new_estadio)
                
    except Exception as e:
        print(e)
        print("Error al descargar la informacion de los estadios")
        
        

    try:
        with open("partidos.txt", "r") as file:
            data = file.read()
            
        if len(data) == 0:
            url_partidos = urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
            data = json.loads(url_partidos.read())
            for dato in data :
                for x in estadios_todos:
                    if x.id_estadio == dato["stadium_id"] :
                        espacios = x.puestos()
                new_partido = Partido(dato["id"],dato["number"],dato["home"],dato["away"],dato["date"],dato["group"],dato["stadium_id"], espacios)
                partidos_todos.append(new_partido)

            guardar_partidos=[z.guardar() for z in partidos_todos]
            with open("partidos.txt", "w") as file:
                file.write(str(guardar_partidos))

        else:
            for x in eval(data):
                new_partido = Partido(x["id_partido"],x["numero"],x["local"],x["visitante"],x["fecha"],x["grupo"],x["id_estadio"],x["espacio"])
                partidos_todos.append(new_partido)
                
    except Exception as e:
        print(e)
        
        
    try:
        with open("clientes.txt", "r") as file:
            data = file.read()
            
        if len(data) !=0:
            val = eval(data)
            for x in val:
                new_cliente = Cliente(x["nombre"], x["cedula"], x["edad"], x["partido"], x["puesto"], x["VIP"], x["codigo"], x["asistencia"], x["compras"])
                clientes_todos.append(new_cliente)
        
    except Exception as e:
        print(e)
                   
#Filtrar partidos
def buscar_partidos_pais(pais, partidos_todos):
    # Esta funcion busca partidos de un pais en particular y los muestra por pantalla.
    # Toma como parametros el nombre del pais y la lista de partidos todos.
    # Recorre cada partido y comprueba si el nombre del local o el del visitante es igual al nombre del pais.
    # Si es asi, muestra el partido por pantalla.
        for x in partidos_todos:
            if x.local["name"] == pais or x.visitante["name"] == pais:
                print(x.mostrar())
    
# Filtrar estadios            
def buscar_partidos_estadio(estadio, partidos_todos):
        id_est = ""
        for x in estadios_todos:
            if x.nombre_estadio == estadio:
                id_est = x.id_estadio
        for x in partidos_todos:
            if x.id_estadio == id_est:
                print(x.mostrar())
                
# Filtrar fechas
def buscar_partidos_fecha(fecha, partidos_todos):
        for x in partidos_todos:
            if x.fecha == fecha:
                print(x.mostrar())

def busqueda_total(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos):
    print ('1. Buscar partidos por pais')
    print ('2. Buscar partidos por estadio')
    print ('3. Buscar partidos por fecha')
    print ('4. Salir')
    op = input('Elija una opcion: ')
    if op == '1':
        pais = input('Ingrese el pais: ')
        buscar_partidos_pais(pais, partidos_todos)
        
    elif op == '2':
        estadio = input('Ingrese el estadio: ')
        print(buscar_partidos_estadio(estadio, partidos_todos))
    elif op == '3':
        fecha = input('Ingrese la fecha (aaaa-mm-dd): ')
        print(buscar_partidos_fecha(fecha, partidos_todos))
    elif op == '4':
        print('Volver al MENU')   
        
                 
def venta_entradas(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos):
    # Esta funcion se encarga de permitir la venta de entradas a partidos,
    # solicita al usuario su nombre, cedula y edad, luego busca partidos
    # utilizando la funcion busqueda_total, y finalmente solicita el id del
    # partido deseado. Si el partido no es encontrado se vuelve a solicitar
    # el id.
    nombre = input('Ingrese su nombre: ')
    cedula = input('Ingrese su cedula: ')
    while not cedula.isnumeric():
        cedula = input('Ingrese su cedula: ')
        cedula = int(cedula)
    edad = input('Ingrese su edad: ')
    while not edad.isnumeric(): 
        edad = input('Ingrese su edad: ')
    edad = int(edad)
    
    busqueda_total(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos)
    
    partido = input('Ingrese el id del partido deseado: ')
    ids = [x.id_partido for x in partidos_todos]
    while partido not in ids:
        print('Partido no encontrado')
        partido = input('Ingrese el id del partido deseado: ')
    
    for x in partidos_todos:
        if partido == x.id_partido:
            partidoS = x
            for y in estadios_todos:
                if y.id_estadio == x.id_estadio:
                    print(f"La capacidad del estadio es: {y.capacidad}")
                    estadioS=y
                    
    VIP = input('Es VIP (s/n): ')
    if VIP == 's':
        VIP = True
    else:
        VIP = False
    
    fila = input('Ingrese la fila: ')
    while not fila.isdigit() or int(fila) > estadioS.capacidad[0]:
        fila = input('Error, Ingrese la fila: ')
    columna = input('Ingrese la columna: ')
    while not columna.isdigit() or int(columna) > estadioS.capacidad[1]:
        columna = input('Error, Ingrese la columna: ')
    while partidoS.comprobar_puesto(int(fila), int(columna)):
        print("Error, puesto ocupado")
        fila = input('Ingrese la fila: ')
        while not fila.isdigit() or int(fila) > estadioS.capacidad[0]:
            fila = input('Error, Ingrese la fila: ')
        columna = input('Ingrese la columna: ')
        while not columna.isdigit() or int(columna) > estadioS.capacidad[1]:
            columna = input('Error, Ingrese la columna: ')
            
    puesto = [fila,columna]
    codigo = random.randint(10000000, 99999999)
    cliente = Cliente(nombre, cedula, edad, partido, puesto, VIP, codigo, False)
    if cliente.precios() == True:
        clientes_todos.append(cliente)

def entrada_partido(clientes_todos):
    # Esta funcion se encarga de permitir que un cliente ingrese al partido
    # utilizando su codigo de boleto. Verifica si el cliente ya ha asistido al
    # partido y en caso de que no, cambia el atributo asistencia a True.
    codigo = int(input('Ingrese el codigo: '))
    for x in clientes_todos:
        if x.codigo == codigo:
            if x.asistencia == True:
                print('Boleto ya utilizado')
                return
            else:
                x.asistencia = True
                return

def buscar_restaurantes(restaurantes_todos, estadios_todos, edad, partido):
    
    #Esta funcion busca en la lista de restaurantes los que se encuentran en el
    #mismo estadio que el partido ingresado y devuelve una lista con los nombres de
    #dichos restaurantes y otra lista con los productos que ofrecen en ese restaurante.
    
    
    restaurantes = []
    seleccion = []
    productos = []
    if edad >= 18:
        alcohol = True
    else:
        alcohol = False
    if partido == None:
        for x in restaurantes_todos:
            restaurantes.append(x.nombre)
        
    else:
        for x in estadios_todos:
            if x.id_estadio == partido.id_estadio:
                for y in x.restaurantes:
                    restaurantes.append(y.nombre)
                    print(y.nombre)
    
    for x in restaurantes:
        print(x)
    rest = input("Coloque el nombre del restaurante: ")
    while rest not in restaurantes:
        rest = input("Error, Coloque el nombre del restaurante: ")
    
    for x in restaurantes_todos:
        if x.nombre == rest:
            for y in x.producto:
                seleccion.append(y)
                

    print("1. Buscar producto por nombre")
    print("2. Buscar producto por tipo")
    print("3. Buscar producto por rango de precio")
    op = input('Elija una opcion: ')
    if op == '1':
        for x in seleccion:
            print(x.nombre)
        nombre = input('Ingrese el nombre del producto: ')
        for x in seleccion:
            if alcohol == True or x.tipo != 'alcoholic':
                if nombre == x.nombre:
                    print(x.guardar())
                    productos.append(x)
        if len(productos) == 0:
            print("no se encontraron productos")
        return productos
                
    elif op == '2':
        tip = input("1. Bebida\n2. Comida\nElija una opcion: ")
        if tip == '1':
            
            if alcohol == True:
                tipos = input("1. Bebida con alcohol\n2. Bebida sin alcohol\nElija una opcion: ")
                if tipos == '1':
                    tipo = 'alcoholic'
                elif tipos == '2':
                    tipo = 'non-alcoholic'
            else:
                tipo = 'non-alcoholic'
                
        elif tip == '2':
            tipos = input("1. Comida de paquete\n2. Comida de plato\nElija una opcion: ")
            if tipos == '1':
                tipo = 'package'
            elif tipos == '2':
                tipo = 'plate'
        for x in seleccion:
            if tipo == x.tipo:
                print(x.guardar())
                productos.append(x)
        if len(productos) == 0:
            print("no se encontraron productos")
        return productos
            
    elif op == '3':
        precio_min = input('Ingrese el precio minimo: ')
        precio_max = input('Ingrese el precio maximo: ')
        for x in seleccion:
            if alcohol == True or x.tipo != 'alcoholic':
                if float(precio_min) <= float(x.precio) <= float(precio_max):
                    print(x.guardar())
                    productos.append(x)
            
        if len(productos) == 0:
            print("no se encontraron productos")        
        return productos
      
def numero_perfecto(num):
 
    suma = 0
    for x in range(1, num):
        if num % x == 0:
            suma += x
    if suma == num:
        return True
    else:
        return False
  
def Compra_productos(restaurantes_todos, persona, estadios_todos, partidoP):
    
    #Esta funcion recibe una lista de restaurantes, un cliente y los estadios, un partido opcional.
    #Busca en los restaurantes los que se encuentran en el mismo estadio que el partido ingresado.
    #Luego pide al cliente que elija un restaurante y luego un producto del mismo.
    #Si el cliente es mayor de edad, se le aplicara un descuento del 15%.
    #Finalmente, se valida la cantidad de productos que se desea comprar y se guarda en una lista.
    
    compras = []
    while True:
        Productos = buscar_restaurantes(restaurantes_todos, estadios_todos, persona.edad, partidoP)
        if len(Productos) != 0:
            Producto = []
            for x in Productos:
                Producto.append(x.nombre)
            comp = input("Coloque el nombre del producto que desea comprar: ")
            while comp not in Producto:
                comp = input("Error, Coloque el nombre del producto que desea comprar: ")
            for x in Productos:
                if x.nombre == comp:
                    stock = x.stock
            if stock == 0:
                print('No hay mas stock')
            else:
                cant = input('Ingrese la cantidad: ')
                while not cant.isdigit() or int(cant) <= 0 or int(cant) > stock:
                    cant = input('Error, Ingrese la cantidad: ')

                for x in Productos:
                    if x.nombre == comp:
                        for y in range(int(cant)):
                            compras.append(x)

                print('1. Seguir Comprando')
                print('2. Terminar Compra')
                op = input('Elija una opcion: ')
                if op == '2':
                    descuento = 0
                    precio_final=0
                    if numero_perfecto(int(persona.cedula)):
                        descuento = 0.15
                    for x in compras:
                        print(f"{x.nombre}  Precio: {x.precio}")
                        precio_final += float(x.precio)
                    precio_final = precio_final - (float(precio_final) * descuento)
                    print(f"Descuento: {descuento*precio_final}")
                    print(f"Total a pagar: {precio_final}")
                    confirmar = input("Desea confirmar la compra (s/n): ")
                    if confirmar == 's':
                        for x in compras:
                            x.stock -= 1
                            persona.compras.append(x.nombre)
                        break
                    else:
                        break
    
            
def Estadisticas(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos):
    print("1. promedio de gasto de cliente por partido")
    print("2. asistencia a los partidos de mejor a peor")
    print("3. partido con mayor asistencia")
    print("4. partido con mayor boletos vendidos")
    print("5. Top 3 productos más vendidos en el restaurante")
    print("6. Top 3 de clientes (clientes que más compraron boletos)")
    op = input("Elija una opcion: ")
    if op == '1':
        partidosID=[]
        
        for x in partidos_todos:
            partidosID.append(x.id_partido)
        id_P = input("Ingrese el id del partido: ")
        while id_P not in partidosID:
            id_P = input("Error, Ingrese el id del partido: ")
        cant = 0
        gasto = 0
        precios = []
        for y in restaurantes_todos:
            for z in y.producto:
                precios.append({"nombre":z.nombre,"precio":float(z.precio)})
        for x in clientes_todos:                
            if x.partido == id_P:
                gasto += x.gasto()
                cant+=1
                for y in x.compras:
                    for z in precios:
                        if y == z["nombre"]:
                            gasto += z["precio"]
        print("El promedio de gasto por partido es: ", gasto/cant)

    elif op == '2':
        partidosDic = []
        for x in partidos_todos:
            par = {"partido": x, "asistidos": 0, "ventas": 0, "Personas": []}
            partidosDic.append(par)
        
        for x in partidosDic:
            for y in clientes_todos:
                if x["partido"].id_partido == y.partido:
                    x["Personas"].append(y)
                    x["ventas"] += 1
                    if y.asistencia == True:
                        x["asistidos"] += 1
        
        partidosDic.sort(key=lambda x: x["asistidos"], reverse=True)
        
        for x in partidosDic:
            print(x["partido"].mostrar())
            print(f"asistidos: {x['asistidos']}, boletos vendidos: {x['ventas']}")
            if x["asistidos"] != 0:
                print(f"Relacion de asistencia/boletos vendidos: {x['asistidos']/x['ventas']}")
            else:
                print(f"Relacion de asistencia/boletos vendidos: 0")
        
    
    elif op == '3':
        partidoIDAsis=[]
        for x in clientes_todos:
            if x.asistencia == True:
                partidoIDAsis.append(x.partido)
        asistidos = []
        for x in partidos_todos:
            partido = {"id_partido": x.id_partido, "asistidos": 0}
            asistidos.append(partido)
            
        for x in partidoIDAsis:
            for y in asistidos:
                if x == y["id_partido"]:
                    y["asistidos"] += 1
        partido_mas_asistido = max(asistidos, key=lambda x: x["asistidos"])
        for x in partidos_todos:
            if x.id_partido == partido_mas_asistido["id_partido"]:
                print(f"El partido con mayor asistencia es {x.mostrar()}")
    
    elif op == '4':
        partidosComp = []
        for x in clientes_todos:
            partidosComp.append(x.partido)
            comprados = []
        for x in partidos_todos:
            partido = {"id_partido": x.id_partido, "comprados": 0}
            comprados.append(partido)
            
        for x in partidosComp:
            for y in comprados:
                if x == y["id_partido"]:
                    y["comprados"] += 1
        
        partido_mas_comprado = max(comprados, key=lambda x: x["comprados"])
        for x in partidos_todos:
            if x.id_partido == partido_mas_comprado["id_partido"]:
                print(f"El partido con mayor compra de boletos es {x.mostrar()}")
    
    elif op == '5':
        ventas = []
        ventasL = []
        for x in clientes_todos:
            for y in x.compras:
                if y not in ventasL:
                    venta = {"nombre": y, "cant": 1}
                    ventasL.append(y)
                    ventas.append(venta)
                else:
                    for z in ventas:
                        if z["nombre"] == y:
                            z["cant"] += 1
                            
        top3 = sorted(ventas, key=lambda x: x["cant"], reverse=True)[:3]
        for x in top3:
            print(x)
    
    elif op == '6':
        clientes = []
        clientes_comp = []
        for x in clientes_todos:
            if x.cedula not in clientes_comp:
                cliente = {"cedula": x.cedula, "cant": 1}
                clientes_comp.append(cliente)
                clientes.append(x.cedula)
            else:
                for z in clientes_comp:
                            if z["cedula"] == y:
                                z["cant"] += 1
                                
        top3 = sorted(clientes_comp, key=lambda x: x["cant"], reverse=True)[:3]
        for x in top3:
            for y in clientes_todos:
                if x["cedula"] == y.cedula:
                    print(y.mostrar())
                    continue
#MENU
def menu(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos):
    while True: 
        print('MENU')
        print('1. Buscar partidos ')
        print('2. Venta de Entradas')
        print('3. Entrar a partido')
        print('4. Buscar restaurantes')
        print('5. Comprar en restaurante')
        print('6. Estadisticas')
        print('7. Salir')
        
        opcion = input('Elija una opcion: ')
        
        
        if opcion == '1':
            print ('1. Buscar partidos por pais')
            print ('2. Buscar partidos por estadio')
            print ('3. Buscar partidos por fecha')
            print ('4. Salir')
            op = input('Elija una opcion: ')
            if op == '1':
                pais = input('Ingrese el pais: ')
                buscar_partidos_pais(pais, partidos_todos)
                
            elif op == '2':
                estadio = input('Ingrese el estadio: ')
                print(buscar_partidos_estadio(estadio, partidos_todos))
            elif op == '3':
                fecha = input('Ingrese la fecha (aaaa-mm-dd): ')
                print(buscar_partidos_fecha(fecha, partidos_todos))
            elif op == '4':
                print('Volver al MENU')
                
                
        elif opcion == "2": 
            venta_entradas(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos)   
            guardar(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos)
        
        elif opcion == '3':
            entrada_partido(clientes_todos)
            guardar(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos)
            
        elif opcion == '4': 

            buscar_restaurantes(restaurantes_todos, estadios_todos, 18, None)
            
        elif opcion == '5':
            codigos = []
            for x in clientes_todos:
                codigos.append(x.codigo)
            if len(codigos) == 0:
                print('No hay clientes')
                continue
            codigo = int(input('Ingrese el codigo: '))
            while codigo not in codigos:
                codigo = int(input('Error, Ingrese el codigo: '))
            for x in clientes_todos:
                if x.codigo == codigo:
                    persona = x
            print(f"bienvenido {persona.nombre}")
            print()
            for x in partidos_todos:
                if x.id_partido == persona.partido:
                    partidoP = x
                    print(x.mostrar())
                
            if persona.entrada == True:
               Compra_productos(restaurantes_todos, persona, estadios_todos, partidoP)
               guardar(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos)
            else:
                print('No tiene entrada VIP')
            
        elif opcion == '6':
            Estadisticas(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos)
            
        elif opcion == '7':
            guardar(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos)
            break     
        
        elif op == '8':
            reiniciar()
        
        else:
            print('Opcion no valida')
         
             

    
    


equipos_todos = []
estadios_todos = []
partidos_todos = []
restaurantes_todos = []
clientes_todos = []
gestion_info(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos, clientes_todos)
menu(equipos_todos, estadios_todos, partidos_todos, restaurantes_todos,clientes_todos)
