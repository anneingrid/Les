class Les:
  def __init__(self,tamanho):
    self.tamanho_maximo = tamanho
    self.vetor = [None] * tamanho
    self.quant = 0

  def inserir_fim(self,valor):
    self.vetor[self.quant] = valor
    self.quant += 1

  def show(self):
    for i in range(self.quant):
      print(self.vetor[i])
    print()

  def remover_fim(self):
    self.quant -= 1 

  def inserir_inicio(self,valor):
    for i in range(self.quant,0,-1):
      self.vetor[i]=self.vetor[i-1]
    self.vetor[0]=valor
    self.quant+=1

  def remover_inicio():
    for i in range(self.quant):
      self.vetor[i]=self.vetor[i+1]
    self.quant-=1
    
  def ver_primeiro(self):
    return self.vetor[0]
  
  def ver_ultimo(self):
    return self.vetor[self.quant - 1]

  def tamanho_atual(self):
    return self.quant
  
  def capacidade(self):
    return self.tam_maximo

  def esta_cheia(self):
    if self.quant==self.tamanho_maximo:
      return True
    return False
    
  def esta_vazia(self):
    if self.quant==0:
      return True
    return False

  def remover_elemento(self, valor):
    for i in range(self.quant):
      if self.vetor[i]==valor:
        aux=i
        self.quant-=1
        for i in range (aux,self.quant):
          self.vetor[i]=self.vetor[i+1]

  def buscar(self,valor):
    for i in range(self.quant):
      if self.vetor[i]==valor:
        return f'{valor} - Posição: {i}'
      else:
        return None

  def inserir_apos(self,valor1,valor2):
    for i in range(self.quant):
      if self.vetor[i]==valor2:
        aux=i+1
        for i in range(self.quant,aux,-1):
          self.vetor[i]=self.vetor[i-1]
        self.vetor[aux]=valor1
        self.quant+=1 
        
  def inserir_antes(self, valor1, valor2):
    for i in range(self.quant):
      if self.vetor[i]==valor2:
        aux=i
        for i in range(self.quant,aux,-1):
          self.vetor[i]=self.vetor[i-1]
        self.vetor[aux]=valor1
        self.quant+=1
        break  