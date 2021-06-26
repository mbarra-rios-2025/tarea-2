from ecuaciones import get_puntos_de_vida, get_stat

def estadisticas_base(pokemon):
    print('\nEstadísticas base del Pokémon')
    print(f'- HP = {pokemon.pts_vida}')
    print(f'- Ataque = {pokemon.pts_ataque_fisico_base}')
    print(f'- Defensa = {pokemon.pts_defensa_fisica_base}')
    print(f'- Ataque especial = {pokemon.pts_ataque_especial_base}')
    print(f'- Defensa especial = {pokemon.pts_defensa_especial_base}')
    print(f'- Velocidad = {pokemon.pts_velocidad_base}')

def movimientos(pokemon):
    count = 0
    for x in pokemon.movimientos:
        print(f'{count} - {x}')
        count += 1

def estadisticas_lvl_50(pokemon): 
    print('\nEstadísticas base del Pokémon')
    print(f'El hp al nivel 50 de {pokemon.nombre} es {get_puntos_de_vida(pokemon.pts_vida)}')
    print(f'El atk al nivel 50 de {pokemon.nombre} es {get_stat(pokemon.pts_ataque_fisico_base)}')
    print(f'El def al nivel 50 de {pokemon.nombre} es {get_stat(pokemon.pts_defensa_fisica_base)}')
    print(f'El spa al nivel 50 de {pokemon.nombre} es {get_stat(pokemon.pts_ataque_especial_base)}')
    print(f'El spd al nivel 50 de {pokemon.nombre} es {get_stat(pokemon.pts_defensa_especial_base)}')
    print(f'El spe al nivel 50 de {pokemon.nombre} es {get_stat(pokemon.pts_velocidad_base)}')