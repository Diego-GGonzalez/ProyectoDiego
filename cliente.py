import itertools 
class Cliente: 
    def __init__(self, nombre, cedula, edad, partido, puesto, entrada, codigo, asistencia, compras =[]):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido = partido
        self.puesto = puesto
        self.entrada = entrada
        self.codigo = codigo
        self.asistencia = asistencia
        self.compras = compras

    def guardar(self):
        return {
            'nombre': self.nombre,
            'cedula': self.cedula,
            'edad': self.edad,
            'partido': self.partido,
            'puesto': self.puesto,
            'VIP': self.entrada,
            'codigo': self.codigo,
            'asistencia': self.asistencia,
            'compras': self.compras
        }
        
    def mostrar(self):
        return {
            'nombre': self.nombre,
            'cedula': self.cedula,
            'edad': self.edad,
            'partido': self.partido,
            'puesto': self.puesto,
            'VIP': self.entrada,
            'codigo': self.codigo,
            'asistencia': self.asistencia
        }
    def gasto(self):
        # Esta funcion calcula el gasto total del cliente en el partido.
        # Primero, se verifica si el cliente es VIP o no y se asigna el precio
        # de la entrada correspondiente. Luego, se verifica si la cedula del
        # cliente es par o impar. Si es par, se calcula el descuento aplicado
        # a la entrada. Finalmente, se calcula el gasto total del cliente, que
        # es la suma del precio de la entrada, el descuento y el iva.
        if self.entrada == False:
            precio = 35
        elif self.entrada == True:
            precio = 75
        
        if len(list(str(self.cedula))) % 2 == 0:
            permutaciones = itertools.permutations(str(self.cedula))
            for perm in permutaciones : 
                mitad1 = int(''.join(perm[:len(str(self.cedula))//2]))
                mitad2 = int(''.join(perm[len(str(self.cedula))//2:]))
                
            if self.cedula == mitad1 * mitad2 :
                descuento = precio*0.16
            else:
                descuento = 0
        else:
            descuento = 0

        iva = precio - descuento * 0.16  # 16% de IVA
        return precio - descuento + iva
        
    def precios(self):
        
        if self.entrada == False:
            precio = 35
        elif self.entrada == True:
            precio = 75
        
        if len(list(str(self.cedula))) % 2 == 0:
            permutaciones = itertools.permutations(str(self.cedula))
            for perm in permutaciones : 
                mitad1 = int(''.join(perm[:len(str(self.cedula))//2]))
                mitad2 = int(''.join(perm[len(str(self.cedula))//2:]))
                
            if self.cedula == mitad1 * mitad2 :
                descuento = precio*0.5
            else:
                descuento = 0
        else:
            descuento = 0

        iva = precio -descuento * 0.16  # 16% de IVA

        print(f"Nombre: {self.nombre}\n Cedula: {self.cedula}\n Edad: {self.edad}\n Partido: {self.partido}\n Puesto: {self.puesto}\n VIP: {self.entrada}\nEl precio de la entrada es: {precio}\n Descuento: {descuento}\n IVA: {iva}\n Precio total: {precio - descuento + iva}")
        pago = input("Desea realizar el pago (s/n): ")
        if pago == 's':
            print("Gracias por su compra")
            print("Su codigo es: ", self.codigo)
            return True
        else:
            print("Gracias por su visita")
            return False


