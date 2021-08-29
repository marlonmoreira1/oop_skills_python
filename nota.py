class verificarnota:

	def __init__(self,materia,nota1,nota2,nota3):
		self.materia = materia
		self.nota1 = nota1
		self.nota2 = nota2
		self.nota3 = nota3

	def calcularnota(self):
		media = 28
		soma = nota1 + nota2 + nota3
		if media > soma:
			precisa = media - soma
			return 'Você precisa de %d em %s' % (precisa,materia)
		else:
			return 'Você já está aprovado!'

	
materia = input('Digite a materia: ')
nota1 = int(input('Digite a nota1: '))
nota2 = int(input('Digite a nota2: '))
nota3 = int(input('Digite a nota3: '))


verifica = verificarnota(materia,nota1,nota2,nota3)
print(verifica.calcularnota())

