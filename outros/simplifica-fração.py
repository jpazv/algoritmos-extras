def simplifica(numerador, denominador):
    lista = []
    for numero in range(1, numerador+1):
        if denominador % numero == 0 and numerador % numero == 0:
            lista.append(numero)
    return numerador/max(lista), denominador/max(lista)
