import numpy as np


def array (phrase):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    matrix = []

    characters = []
    for character in phrase:
        characters.append(character)

    fila = []
    for n, c in enumerate(characters):
        fila.append(abc.index(c)+1)
        if ((n+1) % 3) == 0:
            matrix.append(fila)
            fila = []

    a = np.array(matrix)
    matrix = a.transpose()

    return matrix

def codificar(phrase, key):
    b = np.array(key)
    e = np.matmul(b, phrase)
    return e

def decodificar(phrase, key):
    key = np.array(key)

    matriz_inversa = np.linalg.inv(key)

    d = np.matmul(matriz_inversa, phrase)

    return d