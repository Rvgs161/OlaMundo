#Validador de CPF - Python#
Este é um programa simples em Python que implementa um validador de CPF (Cadastro de Pessoa Física) de acordo com o algoritmo de validação utilizado no Brasil. O código verifica a autenticidade de um CPF inserido pelo usuário, realizando cálculos específicos nos dígitos verificadores.

Funcionamento
O programa solicita que o usuário insira um CPF de 11 dígitos. Em seguida, ele realiza as seguintes etapas:

**Validação de Entrada:** O programa verifica se a entrada contém somente dígitos e se possui exatamente 11 caracteres.

**Cálculo do 10º Dígito Verificador:** Calcula a soma ponderada dos primeiros nove dígitos do CPF, aplicando um contador específico. Em seguida, calcula o dígito verificador e verifica se ele corresponde ao dígito original.

**Cálculo do 11º Dígito Verificador:** Se o 10º dígito verificador for válido, o programa remove o primeiro dígito do CPF e calcula a soma ponderada dos dígitos restantes, aplicando um segundo contador. Calcula o dígito verificador e verifica sua validade.

**Resultado da Validação:** Com base nos cálculos dos dígitos verificadores, o programa informa se o CPF inserido é válido ou inválido.

**Como Usar**
Certifique-se de ter o Python instalado em seu sistema.
Execute o programa e siga as instruções para inserir um CPF.
O programa exibirá uma mensagem indicando se o CPF é válido ou inválido.
