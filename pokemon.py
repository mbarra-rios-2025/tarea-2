class Pokemon:
    def __init__(self, nombre, tipo, puntos_vida, puntos_ataque_fisico_base, puntos_defensa_fisica_base, 
        puntos_ataque_especial_base, puntos_defensa_especial_base, puntos_velocidad_base, movimientos):

        self.nombre = nombre
        self.tipo = tipo
        self.pts_vida = puntos_vida
        self.pts_ataque_fisico_base = puntos_ataque_fisico_base
        self.pts_defensa_fisica_base = puntos_defensa_fisica_base
        self.pts_ataque_especial_base = puntos_ataque_especial_base
        self.pts_defensa_especial_base = puntos_defensa_especial_base
        self.pts_velocidad_base = puntos_velocidad_base
        self.movimientos = movimientos