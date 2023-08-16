import math

#Usuario escreve o CPF
MaxNumCPF = 11
contador1 = 10
contador2 = 10
Soma1 = 0
Soma2 = 0

def InputUser(mensagem):
    while True:
        UserCPF = input(mensagem)
        if UserCPF.isdigit() and len(UserCPF) == 11:  # Verifica se a entrada tem 11 dígitos
            cpf_numeros = [int(digito) for digito in UserCPF]  # Cria uma lista com os dígitos do CPF
            return cpf_numeros
        

        else:
            print("Entrada inválida.")


cpf_lista = InputUser("Digite o CPF (11 dígitos): ")
lista_origem = cpf_lista

if cpf_lista:
    cpf_lista = cpf_lista[:-2]
    for numero in cpf_lista:
        Teste1 = numero * contador1
        contador1 -= 1
        #print(Teste1) 
        Soma1 += Teste1
        #print(Soma1)
    verificacao1 = math.ceil((Soma1 / 11) - 11)
    #print(verificacao1)

    

    #print("CPF digitado:", cpf_lista)
    #print("A função foi concluída com sucesso.")
else:
    print("A função não foi concluída.")

cpf_lista2 = cpf_lista
if verificacao1 == lista_origem[9]:
    #print("ok")
    cpf_lista2.append(verificacao1)
    cpf_lista2.pop(0)
    #print(cpf_lista2)

    for numero in cpf_lista2:
        Teste2 = numero * contador2
        contador2 -= 1
        #print(Teste2) 
        Soma2 += Teste2
        #print(Soma2)
        verificacao2 = math.ceil((Soma2 / 11) - 11)
        #print(verificacao2)
else:
    print('sheeeeeeesh')


testeFinal = verificacao2 - verificacao1
print(testeFinal)

if testeFinal == lista_origem[10]:
    print("ZERADO")

