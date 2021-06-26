import math
import random 

from moves import get_move
from utilities import get_tabla_efectividad

import constante as const

# @pokemon = instancia de la clase pokemon
# calcula los puntos de vida de un pokemon
def get_puntos_de_vida(base):
    hp = ((base + const.IV) * 2 + ((math.sqrt(const.EV) / 4)) * const.Level / 100) + const.Level + 10 
    return round(hp, 2)

# @base = puntos base dependiendo del tipo de ataque o defensa
# calcula los puntos estadisticos de un pokemon (ataque, defensa, ataque especial,
# defensa especial y velocidad)
def get_stat(base): 
    stat = ((base + const.IV) * 2 + ((math.sqrt(const.EV)) / 4) * const.Level / 100) + 5
    return round(stat, 2) 

# @movimiento nombre del movimiento
# calcula la variable power requerida para calcular la variable modifier
def get_power(movimiento): 
    return int(get_move(movimiento)[1])

# calcula la variable A requerida para calcular el damage (daño)
def get_A(categoria, pokemon):
    categoria = categoria.lower() 
    if categoria == 'physical':
        return get_stat(pokemon.pts_ataque_fisico_base)
    if categoria == 'special':
        return get_stat(pokemon.pts_ataque_especial_base)

# calcula la variable D requerida para calcular el damage (daño)
def get_D(categoria, pokemon):
    categoria = categoria.lower()
    if categoria == 'physical':
        return get_stat(pokemon.pts_defensa_fisica_base)
    if categoria == 'special':
        return get_stat(pokemon.pts_defensa_especial_base)
    return 0


# @tipo_1 = nombre del tipo de ataque
# @tipo_2 = nombre del tipo de defensa
def get_type(tipo_1, tipo_2):
    # efectividad ataque
    # 0: No tiene efecto (Ejemplo: Normal contra Fantasma)  
    # 0.5: No es efectivo (Ejemplo: Fuego contra Agua)
    # 1: Efectividad normal (Ejemplo: Tierra contra Lucha)
    # 2: Super Efectivo (Ejemplo: Dragón contra Dragón)

    tabla_efectividad = get_tabla_efectividad('tabla_efectividad.csv')
    r_atk = 0
    c_def = 0
    rows = 19
    columns = 19
    # obtengo el indice de la fila del tipo de ataque
    for i in range(0, 1):
        for j in range(rows):
            valor = tabla_efectividad[i][j]
            if valor == tipo_1:
                r_atk = j 
    
    # obtengo el indice de la columna del tipo de defensa
    for i in range(columns):
        for j in range(0, 1):
            valor = tabla_efectividad[i][j]
            if valor == tipo_2:
                c_def = i 

    # debido a que devuelve un valor de tipo string, debo convertirlo (parsearlo) a float
    type = float(tabla_efectividad[r_atk][c_def])
    return type

def get_stab(movimiento, tipo_pokemon):
    tipo_movimiento = get_move(movimiento)[2]
    tipo_pokemon = tipo_pokemon
    if tipo_movimiento == tipo_pokemon:
        return 1.2
    else:
        return 1

def get_modifier(type, stab): 
    return type * stab * random.uniform(0.85, 1) * 1

def get_damage(power, a, d, modifier):
    damage = ((((2 * const.Level / 5 + 2) * power * a / d) / 50 + 2) * 2) * modifier
    return damage