# lê dois valores na mesma linha
# quebra os valores por espaço
# o primeiro valor digitado coloca em 'codigo'
# o segundo coloca em 'qtde'

total = 0
# foi necessário adicionar essa variável
# com um valor 0 para que não seja produzido um valor
# incorreto de total quando o usuário digitar um código inexistente.

codigo, qtde = input().split()

codigo = int(codigo)
qtde = int(qtde)

if codigo == 3:
    total = qtde * 5
elif codigo == 5:
    total = qtde * 1.5
elif codigo == 1:
    total = qtde * 4.0
elif codigo == 2:
    total = qtde * 4.5
elif codigo == 4:
    total  = qtde * 2
# enquanto o código não é algo válido, a variável 'total'
# sempre terá o valor '0'. Desta forma, vamos utilizá-la
# para descobrir se há algum valor a ser cobrado pelo usuário
if total != 0:
    print(f'Total: R$ {total:.2f}')
else:
    print('Insira um código válido, deixe de gracinha!')

# VERSAO 2

codigo, qtde = input().split()

codigo = int(codigo)
qtde = int(qtde)

if codigo == 3:
    total = qtde * 5
elif codigo == 5:
    total = qtde * 1.5
elif codigo == 1:
    total = qtde * 4.0
elif codigo == 2:
    total = qtde * 4.5
elif codigo == 4:
    total = qtde * 2
    print(f'Total: R$ {total:.2f}')
elif codigo >= 5 and qtde <= 0:
    print('Esse código não existe, porra!')