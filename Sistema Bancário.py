menu="""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
num_saq = 0
lim_saq = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        deposito = float(input("Quanto deseja depositar?"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("Valor invalido")

    elif opcao == "s":
        print("Saque")
        saque = float(input("Quanto deseja sacar?"))

        if saque > 0 and num_saq < lim_saq:
            if saque <= limite and saque <= saldo:
                saldo -= saque
                num_saq += 1
                extrato += f"Saque: R$ {saque:.2f}\n"
            else:
                print("Saque excede limite ou saldo insuficiente")
        else:
            print("Valor de saque inválido ou limite de saques excedido")

    elif opcao == "e":
        print("Extrato")
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Opcao invalida")