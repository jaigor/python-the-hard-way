#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint   # used to get a random number

class Actor:
	"""Abstract Class for actors (players and enemies)"""
	life = 100
	isDead = False
	attacks = []
	weakness = []

	def set_life(self, life):
		Actor.life = life

	def set_isDead(self, isDead):
		Actor.isDead = isDead

	def set_attacks(self, attacks):
		Actor.attacks = attacks

	def set_weakness(self, weakness):
		Actor.weakness = weakness

	def get_life(self):
		return self.life

	def get_isDead(self):
		return self.isDead

	def get_attacks(self):
		return self.attacks

	def get_weakness(self):
		return self.weakness


class Player(Actor):
	def __init__(self, idClass):
		if idClass == "1":
			self.set_attacks(Ultra().get_attacks())
			self.set_weakness(Ultra().get_weakness())
			self.name = Ultra().get_name()
		elif idClass == "2":
			self.set_attacks(Conservador().get_attacks())
			self.set_weakness(Conservador().get_weakness())
			self.name = Conservador().get_name()
		elif idClass == "3":
			self.set_attacks(Radical().get_attacks())
			self.set_weakness(Radical().get_weakness())
			self.name = Radical().get_name()
		elif idClass == "4":
			self.set_attacks(Socialista().get_attacks())
			self.set_weakness(Socialista().get_weakness())
			self.name = Socialista().get_name()

	def get_idClass(self):
		return self.idClass

	def get_name(self):
		return self.name


class Enemy(Actor):
	def __init__(self, idClass):
		if idClass == "1" or idClass == "2":
			rival = Derecha().get_rival
			# random number to decide rival
			num = randint(3,4)
			if num == 3:
				self.set_attacks(Radical().get_attacks())
				self.set_weakness(Radical().get_weakness())
				self.name = Radical().get_name()
			elif num == 4:
				self.set_attacks(Socialista().get_attacks())
				self.set_weakness(Socialista().get_weakness())
				self.name = Socialista().get_name()
		elif idClass == "3" or idClass == "4":
			rival = Izquierda().get_rival
			# random number to decide rival
			num = randint(1,2)
			if num == 1:
				self.set_attacks(Ultra().get_attacks())
				self.set_weakness(Ultra().get_weakness())
				self.name = Ultra().get_name()
			elif num == 2:
				self.set_attacks(Conservador().get_attacks())
				self.set_weakness(Conservador().get_weakness())
				self.name = Conservador().get_name()

	def get_name(self):
		return self.name


##### Political Classes #####

class Derecha:
	rival = "Izquierda"

	def get_rival(self):
		return self.rival

class Izquierda:
	rival = "Derecha"

	def get_rival(self):
		return self.rival

class Ultra(Derecha):
	name = "Alberto"
	attacks = ["Populismo", "Policia", "Franquismo", "Recortes"]
	weakness = ["Logica", "Corrupcion", "Escrache", "Memoria Historica"]

	def get_attacks(self):
		return self.attacks

	def get_weakness(self):
		return self.weakness

	def get_name(self):
		return self.name

class Conservador(Derecha):
	name = "Rajaos"
	attacks = ["Demagogia", "Tribunal Justicia", "Manipulación Mediatica", "Ilegalizacion"]
	weakness = ["Coherencia", "Socialismo", "Coctel", "Humor negro"]

	def get_attacks(self):
		return self.attacks

	def get_weakness(self):
		return self.weakness

	def get_name(self):
		return self.name

class Radical(Izquierda):
	name = "Utegui"
	attacks = ["Coctel", "Escrache", "Humor negro", "Memoria Historica"]
	weakness = ["Populismo", "Tribunal Justicia", "Franquismo", "Ilegalizacion"]

	def get_attacks(self):
		return self.attacks

	def get_weakness(self):
		return self.weakness

	def get_name(self):
		return self.name

class Socialista(Izquierda):
	name = "Xaves"
	attacks = ["Coherencia", "Corrupcion", "Logica", "Socialismo"]
	weakness = ["Demagogia", "Policia", "Recortes", "Manipulacion Mediatica"]

	def get_attacks(self):
		return self.attacks

	def get_weakness(self):
		return self.weakness

	def get_name(self):
		return self.name

################# MENUS (Text Interface) ###################

def combat_menu():
	print "------Debate Combat-------"
	print "Escoge bando político:"
	print "Derecha"
	print "1. Ultra"
	print "2. Conservador"
	print "Izquierda"
	print "3. Radical"
	print "4. Socialista"
	choice = raw_input('> ')
	initial_stage(choice)

def initial_stage(choice):
	player = Player(choice)
	enemy = Enemy(choice)

	print "Presentacion de contricantes!"
	print "-- %r -- vs -- %r --" % (player.get_name(), enemy.get_name())
	print "Se trata de un combate verbal."
	print "Recuerda que la repeticion en politica es contraproducente"

	print "Pulsa Intro para continuar!"
	raw_input('> ')
	combat_engine(player,enemy)

def combat_engine(player,enemy):
	print "\n"
	print "Player Stats"
	print "HP: %r" % player.get_life()
	print "Ataques: "
	i = 1
	for ataque in player.get_attacks():
		print "%d. %r" % (i, ataque)
		i = i + 1

	print "\n"
	print "Enemy Stats"
	print "HP: %r" % enemy.get_life()
	print "\n"
	print "Introduzca ataque a realizar: "

	nextAttack = raw_input('> ')

combat_menu()