class Estadio: 
    def __init__(self, id_estadio, nombre_estadio, ciudad, capacidad, restaurantes): 
        self.id_estadio = id_estadio
        self.nombre_estadio = nombre_estadio
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.restaurantes = restaurantes 
    
    def show(self): 
        return(self.id_estadio, self.nombre_estadio, self.ciudad, self.capacidad, self.restaurantes)
    
    def guardar(self):
        restaurantes = []
        for x in self.restaurantes:
            restaurantes.append(x.guardar())
        return {
            'id_estadio': self.id_estadio,
            'nombre_estadio': self.nombre_estadio,
            'ciudad': self.ciudad,
            'capacidad': self.capacidad,
            'restaurantes': restaurantes
        }
        
    def puestos(self):
        filas = self.capacidad[0]
        columnas = self.capacidad[1]
        puestos = []
        for x in range(filas):
            col = []
            for y in range(columnas):
                col.append(False)
            puestos.append(col)
            
        return puestos
                
class Restaurante():
    def __init__(self, nombre, producto): 
        self.nombre = nombre
        self.producto = producto 
        
    def show(self): 
        return(self.nombre, self.producto)
    
    def guardar(self):
        productos = []
        for x in self.producto:
            productos.append(x.guardar())
        return {
            'nombre': self.nombre,
            'producto': productos
        }

class Productos():
    def __init__(self, nombre, cantidad, precio, stock, tipo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.tipo = tipo
        
    def show(self):
        return(self.nombre, self.cantidad, self.precio, self.stock, self.tipo)
    
    def guardar(self):
        return {
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio,
            'stock': self.stock,
            'tipo': self.tipo
        }
    
