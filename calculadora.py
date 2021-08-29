def somar(num1,num2):
	soma = num1 + num2
	print(soma)

def diminuir(num1,num2):
	diminui = num1 - num2
	print(diminui)

def dividir(num1,num2):
	dividi = num1 / num2
	print(dividi)

def multiplicar(num1,num2):
	multiplica = num1 * num2
	print(multiplica)


escolha = int(input('Digite o número da operação: \n1-Soma \n2-Multiplicação \n3-Divisão \n4-Subtração \n'))



numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

if escolha == 1:
	somar(numero1,numero2)
elif escolha == 3:
	dividir(numero1,numero2)
elif escolha == 2:
	multiplicar(numero1,numero2)
else:
	diminuir(numero1,numero2)