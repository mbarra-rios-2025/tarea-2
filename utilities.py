import csv
import random

from pokemon import Pokemon

def get_pokemon(nombre):
    with open('pokemon_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        for i in range(len(rows)):
            if nombre.lower() == rows[i][0]:
                pokemon = Pokemon(
                    rows[i][0],
                    rows[i][1],
                    int(rows[i][2]),
                    int(rows[i][3]),
                    int(rows[i][4]),
                    int(rows[i][5]),
                    int(rows[i][6]),
                    int(rows[i][7]),
                    rows[i][8].split(';')
                )
    return pokemon

# @file = nombre del archivo tabla_efectividad
def get_tabla_efectividad(file):
    tabla_efectividad = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        for x in rows:
            tabla_efectividad.append(x)
    return tabla_efectividad