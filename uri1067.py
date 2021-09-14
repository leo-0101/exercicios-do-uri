#quero ler um valor, e em seguida mostrar os numeros impares ate esse valor
#ex 8: 1 3 5 7

val = int(input('Digite um valor inteiro: '))
cont = 1 # inicializa um contador

while cont <= val: # se o contador for menor ou igual a val, verifico se ele é ímpar
    if cont % 2 != 0: # se é um número ímpar, imprima
        print(cont)
    cont += 1 # ele fica dentro do if caso for verdadeiro pra contar mais
              # assim ele vai dar um loop até o número inserido se for preciso