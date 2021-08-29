import random

class adivinha:
	def __init__(self,nome):
		self.nome = nome
		


	def guessing(self):
		numero = random.randrange(0,101)
		contador = 0
		lista = [numero-5,numero-4,numero-3,numero-2,numero-1]
		lista2 = [numero+1,numero+2,numero+3,numero+4,numero+5]
		while contador < 10:
			guess = input('Digite seu palpite: ')
			if int(guess) in lista:
				print('Seu palpite foi baixo, mas está proximo {}'.format(self.nome))
			elif int(guess) < numero:
				print('Seu palpite foi baixo {}'.format(self.nome))	
			elif int(guess) in lista2:
				print('Seu palpite foi alto, mas está proximo {}'.format(self.nome))			
			elif int(guess) > numero:
				print('Seu palpite foi alto {}'.format(self.nome))			
			elif int(guess) == numero:
				print('Parabéns {} você acertou!'.format(self.nome))
				break
			contador += 1
			print('você ainda tem ' + str(10-contador) + ' jogadas.')	




nome = input('Digite seu nome: ')


inicio = adivinha(nome)

inicio.guessing()
