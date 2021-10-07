def printCedulas(numero):
    num = [1, 2, 5, 10, 20, 50, 100]
    cedulas = ['Moeda de 1', 'Nota de 2', 'Nota de 5', 'Nota de 10', 'Nota de 20', 'Nota de 50', 'Nota de 100']
    i = 6
    while numero:
        div = numero//num[i]
        numero %= num[i]

        while div:
            print(cedulas[i], end='\n')
            div -= 1
        i -= 1
