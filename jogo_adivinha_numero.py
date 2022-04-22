import random

class Adivinha:
	def __init__(self,nome):
		self.nome = nome

	def palpite(self):
		numero = random.randrange(0,101)
		contador = 0
		proximo_baixo = [numero-5,numero-4,numero-3,numero-2,numero-1]
		proximo_alto = [numero+5,numero+4,numero+3,numero+2,numero+1]
		while contador < 10:
			chute = int(input("Digite seu palpite:"))
			if chute in proximo_baixo:
				print("Seu palpite foi baixo, mas está próximo {}".format(self.nome))
			elif chute < numero:
				print("Seu palpite foi baixo {}".format(self.nome))
			elif chute in proximo_alto:
				print("Seu palpite foi alto, mas está próximo {}".format(self.nome))
			elif chute > numero:
				print("Seu palpite foi alto {}".format(self.nome))
			elif chute == numero:
				print("Parabéns {} você acertou!\nO numero era {}".format(self.nome,numero))
				break
			contador+=1
			print("Você ainda tem " + str(10-contador) + " jogadas.")
		if contador == 10:
			print("Você não tem mais jogadas!\nO número era {}".format(numero))



nome = input("Digite seu nome: ")

jogar = Adivinha(nome)
jogar.palpite()