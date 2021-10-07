numero_romano = input('Digite um número em romano: ')
somatorio = []
lista = list(numero_romano)

for item in lista:
    if item == 'I':
        if lista.count('X') == 2:
            try:
                if lista.index('I') < lista.index('X')+2:
                    somatorio.append(-2)
            except:
                pass
        if lista.count('X') == 3:
            try:
                if lista.index('I') < lista.index('X')+3:
                    somatorio.append(-2)
            except:
                pass
        if lista.count('X') == 4:
            try:
                if lista.index('I') < lista.index('X') + 4:
                        somatorio.append(-2)
            except:
                pass
        somatorio.append(1)
        item2 = 'V'
        itemx = 'X'
        try:
            if lista.index('I') < lista.index('V'):
                somatorio.append(-2)
        except:
            pass
        try:
            if lista.index('I') < lista.index('X'):
                somatorio.append(-2)
        except:
            pass
    if item == 'V':
        somatorio.append(5)
        item3 = 'X'
        try:
            if lista.index('V') < lista.index('X'):
                somatorio.append(-10)
        except:
            pass
    if item == 'X':
        somatorio.append(10)
        item4 = 'L'
        itemi = 'I'
        try:
            if lista.index('X') < lista.index('L'):
                somatorio.append(-10)
        except:
            pass
    if item == 'L':
        somatorio.append(50)
        item5 = 'C'
        if lista.count('X') == 2:
            try:
                if lista.index('L') > lista.index('X'):
                    somatorio.append(-2)
            except:
                pass
        try:
            if lista.index('L') < lista.index('C'):
                somatorio.append(-100)
        except:
            pass
    if item == 'C':
        if lista.count('X') == 2:
            try:
                if lista.index('C') > lista.index('X'):
                    somatorio.append(-2)
            except:
                pass
        somatorio.append(100)
        item6 = 'D'
        itemx = 'X'
        try:
            if lista.index('C') < lista.index('D'):
                somatorio.append(-200)
        except:
            pass
        try:
            if lista.index('X') < lista.index('C'):
                somatorio.append(-20)
        except:
            pass

print(sum(somatorio))