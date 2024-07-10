#Escreva um programa que solicita ao usuário um valore numérico inteiro positivo e, em
#seguida, calcule o fatorial desse número usando um loop do tipo while. Ao final o
#programa deverá exibir o valor do fatorial do número informado pelo usuário e término
#do programa.

numero = int(input("Digite um número inteiro que deseje fatorar: "))

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)
print('Fim do programa')