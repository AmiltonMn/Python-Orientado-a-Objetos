
"""
class -> Estrutura que abstrai característica de um objeto
instância -> cria um objetio a partir de classe
métodos -> Funções dentro da classe
atributo -> Características de um objeto
self -> Referência ao mesmo objeto
construtor -> Cria a classe e o objeto "__init__"
destrutor -> Função criada para destruir a classe "__del__"
pass -> Ignorar
@Staticmethod -> Função estática (suas variáveis devem ser globais, ou seja, devem ser atribuídas fora dos métodos)

ctrl + : -> comentar
ctrl + alt + seta para cima ou baixo -> Seleciona mais de uma linha
alt + seta -> Mover linha inteira para cima ou para baixo
F2 -> Mudar nomes iguais ao mesmo tempo
__ -> Deixa uma variável como privada dentro da classe
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4 Pilares da Orientação a Objetos

Abstração: abstrar características e comportamentos de determinado objeto físico ou abstrato
Encapsulamento: Restringir o acesso de outras classes a determinada informação. Deixando os atributos Públicos ou Privados
Herança: A herança ocorre quando uma classe criada herda funcionalidades de uma classe base.
Polimorfismo: Consiste em modificar um método herdado da nova classe. Ex: Abrir janela no carro é a partir do botão, abrir uma janela é manualmente.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class casa():
    def ligar_luzes(self):
        print('Luzes ligadas')
    def desligar_luzes(self):
        print('Luzes desligadas')
    def trancar_portas(self):
        print('Portas trancadas')
    def destrancar_portas(self):
        print('Portas destrancadas')

casa_joao = casa()
casa_maria = casa()
casa_verde = casa()

casa_joao.destrancar_portas()
casa_joao.ligar_luzes()
casa_joao.trancar_portas()


class casa():
    def __init__(self, area, rua, cor):
        self.area = area
        self.cor = cor
        self.rua = rua

casa_joao = casa(120, 'Azul', 'Juscelino Kubistchek')
print(f'Area: {casa_joao.area}. Cor: {casa_joao.cor}. Rua: {casa_joao.rua}')


class casa():
    def __init__(self, area, rua, cor):
        self.area = area
        self.cor = cor
        self.rua = rua
        self.luzes_ligadas = False
        self.luzes = False
        self.energia = False
    def __del__(self):
        pass
    def ligar_luzes(self):
        if self.energia == True:
            self.luzes = True
    def desligar_luzes(self):
        self.luzes = False

    @staticmethod
    def cortar_energia():
        casa.energia = False
    
    @staticmethod
    def ligar_energia():

        casa.energia = True

casa_joao = casa(120, 'Azul', 'Juscelino Kubistchek')
casa_maria = casa(120, 'Rosa', 'Juscelino Kubistchek')
print(casa_joao.energia)
print(casa_joao.energia)

print('Ligando a anergia!')

casa.ligar_energia()

print('A energia foi ligada!')

print(f'A casa do João tem energia? {casa_joao.energia}')
print(f'A casa da Maria tem energia? {casa_maria.energia}')


class casa():
    def __init__(self, area, rua, cor, morador=''):
        self.area = area
        self.cor = cor
        self.rua = rua
        self.morador = morador
        self.luzes_ligadas = False
        self.luzes = False
        self.energia = False
    def __del__(self):
        pass
    def ligar_luzes(self):
        if self.energia == True:
            self.luzes = True
    def desligar_luzes(self):
        self.luzes = False

    @staticmethod
    def cortar_energia():
        casa.energia = False
    
    @staticmethod
    def ligar_energia():
        casa.energia = True

casa_joao = casa(120, 'Azul', 'Juscelino Kubistchek', 'João')
casa_maria = casa(120, 'Rosa', 'Juscelino Kubistchek')
print(casa_joao.morador)
print(casa_maria.morador)
print(casa_joao.energia)
print(casa_maria.energia)
print('Ligando a anergia!')

casa.ligar_energia()

print('A energia foi ligada!')

print(f'A casa do João tem energia? {casa_joao.energia}')
print(f'A casa da Maria tem energia? {casa_maria.energia}')

class casa():
    energia = False
    def __init__(self, area, rua, cor, morador=''): # Para especificar a classe de algo, é só colocar o':'. Ex: cor: str = 'Azul'
        self.area = area
        self.cor = cor
        self.rua = rua
        self.morador = morador
        self.luzes_ligadas = False
        self.luzes = False
    def __del__(self):
        pass
    def ligar_luzes(self):
        if self.energia == True:
            self.luzes = True
    def desligar_luzes(self):
        self.luzes = False

    @staticmethod
    def cortar_energia():
        casa.energia = False
        return casa.energia
    
    @staticmethod
    def ligar_energia():
        casa.energia = True

        
morador = None
casa_pedro = casa(120, 'Azul', 'Juscelino Kubistchek', 'João')
casa_maria = casa(120, 'Rosa', 'Juscelino Kubistchek')
print(casa_pedro.morador)
print(casa_maria.morador)
print(casa_pedro.energia)
print(casa_maria.energia)
print('Ligando a anergia!')

casa.ligar_energia()

print('A energia foi ligada!')

print(f'A casa do João tem energia? {casa_pedro.energia}')
print(f'A casa da Maria tem energia? {casa_maria.energia}')

Ternario = casa(120, 'verde', 'Auto da XV', 'sem morador' if morador == None else morador)
print(Ternario.morador)
# Exemplo de algo sendo privado em uma classe
class casa():
    def __init__(self):
        self.public = "public"
        self.__pi = 3.14159265
    def get_pi(self):
        return self.__pi
    def piv2(self):
        return self.__pi * 2
casinha = casa()
casinha.public = 'Uma string'
print(casinha.public)
print(casinha.piv2())


# Classe pai
class instrumento_escrita:
    def __init__(self, material): 
        self.material = material
    def escrever(self):
        print('✍ Escrevendo...')
    def desenhar(self):
        print('Desenhando em sentidos aleatórios')

# Classes filho 
class lapis(instrumento_escrita): # A classe esta referenciada com o nome da classe "pai".
    def __init__(self):
        super().__init__('grafite') # Pega a primeira classe e faz o início dela. O super referência o objeto "pai". Pega a função de inicialização da primeira classe

class caneta(instrumento_escrita): # A classe esta referenciada com o nome da classe "pai".
    def __init__(self):
        super().__init__('tinta') # Pega a primeira classe e faz o início dela. O super referência o objeto "pai". Pega a função de inicialização da primeira classe. Tem como utilizar também como referência do super as funções dentro da função principal.

class canetinha(instrumento_escrita):
    def __init__(self):
        super().__init__('tinta')

    def desenhar(self):
        print('Desenhando em sentidos horizontais')

c = canetinha
l = lapis
print('Instrumento de escrita')
print(c.desenhar())
print(lapis.desenhar())
"""

# Personagem base
class Personagem:
    _Vida = 0
    _Força = 0
    _Inteligência = 0
    _DinheiroPorMinuto = 0
    def __init__(self):
        self._Vida = 100
        self._Força = 10
        self._Inteligência = 10
        self._DinheiroPorMinuto = 10
        pass
    def GetVida(self):
        return self._Vida
    def Atack(self):
        return self._força
    def Minerar(self):
        return self._Força

# Goblin
class Goblin(Personagem):

    def __init__(self):
        super().__init__()
        self._Força = 15
        self._Inteligência = 8
        self._DinheiroPorMinuto = 11
    def Minerar(self):
        return self._Força

random = Personagem()
print(f'Vida de um personagem aleatório: {random.GetVida()}')
print(f'Força de mineração: {random.Minerar()}')
g = Goblin()
print('Especificações da classe Globin')
print(f'Vida do Goblin: {g.GetVida()}')
print(f'Força de mineração: {g.Minerar()}')
print(random.Minerar())
