menu = """

Selecione uma das opções para seguir:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair



=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)
	
    if opcao == "d":
		
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")
		
        else:
            print("\nOperação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        saque = float(input("Informe o valor para saque: "))

        if saque > saldo:
            print("\nOperação inválida! Saldo insuficiente em conta.")

        elif saque > limite_saque:
            print("\nOperação inválida! O valor do saque excede o limite.")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("\nOperação inválida! Limite de saques excedido.")

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R${saque:.2f}\n"
            print("\nSaque realizado com sucesso.")
        
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            

    elif opcao == "e":
       print("\n==========EXTRATO==========")
       print()
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R${saldo:.2f}")
       print("===========================")

    elif opcao == "q":
       break

    else:
        print("\nOperação inválida, por favor selecione a opção desejada.")