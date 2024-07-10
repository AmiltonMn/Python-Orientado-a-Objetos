"""
Um dos problemas desse código seria o fato de ser em programação estruturada, sendo que ele pode ser feito utilizando POO.

nome_aluno = input('Digite o nome do aluno: ')
idade_aluno = input('Digite a idade do aluno: ')
turma_aluno = input('Digite a turma do aluno: ')
planta_aluno = input('Digite a planta do aluno: ')
aluno = {'Nome': nome_aluno, 'Idade': idade_aluno, 'Turma':turma_aluno, 'Planta': planta_aluno} # A criação desse dicionário não seria necessária.


aluno_str = str(aluno)
with open ('alunos.txt', 'w', encoding='utf8') as arquivo: # Outro erro seria em relação a forma que foi aberto o arquivo.txt pois na funça 'w' ele ira apagar tudo que tinha antes no arquivo, deixando a possibilidade de 'cadastrar' apenas um aluno no arquivo.
    arquivo.write(aluno_str)
"""

class aluno():
    def __init__(self, nomeAluno, idadeAluno, turmaAluno, plantaAluno):
        pass

    def cadastrarAluno(nomeAluno, idadeAluno, turmaAluno, plantaAluno):
        arquivo = open('alunos.txt', encoding='utf8', mode='a+')
        arquivo.write(f'O nome do aluno é {nomeAluno}. A idade do aluno é {idadeAluno}. A turma do aluno é {turmaAluno}. A planta do aluno é a de {plantaAluno}.\n')
        arquivo.close()
nomeAluno = input('Digite o nome do aluno: ')
idadeAluno = input('Digite a idade do aluno: ')
turmaAluno = input('Digite a turma do aluno: ')
plantaAluno = input('Digite a planta do aluno: ')
aluno.cadastrarAluno(nomeAluno, idadeAluno, turmaAluno, plantaAluno)