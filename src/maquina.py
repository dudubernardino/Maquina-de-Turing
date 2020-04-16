from turing import *
from ler_arquivo import * 

arquivo = ler_arquivo('src/config.txt')
arquivo.get_linhas()

DIR = True
ESQ = False

alfabeto = arquivo.alfabeto
alfabeto_aux = arquivo.alfabeto_aux
estados = []
estado_inicial = arquivo.estado_inicial[0]
simbolo_inicial = arquivo.simbolo_inicial[0]

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

# trans_q0 = [["#","#",DIR,"q0"],['a','A',DIR,"q1"],['B','B',DIR,"q3"],[' ',' ',DIR,"q4"]]
# trans_q1 = [['b','B',ESQ,"q2"],['a','a',DIR,"q1"],['B','B',DIR,"q1"]]
# trans_q2 = [['A','A',DIR,"q0"],['a','a',ESQ,"q2"],['B','B',ESQ,"q2"]]
# trans_q3 = [['B','B',DIR,"q3"],[' ',' ',DIR,"q4"]]
# trans_q4 = []

# Atribui as transições aos respectivos estados
for i in range(len(arquivo.estados)):
  globals()["q" + str(i)] = estado(f'q{i}',globals()["trans_q" + str(i)])
  if i == (len(arquivo.estados) - 1):
    globals()["q" + str(i)] = estado(f'q{i}',globals()["trans_q" + str(i)],is_final=True)
  estados.append(globals()["q" + str(i)])

# q0 = estado("q0",trans_q0)
# q1 = estado("q1",trans_q1)
# q2 = estado("q2",trans_q2)
# q3 = estado("q3",trans_q3)
# q4 = estado("q4",trans_q4,is_final=True)

# Máquina da config.txt
turing = turing(alfabeto,estados,estado_inicial,alfabeto_aux,simbolo_inicial,' ')
turing.run("ab")
turing.run("aabb")
turing.run("aaab")
turing.run("aaaabbbb")

# Máquina da config2.txt
# turing = turing(alfabeto,estados,estado_inicial,alfabeto_aux,simbolo_inicial,' ')
# turing.run("")
# turing.run("aabbcc")
# turing.run("aaabbbccc")
# turing.run("abbc")