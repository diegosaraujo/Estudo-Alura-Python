# -*- coding: UTF-8 -*-

class Perfil(object):
   'Classe padrão para perfis de usuários'

   def __init__(self, nome, telefone, empresa):
      self.nome = nome
      self.telefone = telefone
      self.empresa = empresa
      self.__curtidas = 0

   def imprimir_dados_perfil(self):
      print (('Nome: %s, Telefone: %s, Empresa: %s')%(self.nome, self.telefone, self.empresa))

   def curtir(self):
      self.__curtidas+=1

   def numero_curtidas(self):
      print (('Você possui %s curtida(s)') % (self.__curtidas))

   def obter_curtidas(self):
      return self.__curtidas



class Perfil_Vip(Perfil):
   'Classe padrão para perfis de usuários VIPs'

   def __init__(self, nome, telefone, empresa, apelido):
      super(Perfil_Vip, self).__init__(nome, telefone, empresa)
      self.apelido = apelido

   def obter_creditos(self):
      return super(Perfil_Vip, self).obter_curtidas() * 10.0



class Data(object):
   'Classe para formatar datas - Desafio Exercicio'

   def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano

   def imprimir(self):
      print (('%s/%s/%s') % (self.dia, self.mes, self.ano))


class Pessoa(object):
   'Classe para Pessoa que calcula o IMC - Desafio Exercicio'

   def __init__(self, nome, peso, altura):
      self.nome = nome
      self.peso = float(peso)
      self.altura = float(altura)


   def imprime_imc(self):
      imc = self.peso / (self.altura **2)
      print (('IMC de %s: %s') % (self.nome, imc))