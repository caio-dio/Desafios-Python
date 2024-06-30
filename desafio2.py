# Segundo desafio de programação em Python implementando funções no sistema bancário
import textwrap

menu = """

[d] \tDepositar
[s] \tSacar
[e] \tExtrato
[c] \tNova Conta
[u] \tNoco Usuário
[l] \tListar Contas
[q] \tSair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"




def fdepositar(saldof, valorf, extratof, /):
    if valorf > 0:
        saldof += valorf
        extratof += f"Depósito: R$ {valorf:.2f}\n"
        print(f"Deposito efetuado com sucesso, seu saldo é R$ {saldof:.2f}\n")
        op = input ("Gostaria de ver o seu extrato? (s para SIM e N para Não) ")
        if op == "s":
            fextrato(saldof, extratof=extratof)
        return saldof, extratof
    else:
        print("Operação falhou! O valor informado é inválido.")

def fsacar(*, saldof, valorf, extratof, limitef, numero_saquesf, limite_saquesf):
    global numero_saques
    excedeu_saldo = valorf > saldof
    excedeu_limite = valorf > limitef
    excedeu_saques = numero_saquesf >= limite_saquesf

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valorf > 0:
        saldof -= valorf
        extratof += f"Saque: R$ {valorf:.2f}\n"
        numero_saques += 1
        print(F"Operação com sucesso! O valor {valorf:.2f} foi sacado")
        op = input ("Gostaria de ver o seu extrato? (s para SIM e N para Não) ")
        if op == "s":
            fextrato(saldof, extratof=extratof)
        return saldof, extratof

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldof, extratof


def fextrato(saldof, /, *, extratof):
    print("Em desenvolvimento")
    print("\n================ EXTRATO Banco Caio ================")
    print("Não foram realizadas movimentações." if not extratof else extratof)
    print(f"\nSaldo: R$ {saldof:.2f}")
    print("====================================================")

def fcriarusuario(usuariosf):
    abertura = "Cadastro de novos usuários"
    print(abertura.center(75,"="))
    cpf = input("Informe o CPF (somente número): ")
    usuario = ffiltrar_usuario(cpf, usuarios)
    if usuario:
        print("\n Usuário já existe usuário com esse CPF! ")
        return
    # Se ele não existir efetua o cadastro do usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===\n")

def ffiltrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def fcriarconta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = ffiltrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===\n")
        #print(f"Agencia = {agencia}, conrta = {numero_conta}, usuário = {usuario}\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")


def flistarcontas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



# ----------------- Corpo -----------------
inicial = "Inicio do terminal bancario avançado"
print(inicial.center(75,"="))

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = fdepositar(saldo, valor, extrato)
        #utilizando função

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = fsacar(saldof=saldo, valorf=valor, extratof=extrato, limitef=limite, numero_saquesf=numero_saques, limite_saquesf=LIMITE_SAQUES)
        #utilizando função

    elif opcao == "e":
        fextrato(saldo, extratof=extrato)
        #utilizando função

    elif opcao == "u":
        fcriarusuario(usuarios)
        #print(usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = fcriarconta(AGENCIA, numero_conta, usuarios)
        if conta:
                contas.append(conta)

    elif opcao == "l":
        flistarcontas(contas)


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
