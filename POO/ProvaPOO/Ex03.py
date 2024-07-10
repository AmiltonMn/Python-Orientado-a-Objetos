class Banco:
    quantidadeDeContas = 0
    def __init__(self, NomeCliente, NumeroAgencia, NumeroConta, SaldoCliente, TipoConta):
        self.__NomeCliente = NomeCliente
        self.__NumeroAgencia = NumeroAgencia
        self.__NumeroConta = NumeroConta
        self.__SaldoCliente = SaldoCliente
        self.__TipoConta = TipoConta
    def getNome(self):
        return self.__NomeCliente
    def getAgencia(self):
        return self.__NumeroAgencia
    def getConta(self):
        return self.__NumeroConta
    def getSaldo(self):
        return self.__SaldoCliente
    def getTipo(self):
        return self.__TipoConta
    
    # @staticmethod
    # def QuantidadeContas(quantidadeDeContas):

conta1 = Banco('Amilton', 1234, 123456, 100, 'Corrente')
print(conta1.getNome())
print(conta1.getAgencia())
print(conta1.getConta())
print(f'Seu saldo é de R${conta1.getSaldo()} reais')
print(conta1.getTipo())
conta2 = Banco('José', 4321, 654321, 150, 'Poupança')
print(conta2.getNome())
print(conta2.getAgencia())
print(conta2.getConta())
print(f'Seu saldo é de R${conta2.getSaldo()} reais')
print(conta2.getTipo())