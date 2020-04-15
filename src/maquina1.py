from turing import *
from ler_arquivo import *
import json 

arquivo = ler_arquivo('src/config.txt')
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
    
print(trans_q0)
print(trans_q1)
print(trans_q2)


alfabeto = arquivo.alfabeto
alfabeto_aux = arquivo.alfabeto_aux
estados = arquivo.estados
estado_inicial = arquivo.estado_inicial[0]
simbolo_inicial = arquivo.simbolo_inicial[0]


trans_q0 = [["#","#",DIR,"q0"],['a','A',DIR,"q1"],['B','B',DIR,"q3"],[' ',' ',DIR,"q4"]]
trans_q1 = [['b','B',ESQ,"q2"],['a','a',DIR,"q1"],['B','B',DIR,"q1"]]
trans_q2 = [['A','A',DIR,"q0"],['a','a',ESQ,"q2"],['B','B',ESQ,"q2"]]
trans_q3 = [['B','B',DIR,"q3"],[' ',' ',DIR,"q4"]]
trans_q4 = []

q0 = estado("q0",trans_q0)
q1 = estado("q1",trans_q1)
q2 = estado("q2",trans_q2)
q3 = estado("q3",trans_q3)
q4 = estado("q4",trans_q4,is_final=True)

# turing = turing(alfabeto,[q0,q1,q2,q3,q4],'q0',alfabeto_aux,simbolo_inicial,' ')
# turing.aceita("ab")
# turing.aceita("aabb")
# turing.aceita("aaab")
# turing.aceita("aaaabbbb")