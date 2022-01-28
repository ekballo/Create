# Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))


if n1 > n2 and n2 > n1:
    print('Entre os nunmeros digtados o {} é o maior!'.format(n1))
else:
    print('Entre os nunmeros digitos o {} é o maior !'.format(n2))