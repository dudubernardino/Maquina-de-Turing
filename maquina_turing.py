# Equipe: 
#Eduardo de Moura Bernardino - 1469757
#Raimundo Angeliano Gonçalves de Sousa - 1476646
#Vinícius Linhares Alves de Oliveira - 1469823

import os
import numpy
import time

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
  
  def escrever_fita(self, estado_atual, string_fita, proximo_estado, parada = False):
    if parada and self.estadoFinal(proximo_estado):
      status = 'ACEITO'
    elif parada:
      status = 'REJEITADO'
    else:
      status = 'RODANDO'
    with open(self.arquivo_fita, 'w+') as handle:
      handle.write(str(estado_atual) + '\n'
                    + string_fita + '\n'
                    + status + '\n'
                    + str(proximo_estado) + '\n'
                    + str(self.velocidade))

  def estadoFinal(self, state):
    if state == self.estado_final:
      return True
    return False
  
  def get_acao(self, acao, input, index):
    if not acao:
      return False
    if 'R' in acao:
      proximo_index = index + 1
      if proximo_index > len(input)-1:
        input += self.simbolo_final
      proximo_estado = acao.split('R')[-1]
      input = input[:index] + acao.split('R')[0] + input[(index+1):]
    else:
      proximo_index = index - 1
      if proximo_index < 0:
        input = self.simbolo_final + input
      proximo_estado = acao.split('L')[-1]
      input = input[:index] + action.split('L')[0] + input[(index+1):]
    return proximo_index, input, proximo_estado
  
  def simular(self, input):
    if input[-1] != self.simbolo_final:
      input += self.simbolo_final
    proximo_estado = self.estado_inicial
    proximo_index = 0
    status = "Rodando"
    for index, simbolo in enumerate(input):
      self.escrever_fita(index, input, proximo_estado)
      simbolo = input[proximo_index]
      try:
        acao = self.delta[proximo_estado][simbolo]
      except:
        self.escrever_fita(index, input, proximo_estado, parada=True)
        return
      print(f"String: {input}")
      print(f"Ação: {acao}")
      proxima_acao = self.get_acao(acao, input, index)
      proximo_index, input, proximo_estado = proxima_acao
      time.sleep(self.velocidade)
    self.escrever_fita(index, input, proximo_estado, parada=True)


if __name__ == "__main__":
  mt = MaquinaTuring("fita.txt", velocidade = 0.1)

  mt.get_config("config.txt")

  mt.simular("aaa") # Deve Aceitar
  # mt.simular("aaabaabbaaacabbsss") # Deve Rejeitar