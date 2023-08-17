MaxNumCPF = 11             # Numero maximo de caracteres para o CPF
contador_1 = 10            # Contador da conta da primeira verificação
contador_2 = 10            # Contador da conta da segunda verificação
Soma_1 = 0                 # Soma necessaria para primeira verificação 
Soma_2 = 0                 # Soma necessaria para segunda verificação


def InputUser(mensagem): 
    while True:
        UserCPF = input(mensagem)
        #verifica se tem somente digitos e tem exatamente 11 caracteres
        if UserCPF.isdigit() and len(UserCPF) == 11:  # Verifica se a entrada tem 11 dígitos
            cpf_numeros = [int(digito) for digito in UserCPF]  # Cria uma lista com os dígitos do CPF
            return cpf_numeros
    
        else:
            print("Entrada inválida. Tente novamente")


CPF_lista = InputUser("Digite o CPF (11 dígitos): ")
lista_origem = CPF_lista

#Conta da verificação do 10° digito do CPF
if CPF_lista:
    CPF_lista = CPF_lista[:-2]
    for numero in CPF_lista:
        Teste_1 = numero * contador_1
        contador_1 -= 1 
        Soma_1 += Teste_1
    verificacao_1 = (Soma_1 % 11)
else:
    print("A função não foi concluída.")

#Verifica se a sobra é menor que 2. se for, o 10° digito é 0
if verificacao_1 < 2:
    testeFinal_1 = 0
else:
    testeFinal_1 = 11 - verificacao_1


#Conta da verificação do 11° digito
CPF_lista_2 = CPF_lista

#Confirmação da conta do 10° digito
if testeFinal_1 == lista_origem[9]:
    CPF_lista_2.append(testeFinal_1)
    CPF_lista_2.pop(0)

    for numero in CPF_lista_2:
        Teste_2 = numero * contador_2
        contador_2 -= 1
        Soma_2 += Teste_2
        verificacao_2 = (Soma_2 % 11)

else:
    print('sheeeeeeesh')

#Verifica se a sobra é menor que 2. se for, o 11° digito é 0
if verificacao_2 < 2:
    testeFinal_2 = 0
else:
    testeFinal_2 = 11 - verificacao_2


#Confirmação da conta do 11° digito. 
if testeFinal_2 == lista_origem[10]:
    print("CPF VALIDO")
else:
    print("CPF INVALIDO")
