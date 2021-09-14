par = 0

for n in range(5):
    n = int(input())  #tinha colocado o nome 'valor' na variável e o uri não aceitava
    if n%2 == 0:
        par += 1
print(f'{par} valores pares')
