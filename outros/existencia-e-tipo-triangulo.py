def is_triangle(lado1, lado2, lado3):
    if lado1+lado2 < lado3 or lado1+lado3 < lado2 or lado2+lado3 < lado1:
        return False
    return True


def tipo_de_triangulo(lado1, lado2, lado3):
    if is_triangle(lado1, lado2, lado3) is True:
        if lado1 != lado2 and lado2 != lado3:
            return 'Triângulo escaleno'
        if lado1 == lado2 and lado2 != lado3 or lado2 == lado3 and lado1 != lado2:
            return 'Triângulo isósceles'
        return 'Triângulo equilátero'
    return False




