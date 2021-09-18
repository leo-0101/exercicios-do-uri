a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

# a estrategia é testar todos os valores com todos para descobrir a ordem crescente dos valores
if((a < b) and (b < c)):
    print(f'{a}\n{b}\n{c}')
elif((a < c) and (c < b)):
    print(f'{a}\n{c}\n{b}')
elif((b < c) and (c < a)):
    print(f'{b}\n{c}\n{a}')
elif((b < a) and (a < c)):
    print(f'{b}\n{a}\n{c}')
elif((c < a) and (a < b)):
    print(f'{c}\n{a}\n{b}')
else:
    print(f'{c}\n{b}\n{a}')

print(f'\n{a}\n{b}\n{c}')
