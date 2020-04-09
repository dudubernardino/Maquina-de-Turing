# Equipe: Eduardo de Moura Bernardino - 1469757
#         Raimundo Angeliano
#         Vinícius Linhares Alves de Oliveira - 1469823

import os
import numpy
import time
import multiprocessing

def esta_comentada(linha):
  if linha[0] == '#':
    return True
  return False

class MaquinaTuring:
  def __init__(self, arquivo_fita, velocidade = 0.1):
    self.arquivo_fita = arquivo_fita
    self.velocidade = velocidade

  def extra_delta(self, linhas, variaveis):
    linhas = list(filter(None, linhas))
    if 'delta' not in linhas[0]:
      print('Delta Inválido')
      return 0
    linhas = linhas[1:]
    delta = {}
    for linha in linhas:
      chave = linha.split(':')[0]
      valores = dict(zip(
        variaveis,linha.split(":")[1].split()
      ))
      delta[chave] = valores
    return delta

  def get_config(self, nome_arquivo):
    with open(nome_arquivo, 'r') as handle:
      config = handle.readlines()
    delta = []
    for linha in config:
      if "estados" in linha:
        linha = linha.rstrip()
        self.estados = list(filter(
          None, linha.split(':')[1].split(',')
        ))
      elif "variaveis" in linha:
        linha = linha.rstrip()
        self.variaveis = list(filter(
          None, linha.split(':')[1].split(',')
        ))
      elif "simbolo_final" in linha:
        linha = linha.rstrip()
        self.simbolo_final = list(filter(
          None, linha.split(':')[1].split(',')
        ))[0]
      elif "estado_final" in linha:
        linha = linha.rstrip()
        self.estado_final = list(filter(
          None, linha.split(':')[1].split(',')
        ))[0]
      elif "estado_inicial" in linha:
        linha = linha.rstrip()
        self.estado_inicial = list(filter(
          None, linha.split(':')[1].split(',')
        ))[0]
      elif not esta_comentada(linha):
        delta.append(linha)
    self.variaveis.append(self.simbolo_final)
    self.delta = self.extra_delta(delta, self.variaveis)
    print(self.delta)

mt = MaquinaTuring("fita.txt", velocidade = 0.1)

mt.get_config("config.txt")