import random

class Forca:

	def __init__(self,palavra):
		self.palavra = palavra
		self.erro = []
		self.acerto = []

	def adivinha(self,letra):
		if letra in self.palavra and letra not in self.acerto:
			self.acerto.append(letra)
		elif letra not in self.palavra and letra not in self.erro:
			self.erro.append(letra)
		else:
			False
		return True

	def esconde(self):
		traco = ''
		for letra in self.palavra:
			if letra not in self.acerto:
				traco += '-'
			else:
				traco += letra
		return traco

	def vencer(self):
		if '-' not in self.esconde():
			return True
		return False

	def perder(self):
		if len(self.erro) == 6:
			return True
		return False

	def termino(self):
		return self.vencer() or self.perder()


def palavrinha():
	with open('palavras.txt') as f:
		word = f.readlines()
	return word[random.randint(0,len(word))].strip()


jogo = Forca(palavrinha())

while not jogo.termino():

	print('Qual a Palavra:')
	print(jogo.esconde())
	tentativa = input('Digite uma letra: ')
	jogo.adivinha(tentativa)

	

	if jogo.vencer():
		print('Parabéns!! Você adivinhou a palavra')
		print(jogo.palavra)
	elif jogo.perder():
		print('Game Over! Você não adivinhou a palavra')
		print(jogo.palavra)
	

