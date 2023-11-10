from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler a arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados no arquivo!')
        else:
            print(f'Novo registro de {nome} adcionado.')
            a.close()


def deletar_cadastro(arq, nome):
    try:
        with open(arq, 'r') as file:
            linhas = file.readlines()
        with open(arq, 'w') as file:
            for linha in linhas:
                if not linha.startswith(nome + ';'):
                    file.write(linha)
        print(f'Registro de {nome} deletado, se existir.')
    except Exception as e:
        print(f'Houve um erro ao deletar o registro de {nome}: {e}')