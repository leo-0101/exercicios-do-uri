qtdeLaco = int(input())

qtdeRatos = 0
qtdeCoelhos = 0
qtdeSapos = 0
totalCobaias = 0

for valor in range(qtdeLaco):
    qtde, tipo = input().split()
    qtde = int(qtde)
    totalCobaias += qtde
    if tipo == 'R':
        qtdeRatos += qtde
    elif tipo == 'C':
        qtdeCoelhos += qtde
    elif tipo == 'S':
        qtdeSapos += qtde
print(f'Total: {totalCobaias}')
print(f'Total de coelhos: {qtdeCoelhos}')
print(f'Total de ratos: {qtdeRatos}')
print(f'Total de sapos: {qtdeSapos}')
print(f'Percentual de coelhos: {(qtdeCoelhos / totalCobaias) * 100:.2f}%')
print(f'Percentual de ratos: {qtdeRatos / totalCobaias * 100:.2f}%')
print(f'Percentual de ratos: {qtdeSapos / totalCobaias * 100:.2f}%')