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


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
"""variáveis em maiúsculas representam constantes. Em python não tem uma palavra reservada para indicar uma constante, por isso
usa-se declarar a variável com letras maiúsculas, como um lembrete de que esse valor não deve ser alterado."""


while True:
    opcao = input(menu)

    if opcao =="d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao=="s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou!\nVocê não possui saldo o suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou!\nO valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operaçao falhou!\nNúmero máximo de saques excedido.")
        
        elif valor > 0:
            saldo-= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou!\nO valor informado é inválido")

    elif opcao =="e":
        print("\n============== Extrato ==============\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=====================================\n")
    elif opcao =="q":
        break
    else:
        print("Operação inválida!!!\nPor favor selecione novamente a opção desejada:")
