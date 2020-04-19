from turing import *
from ler_arquivo import * 

nome_do_arquivo = 'config'
print(f'carregando a máquina com configurações: {nome_do_arquivo}.txt')
arquivo = ler_arquivo(f'src/{nome_do_arquivo}.txt')
arquivo.get_linhas()

DIR = True
ESQ = False

# Organizando Transições
nova_transicao = []
for i in range(len(arquivo.transicoes)):
    for transicao in arquivo.transicoes[i]:
        globals()["trans_q" + str(i)] = []
        nova_transicao = transicao.replace('[', '').replace(']', '').split(';')
        for direcao in nova_transicao:
            transicao = direcao.split(',')
            for direcao in transicao:
                if "DIR" in direcao:
                    transicao[2] = DIR
                elif "ESQ" in direcao:
                    transicao[2] = ESQ
            globals()["trans_q" + str(i)].append(transicao)
        if globals()["trans_q" + str(i)] == [['']]:
            globals()["trans_q" + str(i)] = []

# Identifica o simbolo branco
for i in range(len(arquivo.transicoes)):
    for transicao in globals()["trans_q" + str(i)]:
        for j in range(len(transicao)):
            if transicao[j] == "' '":
                transicao[j] = ' '

# Atribui as transições aos respectivos estados
estados = []
for i in range(len(arquivo.estados)):
    globals()["q" + str(i)] = estado(f'q{i}',globals()["trans_q" + str(i)])
    if i == (len(arquivo.estados) - 1):
        globals()["q" + str(i)] = estado(f'q{i}',globals()["trans_q" + str(i)],is_final=True)
    estados.append(globals()["q" + str(i)])

turing = turing(arquivo.alfabeto, estados, arquivo.estado_inicial[0] ,arquivo.alfabeto_aux, arquivo.simbolo_inicial[0], ' ')

print('Máquina carregada.')
print(f'A máquina irá processar as cadeias: {arquivo.cadeias}')

# Lê as cadeias e executa a máquina, verificando se aceita ou não as cadeias inseridas
for i in range(len(arquivo.cadeias)):
    if arquivo.cadeias[i] == "''":
        arquivo.cadeias[i] = ""
    turing.processar(arquivo.cadeias[i])
