negativo = 0
positivo = 0

for n in range(6):
    n = float(input('Insira os valores: '))
    if n < 0:
        negativo += 1
    else:
        positivo += 1

print(f'negativo: {negativo}')
print(f'{positivo} valores positivos')
