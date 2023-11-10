from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Deletar cadastros', 'Sair do Sistema'])
    if resposta == 1:
        #opção de lsitar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRADO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        nome = str(input('Nome: '))
        deletar_cadastro(arq, nome)
    elif resposta == 4:
        cabeçalho('Saindo do sistema ..Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
    
'''
Adicionei a opção de deletar cadastro
'''