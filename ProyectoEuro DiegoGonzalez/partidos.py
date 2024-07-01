from equipo import Equipo
from estadio import Estadio

class Partido(Equipo) : 
    def __init__(self, id_partido, numero, local,visitante, fecha, grupo_partido, id_estadio, espacio):
        self.id_partido = id_partido 
        self.numero = numero 
        self.local = local
        self.visitante = visitante
        self.fecha = fecha 
        self.grupo = grupo_partido
        self.id_estadio = id_estadio
        self.espacio = espacio
        
        
        
    def guardar(self):
        return {
            'id_partido': self.id_partido,
            'numero': self.numero,
            'local': self.local,
            'visitante': self.visitante,
            'fecha': self.fecha,
            'grupo': self.grupo,
            'id_estadio': self.id_estadio,
            'espacio': self.espacio
        }
        
    def show(self): 
        
        return(self.id_partido, self.local, self.visitante, self.fecha, self.grupo, self.id_estadio)
    
    def mostrar(self): 
        return f'partido : \n id : {self.id_partido} \n local : {self.local} \n visitante : {self.visitante} \n fecha : {self.fecha} \n grupo : {self.grupo} \n id_estadio : {self.id_estadio}'
    
    def ocupar_puesto(self, fila, columna):
        self.espacio[fila-1][columna-1] = True
        
    def comprobar_puesto(self, fila, columna):
        return self.espacio[fila-1][columna-1]