saque = None
print('Bem vindo. Digite a quantia que deseja sacar ou digite "sair" para sair')
print('-'*72)
while True:
    saque = input('Digite quanto você deseja sacar: ')
    if saque == 'sair':
        break
    notas_de_cem = int(saque)//100
    novo_saldo = int(saque) - (notas_de_cem*100)
    notas_de_cinquenta = novo_saldo//50
    novo_saldo1 = novo_saldo - (notas_de_cinquenta*50)
    notas_de_vinte = novo_saldo1//20
    novo_saldo2 = novo_saldo1 - (notas_de_vinte*20)
    notas_de_dez = novo_saldo2//10
    novo_saldo3 = novo_saldo2 - (notas_de_dez*10)
    notas_de_cinco = novo_saldo3//5
    novo_saldo4 = novo_saldo3 - (notas_de_cinco*5)
    notas_de_dois = novo_saldo4//2
    novo_saldo5 = novo_saldo4 - (notas_de_dois*2)
    moedas_de_um = novo_saldo5//1
    print('Quantidade de notas de 100: ', notas_de_cem)
    print('-'*30)
    print('Quantidade de notas de 50: ', notas_de_cinquenta)
    print('-'*30)
    print('Quantidade de notas de 20: ', notas_de_vinte)
    print('-'*30)
    print('Quantidade de notas de 10: ', notas_de_dez)
    print('-'*30)
    print('Quantidade de notas de 5: ', notas_de_cinco)
    print('-'*30)
    print('Quantidade de notas de 2: ', notas_de_dois)
    print('-'*30)
    print('Quantidade de moedas de 1: ', moedas_de_um)
    print('-' * 30)
    print('')
