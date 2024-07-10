class Livro():
    pagina = 1
    guardado = True
    def __init__(self, titulo, autor, qtd_paginas, guardado=True):
        self.titulo = titulo
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.guardado = guardado
        self.pagina = 1
        self.guardado = True

    # Método de pegar o livro
    @staticmethod
    def pegarLivro():
        if Livro.guardado == True:
            Livro.guardado = False
            print('Você pegou o livro!')
        else:
            print('O livro não está guardado para ser retirado!')

    # Método de devolver o livro
    @staticmethod
    def devolverLivro():
       Livro.guardado = True
       print(Livro.guardado)
       print('Você guardou o livro!')

    # Método de virar uma página
    def virarUmaPagina(self, guardado):
        if guardado == False:
            print(f'Você está na página {self.pagina}')
            return self.pagina + 1
        else:
            print('O livro está guardado!')

    def getPagina(self):
        return self.pagina
            
    # Método para virar quantas páginas quiser       
    def virarNPaginas(self, guardado, paginas, qtd_paginas):
        if guardado == False:
            self.pagina += paginas
            print(self.pagina)
            print(f'Você está na página {self.pagina}!')
            if paginas > qtd_paginas:
                print(f'O livro tem apenas {qtd_paginas} páginas!')
        else:
            print('O livro está guardado')

    # Método de voltar 1 página
    def voltarUmaPagina(self, guardado, qtd_paginas):
        if guardado == False:
            self.pagina -= 1
            if self.pagina == 0:
                print(f'Você está na página {self.pagina}!')
                print('Você fechou o livro!')
                return self.pagina
        else:
            print('O livro está guardado!')

    # Método de voltar quantidade específica de páginas
    def voltarNPaginas(self, guardado, paginaAtual, paginas, qtd_paginas):
        if guardado == False:
            paginaAtual -= paginas
            print(self.pagina)
            if paginaAtual == 0:
                print(f'Você está na página {paginaAtual}')
                print('Você fechou o livro!')
            else:
                print(f'Você está na página {paginaAtual}!')
        else:
            print('O livro está guardado')
    
    # Método para ver o nome e o autor do livro
    @staticmethod
    def lerLivro(título, autor):
        print(f'O livro é {título} e o autor é {autor}')

while True:
    Livro.lerLivro('Moby Dick', 'Algum')
    livro1 = Livro('Moby Dick', 'Algum', 1, 320)
    livro1.pegarLivro()
    livro1.virarUmaPagina(Livro.guardado)
    # livro1.virarNPaginas(Livro.guardado, 333, qtd_paginas=320)
    # livro1.voltarUmaPagina(Livro.guardado, 320)
    # livro1.voltarNPaginas(Livro.guardado, 120, 100, 320)
    sair = int(input('Quer continuar lendo? Se sim digite \'1\' se não digite \'0\''))
    if sair == 0:
        break