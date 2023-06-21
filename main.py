import encoder
from encoder import *
title = 'Bienvenido a mi codificador'
print(title + '\n' + len(title) * '-')

while True:
    option = input('\n1.Ingrese la frase\n2.Ingrese la llave\n3.Codificar\n4.Descodificar\n5.Salir\nSeleccione una opcion:')

    if option == '1':
        phrase = input('Ingrese la frase:')
        phrase = encoder.array(phrase)
        print(phrase)

    elif option == '2':
        key_matrix = []

        for i in range(0,3):
            row = input('Ingrese la fila: ')
            row = row.split()
            for r in range(len(row)):
                row[r] = int(row[r])
            key_matrix.append(row)
            print('La llave es {}'.format(key_matrix))


    elif option == '3':
        cifrado = encoder.codificar(phrase, key_matrix)
        print(cifrado)

    elif option == '4':
        print(encoder.decodificar(cifrado, key_matrix))


    elif option == '5':
        print('Saliendo del programa....')
        break
    else:
        print('Error, por favor ingrese una opcion valida')