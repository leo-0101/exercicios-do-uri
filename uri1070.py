cont = 0
n = int(input())
while cont < 6:
    if n% 2 != 0:   # se o input for ímpar
        print(n)
        cont += 1 # e adiciona mais 1 na contadora até cehagar no 6 e o programa parar
    n += 1 # e adiciona mais um na varável pra assim sempre mostrar números ímpares

