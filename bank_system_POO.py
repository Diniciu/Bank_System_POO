menu = """
====================Operações====================
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] CRIAR USUÁRIO
[5] CRIAR CONTA CORRENTE
[6] LISTAR CONTAS
[0] SAIR
=> """

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def saldo(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(saldo=0.0, numero=numero, agencia="0001", cliente=cliente, historico=Historico())

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return False
        elif valor <= 0:
            print("Valor inválido! Tente novamente.")
            return False
        else:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque: R${valor:.2f}")
            return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido! Tente novamente.")
            return False
        else:
            self.saldo += valor
            self.historico.adicionar_transacao(f"Depósito: R${valor:.2f}")
            return True

class Conta_Corrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Saldo insuficiente!")
            return False
        elif valor <= 0:
            print("Valor inválido! Tente novamente.")
            return False
        elif self.numero_saques >= self.limite_saques:
            print("Limite de saques excedido!")
            return False
        else:
            self.saldo -= valor
            self.numero_saques += 1
            self.historico.adicionar_transacao(f"Saque: R${valor:.2f}")
            return True

usuarios = []
contas_correntes = []
numero_agencia = "0001"

def depositar(conta, valor):
    if conta.depositar(valor):
        print("Depósito realizado com sucesso!")
    else:
        print("Falha ao realizar depósito.")

def sacar(conta, valor):
    if conta.sacar(valor):
        print("Saque realizado com sucesso!")
    else:
        print("Falha ao realizar saque.")

def mostrar_extrato(conta):
    print("\n===============EXTRATO===============")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in conta.historico.transacoes:
            print(movimento)
    print(f"\nSaldo: R${conta.saldo:.2f}")
    print("======================================")

def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere não numérico do CPF
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Usuário já existe!")
            return
    usuarios.append(Cliente(nome, data_nascimento, cpf, endereco))
    print("Usuário criado com sucesso!")

def criar_conta_corrente(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere não numérico do CPF
    for usuario in usuarios:
        if usuario.cpf == cpf:
            numero_conta = f"{len(contas_correntes) + 1:04d}"
            conta = Conta_Corrente(0.0, numero_conta, numero_agencia, usuario, Historico(), 500, 3)
            contas_correntes.append(conta)
            print(f"Conta corrente {numero_conta} criada com sucesso!")
            return
    print("Usuário não encontrado!")

def listar_contas():
    if not contas_correntes:
        print("Nenhuma conta encontrada.")
    else:
        print("\n===============CONTAS===============")
        for conta in contas_correntes:
            usuario = conta.cliente
            print(f"Agência: {conta.agencia}, Número da Conta: {conta.numero}, Usuário: {usuario.nome}, CPF: {usuario.cpf}")
        print("======================================")

while True:
    opcao = input(menu)
    
    if opcao == '1':
        numero_conta = input("Digite o número da conta: ")
        valor = float(input("Digite o valor do depósito: R$"))
        conta = next((c for c in contas_correntes if c.numero == numero_conta), None)
        if conta:
            depositar(conta, valor)
        else:
            print("Conta não encontrada.")
    
    elif opcao == '2':
        numero_conta = input("Digite o número da conta: ")
        valor = float(input("Digite o valor do saque: R$"))
        conta = next((c for c in contas_correntes if c.numero == numero_conta), None)
        if conta:
            sacar(conta, valor)
        else:
            print("Conta não encontrada.")
    
    elif opcao == '3':
        numero_conta = input("Digite o número da conta: ")
        conta = next((c for c in contas_correntes if c.numero == numero_conta), None)
        if conta:
            mostrar_extrato(conta)
        else:
            print("Conta não encontrada.")
    
    elif opcao == '4':
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário (logradouro, número, bairro, cidade/sigla do estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
    
    elif opcao == '5':
        cpf = input("Digite o CPF do usuário para vincular a conta corrente: ")
        criar_conta_corrente(cpf)
    
    elif opcao == '6':
        listar_contas()
    
    elif opcao == '0':
        print("Fim do programa.")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
