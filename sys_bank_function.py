#O sistema tem apenas 1 usuário. Portanto, não precisa identificar agencia e conta

#Regras para depósito:
#O sistema deve permitir depositar apenas valores positivos. 
#Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

#Regras para saque:
#O sistema deve permitir no máximo 3 saques diários. | O limite por saque é de R$ 500,00
#Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não sera possível sacar o dinheiro por falta de saldo
#Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.
#Regras para extrato:
#O extrato deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta
#Os valores devem ser exibidos no formato "R$ xxx.xx"

from colorama import init, Fore, Style

# Inicializa o colorama para suporte a ANSI no terminal
init(autoreset=True)


# Constantes
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUES = 500

# Variáveis globais
saldo= 0
extrato = ""
numero_saques = 0

menu = """\n
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

def depositar(saldo, extrato):
    #Função para depósito
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
        print(Fore.GREEN + "Depósito realizado com sucesso!")
    else:
        print(Fore.RED + "Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    #Função para saque
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_VALOR_SAQUES
    excedeu_saques = numero_saques>= LIMITE_SAQUES

    if excedeu_saldo:
        print(Fore.RED + "Operação falhou! Você não possui saldo o suficiente.")
    elif excedeu_limite:
        print(Fore.RED + "Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print(Fore.RED + "Operação falhoou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor: .2f}\n"
        numero_saques += 1
        print(Fore.GREEN + "Saque realizado com sucesso!")
    else:
        print(Fore.RED + "Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    #Função para exibição do extrato
    print("\n============== Extrato ==============\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo: .2f}")
    print("\n=====================================\n")

# Loop principal
while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
    elif opcao == "4":
        print(Fore.YELLOW + "Saindo do sistema...")
        break

    else:
        print(Fore.RED + "Operação inválida! Por favor, selecione novamente.")
