def menu():
    menu="""

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [nu] Novo Cliente
    [nc] Nova Conta
    [lc] Listas Contas
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
     
def criar_cliente(clientes):
     cpf= input("Informe seu CPF(somente numero): ")
     cliente =filtrar_cliente(cpf,clientes)

     if cliente:
        print("Cliente ja existente com esse CPF!!!")
        return
     
     nome=input("Nome Completo:")
     data_nasc=input("Data de nascimento(dd-aa-aaaa): ")
     endereco=input("Endereco (logradouro, num - bairro - cidade/sigla estado): ")

     clientes.append({"nome": nome, "data_nasc": data_nasc, "cpf":cpf, "endereco": endereco})

     print("Sucesso")
        
def filtrar_cliente(cpf, clientes):
    clientes_filtered=[cliente for cliente in clientes if cliente["cpf"]== cpf]
    return clientes_filtered[0] if clientes_filtered else None

def criar_conta(agencia,num_conta,clientes):
    cpf=input("informe o CPF: ")
    cliente =filtrar_cliente(cpf,clientes)

    if cliente:
        print("Conta criada com sucesso")
        return {"agencia": agencia,"num_conta":num_conta,"cliente":cliente}
    
    print("Cliente nao encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha=f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['num_conta']}
            Titular:\t{conta['cliente']['nome']}
            """
        print("="* 20)
        print(linha)



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

        elif opcao=="nu":
            criar_cliente(clientes)

        elif opcao=="nc":
            num_conta =len(contas)+1
            conta = criar_conta(agencia,num_conta,clientes)

            if conta:
                contas.append(conta)

        elif opcao=="lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opcao invalida")

main()