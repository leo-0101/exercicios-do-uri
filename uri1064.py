s = 0
positivo = 0

for n in range(6):
    n = float(input('Insira os valores: '))
    if n > 0:  # se n for postivo
        positivo += 1
        s = s + n  # as duas variáveis são somadas para calcular a média

print(f'{positivo} valores positivos')
print(f'{s / positivo:.1f}')  # é feita a divisão para mostrar a média
