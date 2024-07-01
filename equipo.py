class Equipo : 
    def __init__(self,id_equipo,codigo,nombre_equipo,grupo): 
        self.id_equipo = id_equipo
        self.codigo = codigo
        self.nombre_equipo = nombre_equipo
        self.grupo = grupo
    
    def show(self): 
        return(self.id_equipo, self.codigo, self.nombre_equipo, self.grupo)
    
    def guardar(self):
        return {
            'id_equipo': self.id_equipo,
            'codigo': self.codigo,
            'nombre_equipo': self.nombre_equipo,
            'grupo': self.grupo
        }