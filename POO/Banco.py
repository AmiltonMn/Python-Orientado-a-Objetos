import random
import time
def tempo():
    time.sleep(1)
saldo = 0
# Classe pai
class conta:
    def __init__(self):
        self._saldo = 0
        nome = ''
        conta = 0000
        agencia = 00000-0
        pass

    # Abertura de Contas
    def AberturaContas():
        agencia = random.randint(0000, 9999)
        conta = random.randint(000000, 999999)
        InfoConta = [agencia, conta]
        print(f'Estamos fazendo a abertura da sua conta {tipo}')
        print('Carregando...')
        tempo()  
        print(f'Seu nome é: {nome}')
        print(f'Sua agência é {InfoConta[0]}')
        print(f'Sua conta é {InfoConta[1]}')

    # Consulta de Saldo   
    def consultaSaldo(self):
            print('Carregando...')
            tempo() 
            print(f'Seu saldo é R${saldo}')

    # Pegar saldo
    def get_saldo(self):
          return self._saldo

    # Fazer Aplicação      
    def fazerAplicacao(self, quantidade):
        self._saldo += quantidade
    
# Classe filho
class contaSalario():
    def __init__(self):
        super().__init__()
        self._saque = 5

# Classe filho
class contaCorrente(conta):
    limite = 100
    def retirarDinheiro(self, valor):
        saldo -= valor
        print('Carregando...')
        tempo()  
        print(f'Você retirou R${valor} da sua conta com sucesso!')
        print(f'Seu novo saldo é de R${saldo}')
# Inicio Sistema
while True:
        print('='*15,'|BANCO FERNANDO|','='*15)
        print('Bem-vindo ao sistema do banco Fernando')
        print('='*48)
        escolha = int(input('Qual função você gostaria de fazer?\n1 - Abrir conta\n2 - Consultar saldo\n3 - Fazer depósito\n4 - Pagar conta\n5 - Retirar Dinheiro\n0 - Sair do sistema\n'))
        # Abrir conta 
        if escolha == 1:
            try:
                TipoConta = int(input('Qual o tipo de conta que você quer abrir?\n1 - Conta poupança\n2 - Conta Salário\n3 - Conta Corrente\n'))
                if TipoConta == 1:
                        tipo = 'Poupança'
                elif TipoConta == 2:
                        tipo = 'Salário'
                elif TipoConta == 3:
                        tipo = 'Corrente'
            except TipoConta < 1 or TipoConta > 3:
                        print('Digite um número válido!')
                        raise ValueError
            except ValueError:
                        print('Digite um número válido!')
            nome = str(input('Digite seu nome: '))
            conta.AberturaContas()
        
        # Consulta de Saldo    
        if escolha == 2:
            Conta = conta()
            Conta.consultaSaldo()

        # Adicionar valor na conta    
        if escolha == 3:
            quantidade = int(input('Quantos reais você deseja depositar?\n'))
            Conta = conta()
            Conta.fazerAplicacao(quantidade)
        if escolha == 4:
            print("aaaa")
        if escolha == 5:
            valor = int(input('Quanto você deseja retirar?\nR$'))
            Conta = contaCorrente()
            Conta.retirarDinheiro(valor)
        if escolha == 0:
            break