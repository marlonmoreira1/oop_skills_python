class Motor:
    
    def __init__(self):
        self.velocidade = 0
        
    def acelerar(self):
        self.velocidade += 1
        
        
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
                    
NORTE = 'norte'
SUL = 'sul'
LESTE = 'leste'
OESTE = 'oeste'

  
class Direcao:
    
    rotacao_direita = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_esquerda = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.posicao = NORTE

    def direita(self):
        self.posicao = self.rotacao_direita[self.posicao]

    def esquerda(self):
        self.posicao = self.rotacao_esquerda[self.posicao]
       

    
    
class Carro(Motor, Direcao):
    def __init__(self):
        Motor.__init__(self)
        Direcao.__init__(self)


ford = Motor()
ford.acelerar()
ford.acelerar()
print(ford.velocidade)
ford.acelerar()
print(ford.velocidade)
ford.frear()
print(ford.velocidade)
ford.frear()
print(ford.velocidade)
ford.frear()
print(ford.velocidade)

ford = Direcao()
ford.direita()
print(ford.posicao)
ford.esquerda()
print(ford.posicao)
ford.esquerda()
print(ford.posicao)
ford.esquerda()
print(ford.posicao)
ford.esquerda()
print(ford.posicao)
ford.direita()
print(ford.posicao)    