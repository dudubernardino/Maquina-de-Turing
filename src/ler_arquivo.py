class ler_arquivo():
  def __init__(self, nome_arquivo):
    self.nome_arquivo = nome_arquivo

  def get_linhas(self):
    f = open(self.nome_arquivo, 'r')
    self.config = []
    self.transicoes = []
    self.count = 0
    for linha in f:
      if "alfabeto" in linha:
        linha = linha.rstrip()
        self.alfabeto = list(filter(
          None, linha.split(':')[1].split(',')
        ))
       
      elif "alfabet0_aux" in linha:
        linha = linha.rstrip()
        self.alfabeto_aux = list(filter(
          None, linha.split(':')[1].split(',')
        ))
        
      elif "trans_q" in linha:
        linha = linha.rstrip()
        self.transicoes.append(list(filter(
            None, linha.split(':')[1].split('[]')
          )))
            


#globals()["trans_q" + str(i)] = arquivo.transicoes[i]