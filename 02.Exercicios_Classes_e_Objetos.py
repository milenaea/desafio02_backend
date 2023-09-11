# 1. O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os   requisitos abaixo.


from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self.__renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError("Tipo da variável deve ser str")
        self._nome = novo_nome

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, novo_tel):
        if not isinstance(novo_tel, str):
            raise TypeError("Tipo da variável deve ser str")
        self._telefone = novo_tel

    @property
    def renda_mensal(self):
        return self.__renda_mensal
    
    @abstractmethod
    def tem_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def tem_cheque_especial(self):
        return True
        
class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def tem_cheque_especial(self):
         return False
        
class ContaCorrente:
    def __init__(self, titular):
        self.__saldo = 0.0
        self.__operacoes = []
        self.__titulares = []
        self.adicionar_titular(titular)

    def adicionar_titular(self, titular):
        self.__titulares.append(titular)

    def depositar(self, valor: float):
        self.__saldo += valor
        self.__operacoes.append(f"Deposito de R$ {valor:.2f}")

    def sacar(self, valor: float):
        titular = self.__titulares[0]
        if not titular.tem_cheque_especial():
            if valor <= self.__saldo:
                self.__saldo -= valor
                self.__operacoes.append(f"Saque de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo insuficiente")
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def operacoes(self):
        return self.__operacoes

cliente_mulher = ClienteMulher("Melry", "829252", 17.987)
cliente_homem = ClienteHomem("Elvis", "834252", 987)

conta1 = ContaCorrente(cliente_mulher)
conta2 = ContaCorrente(cliente_homem)

print(conta1.saldo)
print(conta2.saldo)

conta1.depositar(5000)
conta2.depositar(389)

print(conta1.saldo)
print(conta2.saldo)

conta1.sacar(1574)
conta2.sacar(220)