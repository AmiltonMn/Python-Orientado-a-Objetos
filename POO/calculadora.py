import math
num1 = int(input('Digite o primeiro número: \n'))
num2 = int(input('Digite o segundo número: \n'))
class Calculadora:
    def __init__(self):
        pass
    def soma(self):
        return num1 + num2
    def subtração(self):
        return num1 - num2
    def multiplicação(self):
        return num1 * num2
    def divisão(self):
        return num1 / num2
    def MostrarTudo(self):
        print(f'A soma dos números foi de {resultado.soma()}\n')
        print(f'A subtração dos números foi de {resultado.subtração()}\n')
        print(f'A multiplicação dos números foi de {resultado.multiplicação()}\n')
        print(f'A divisão dos números foi de {resultado.divisão():.2f}\n')
class CalculadoraCientífica(Calculadora):
    def __init__(self):
        pass
    def Fatorial1(self):
        return math.factorial(num1) 
    def Fatorial2(self):
        return math.factorial(num2)
    def Raiz1(self):
        return math.sqrt(num1)
    def Raiz2(self):
        return math.sqrt(num2)
    def Quadrado1(self):
        return num1**2
    def Quadrado2(self):
        return num2**2
    def MostrarTudo(self):
        super().MostrarTudo()
        print(f'O fatorial do 1° número é: {CalculadoraCientífica.Fatorial1(self)}\n')
        print(f'O fatorial do 2° número é: {CalculadoraCientífica.Fatorial2(self)}\n')
        print(f'A Raiz do 1° número é: {CalculadoraCientífica.Raiz1(self):.2f}\n')
        print(f'A Raiz do 2° número é: {CalculadoraCientífica.Raiz2(self):.2f}\n')
        print(f'O 1° número ao quadrado é: {CalculadoraCientífica.Quadrado1(self)}\n')
        print(f'O 2° número ao quadrado é: {CalculadoraCientífica.Quadrado2(self)}\n')
resultado = CalculadoraCientífica()
print('-'*15,'Calculadora','-'*15,'\n')
resultado.MostrarTudo()


