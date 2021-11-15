nome = input().upper()
salario_fixo = float(input())
total_vendas_mes = float(input())

comissao = 15 * total_vendas_mes / 100

sal_total = salario_fixo + comissao
print(f'TOTAL = R$ {sal_total:.2f}')
