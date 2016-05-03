# -*- coding: UTF-8 -*-

class Perfil():
	'Classe padrão para perfis de usuários'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa

	def imprimir_dados_perfil(self):
		print (('Nome: %s, Telefone: %s, Empresa: %s')%(self.nome, self.telefone, self.empresa))

class Data(object):
   'Classe para formatar datas'

   def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano

   def imprimir(self):
      print (('%s/%s/%s') % (self.dia, self.mes, self.ano))


