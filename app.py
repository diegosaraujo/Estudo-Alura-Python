# -*- coding: UTF-8 -*-
def listar(nomes):
	print ('Listando nomes: ')
	for nome in nomes:
		print (nome)

def cadastrar(nomes):
	print ('Digite o seu nome')
	nome = input()
	nomes.append(nome)

def remover(nomes):
	print ('Digite o nome que deseja remover')
	nome = input()
	nomes.remove(nome)

def alterar(nomes):
    print ('Qual nome vc gostaria de alterar?')
    nome_a_remover = input()
    if(nome_a_remover in nomes):
        posicao = nomes.index(nome_a_remover)
        print ('Digite novo nome:')
        nome_novo = input()
        nomes[posicao] = nome_novo

def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print ('1 Cadastrar / 2 Listar / 3 Remover / 4 Alterar / 0 Terminar')
		escolha = input()

		if (escolha =='1'):
			cadastrar(nomes)

		if (escolha == '2'):
			listar(nomes)

		if (escolha == '3'):
			remover(nomes)

		if (escolha == '4'):
			alterar(nomes)

menu()