menu = """ 
===== Menu Principal =====
[1] Depositar
[2] Sacar
[3] Transferir
[4] Extrato
[5] Sair
==========================
"""
#variaveis da conta

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    print(menu)


    escolha = input("\nDigite a opção desejada: ")

    
    if escolha == "1":
        valor = float(input("\nInforme o valor do depósito: ")) 
    
        if valor > 0:
    
            saldo += valor

            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif escolha == "2":
        valor = float(input("\nInforme o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif escolha == "4":
        print("\n================ EXTRATO ================")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif escolha == "5":
        print("\nObrigado por utilizar nossos serviços")
        
        break