class Empresa:
    PaisesAtuacao = []
    Produtos = {}
    listaProduto = []
    def __init__(self, nome, cnpj, nacionalidade, Presidente, PaisesAtuacao, produtos={}):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__nacionalidade = nacionalidade
        self.__Presidente = Presidente
        self.__paisesAtuacao = PaisesAtuacao
        self.__produtos = {}
    
    # Método de retornar o responsável
    def getPresidente(self):
        return self.__Presidente
    
    # Método de Retornar países de atuação
    def getPaisesAtuacao(self):
        return self.__paisesAtuacao
    
    # Método de pesquisar país
    def pesquisarPaisAtuacao(self, pesquisa, paisesAtuacao):
        for i in range(len(paisesAtuacao)):
            if pesquisa == paisesAtuacao[i]:
                print(f'O país {pesquisa} está na lista de atuações da empresa {self.__nome}!')
    
    # Método de adicionar função
    def adicionarProduto(self, nomeProduto, preçoProduto, descProduto):
        listaProduto = [preçoProduto, descProduto]
        self.__produtos = {nomeProduto:listaProduto}
        print(self.__produtos)
        return self.__produtos and listaProduto

    # Método de relatório do produto
    def relatorioProduto(self, produtos, nomeProduto, listaProduto):
        for i in range(len(self.__produtos)):
            produto = str(self.__produtos)
            print(produto)

    # Método de pesquisa do produto
    def pesquisarProduto(self, nomeProduto):
        print(self.__produtos[nomeProduto])

# Classe área
class Area(Empresa):
    _DataInicio = '20/10/2023'
    _DataFim = '20/10/2024'
    _SiglaSetor1 = 'PT'
    _SiglaSetor2 = 'AA'
    _funcaoSetor1 = 'fazer ferramentas'
    _funcaoSetor2 = 'venda de peças'

    def __init__(self, nome, siglaSetor, Função, Diretor, Lucro, DataInicio, DataFim):
        self.__nome = nome
        self.__funcao = Função
        self.__Diretor = 'Alguém'
        self.__Lucro = Lucro

    # Método de get para o nome do diretor
    def getDiretor(self):
        return self.__Diretor

    # Método de relatório financeiro
    def relatorioFinanceiro(self, siglaSetor, funcao, lucro):
        print(f'O setor {siglaSetor} cuja função é {funcao} obteve um lucro de {lucro}')

    # Método de Período da Auditoria
    @staticmethod
    def periodoAuditoria(DataInicio, DataFim, Diretor):
        print(f'A auditoria teve inicio no dia {DataInicio} e irá encerrar no dia {DataFim}. Sendo {Diretor} o responsável pela área!')

# Classe Departamento
class Departamento(Area):
    def __init__(self, nome, siglaSetor, funcao, gestor, quantidadeFuncionarios):
        self._gestor = gestor

    def getGestor(self):
        return self._gestor


# Resultados Classe 'Empresa"
paisesAtuacao=['Brasil', 'Argentina', 'Alemanha', 'Estados Unidos']
bosch = Empresa('Bosch', '000.000.000/000001', 'Alemanha', 'Presidente', paisesAtuacao, produtos={})
bosch.adicionarProduto('Furadeira', 'R$90,00', 'Uma furadeira inteligente')
bosch.pesquisarPaisAtuacao('Brasil', paisesAtuacao)
print(bosch.getPaisesAtuacao())
bosch.relatorioProduto(Empresa.Produtos, 'Furadeira',Empresa.listaProduto)
bosch.pesquisarProduto('Furadeira')
        
# Resultados Classe 'Área'
area = Area('AA', 'AA', 'Faz Ferramentas', 'Alguém', 'R$50.000,00', Area._DataInicio, Area._DataFim)
print(area.getDiretor())
area.relatorioFinanceiro(Area._SiglaSetor1, Area._funcaoSetor1, 'R$50.000,00')
area.periodoAuditoria(Area._DataInicio, Area._DataFim, area.getDiretor())

# Resultados classe 'Departamento'
dep = Departamento('Engineering Technical Schoool', 'ETS', 'Treinamento Aprendizes', 'Alguém', 180)
print(dep.getGestor())