#Crie um programa que solicita ao usuário uma senha e em seguida compare esse valor
#com uma senha armazenada em uma variável. Enquanto o usuário não acertar o valor
#da senha o programa deverá solicitar a senha ao usuário. Quando o usuário acerta a
#senha, o programa deverá encerrar exibindo uma mensagem encerramento e informar
#que o usuário acertou a senha.

valor = int(input('Digita sua senha: '))
senha = 20
while valor != senha:
    valor = int(input('Digita sua senha: '))
print('Senha correta!')
print('Fim do programa!')    


