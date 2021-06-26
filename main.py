from utilities import get_pokemon

import draw

from ecuaciones import get_A, get_D, get_damage, get_modifier, get_power, get_puntos_de_vida, get_stab, get_type
from moves import get_move

if __name__ == '__main__':  
    print('Bienvenido al simulador')
    nombre_pokemon1 = input('Ingrese el nombre del primer Pokémon: ')
    pokemon1 = get_pokemon(nombre_pokemon1)
    print(f'\nNombre del Pokémon seleccionado: {pokemon1.nombre}')
    draw.estadisticas_base(pokemon1)
    print(f'\nMovimientos que puede aprender el Pokémon:\n')
    draw.movimientos(pokemon1)
    int_ataque = int(input('\nSeleccione un ataque a ejecutar: '))
    str_ataque = pokemon1.movimientos[int_ataque]
    print(f'\nEl ataque seleccionado es: {str_ataque}')
    power = get_power(str_ataque)
    print(f'Poder de ataque es: {power}')
    draw.estadisticas_lvl_50(pokemon1)
    nombre_pokemon2 = input('\nIngrese el nombre a atacar del Pokémon: ')
    pokemon2 = get_pokemon(nombre_pokemon2)
    print(f'\nNombre del Pokémon seleccionado {pokemon2.nombre}')
    hp_pokemon2 = get_puntos_de_vida(pokemon2.pts_vida)
    print(f'\nEl hp al nivel 50 de {pokemon2.nombre} es {hp_pokemon2}')
    categoria = get_move(str_ataque)[3]
    a = get_A(categoria, pokemon1)
    d = get_D(categoria, pokemon2)
    type = get_type(pokemon1.tipo, pokemon2.tipo)
    stab = get_stab(str_ataque, pokemon1.tipo)
    modifier = get_modifier(type, stab)
    damage = get_damage(power, a, d, modifier)
    print(f'El daño que realizó {pokemon1.nombre} a {pokemon2.nombre} fue de: {damage}')
    print(f'\n{pokemon2.nombre} quedo con un HP de: {hp_pokemon2 - damage}')