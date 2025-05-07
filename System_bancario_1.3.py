from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, tipo_transacao, valor):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco,):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

        @classmethod
        def nova_conta(cls, numero, cliente):
            return cls(numero, cliente)
        
        @property
        def saldo(self):
            return self.saldo
        
        @property
        def agencia(self):
            return self.agencia
        
        @property
        def numero(self):
            return self.numero
        
        @property
        def cliente(self):
            return self.cliente
        
        @property
        def historico(self):
            return self.historico
        
        def sacar(self, valor):
            saldo = self.saldo
            excedeu_saldo = valor > saldo

            if excedeu_saldo:
                print("Saldo insuficiente")

            elif valor > 0:
                saldo -= valor
                print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
                return True
            
            else:
                print("Falha na operação, valor invélido para saque")
                return False
            
        def depositar(self, valor):
            if valor > 0:
                self.saldo += valor
                print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
                return True
            
            else:
                print("Falha na operação, valor inválido para depósito")
                return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
        
    def sacar(self, valor):
        numero_saques - len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque

        if excedeu_limite:
            print("Limite de saque excedido")
            return False
        elif excedeu_saques:
            print("Número máximo de saques diários excedido")
            return False
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
        Agência: \t {self.agencia}
        Conta: \t {self.numero}
        Cliente: \t {self.cliente.nome}    
        """
    
class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    
    @property
    def valor(self):
        pass

    @classmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)          

def menu():
    menu = """
    ___________MENU___________

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))    

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuparar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.")
        return None
    
    return cliente.contas[0]

def depositar(clientes):

    cpf = input(f"Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuparar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)




    cliente = input("Informe o nome do cliente: ")
    
    for cliente in clientes:
        if cliente.nome == cliente:
            conta = ContaCorrente.nova_conta(cliente.numero, cliente)
            deposito = Deposito(valor)
            deposito.registrar(conta)
            break
    else:
        print("Cliente não encontrado.")

def sacar(clientes):
    cpf = input(f"Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return
    
    valor = float(input("\n Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuparar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input(f"Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return
    
    conta = recuparar_conta_cliente(cliente)
    if not conta:
        return
    
    print(f"\n Extrato da conta {conta.numero} - {conta.cliente.nome}")
    transacao = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas transações."
    else:
        for transacao in transacoes:
            extrato += f"{transacao['data']} - {transacao['tipo']} - {transacao['valor']:.2f}\n"
   
    print(extrato)
    print(f"\nSaldo atual: {conta.saldo:.2f}")
    print("==========================================")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado, fluxo de criação de conta encerrado.")
        return
    
    conta = ContaCorrente.nova_conta(clinete=cliente, numero_conta=numero_conta)
    contas.append(conta)
    clientes.conta.append(conta)

    print(f"Conta {conta.numero} criada com sucesso!")

def listar_contas(contas): 
    for conta in contas:
        print( "=" * 100)
        print(textwrap.dedent(str(conta)))

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n Já existe cliente com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")
    
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)

    print("\n Cliente criado com sucesso!")

def main():

    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)
         
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break

        else:
            print("Opção inválida. Tente novamente.")

main()