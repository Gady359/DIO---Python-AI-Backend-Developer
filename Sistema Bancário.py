def menu():
    menu="""

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """
    return input(menu)

def deposito(saldo,valor,extrato, /):
    print("Deposito")

    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Sucesso")
    else:
        print("Valor invalido")

    return saldo, extrato

def saque(*,saldo,valor,extrato, lim_saq, limite,num_saq):
    print("Saque")
    if valor > 0 and num_saq < lim_saq:
                if valor <= limite and valor <= saldo:
                    saldo -= valor
                    num_saq += 1
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    print("Sucesso")
                else:
                    print("Saque excede limite ou saldo insuficiente")
    else:
        print("Valor de saque inválido ou limite de saques excedido")

    return saldo, extrato


def Mostrar_extrato(saldo, /, *,extrato):
     print("Extrato")
     print("Nao foi realizado nehuma movimentacao" if not extrato else extrato)
     print(f"\nSaldo:\t\tR$ {saldo:.2f}")
     

def main():
    saldo = 0
    limite = 500
    extrato =""
    num_saq = 0
    lim_saq = 3
    contas=[]
    clientes=[]

    agencia="0001"

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Quanto deseja depositar?"))
            saldo,extrato=deposito(saldo,valor,extrato)

        elif opcao == "s":
            
            valor = float(input("Quanto deseja sacar?"))

            saldo,extrato =saque(
                 saldo=saldo,
                 valor=valor,
                 extrato=extrato,
                 limite=limite,
                 num_saq=num_saq,
                 lim_saq=lim_saq,
            )

            

        elif opcao == "e":
            Mostrar_extrato(saldo,extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Opcao invalida")

main()