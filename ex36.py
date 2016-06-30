# -*- coding: utf-8 -*-
from random import randint   # used to get a random number
from sys import exit		# for quit application

# class Actor:
# 	"""Abstract Class for actors (players and enemies)
# 	Common atributes, not instanciated"""
#
# 	life = 100
# 	isDead = False
# 	attacks = []
# 	weakness = []
#
# 	# stores the attacks used on battle to penalize
# 	usedAttacks = []
#
# 	def set_life(self, life):
# 		self.life = life
# 		if life <= 0:
# 			self.set_isDead(True)
#
# 	def set_isDead(self, isDead):
# 		self.isDead = isDead
# 		if isDead == True:
# 			if isinstance(self, Player):
# 				instance = "player"
# 			elif isinstance(self, Enemy):
# 				instance = "enemy"
# 			game_over(instance)
#
# 	def set_attacks(self, attacks):
# 		self.attacks = attacks
#
# 	def set_weakness(self, weakness):
# 		self.weakness = weakness
#
# 	def get_life(self):
# 		return self.life
#
# 	def get_isDead(self):
# 		return self.isDead
#
# 	def get_attacks(self):
# 		return self.attacks
#
# 	def get_weakness(self):
# 		return self.weakness
#
# 	# add a used attack to the list
# 	def add_used_attack(self, attack):
# 		self.usedAttacks.append(attack)
#
# 	def get_usedAttacks(self):
# 		return self.usedAttacks
#
#
# class Player(Actor):
# 	"""Inheritance from Actor, instances object player"""
# 	def __init__(self, idClass):
# 		if idClass == 1:
# 			self.set_attacks(Ultra().get_attacks())
# 			self.set_weakness(Ultra().get_weakness())
# 			self.name = Ultra().get_name()
# 		elif idClass == 2:
# 			self.set_attacks(Conservador().get_attacks())
# 			self.set_weakness(Conservador().get_weakness())
# 			self.name = Conservador().get_name()
# 		elif idClass == 3:
# 			self.set_attacks(Radical().get_attacks())
# 			self.set_weakness(Radical().get_weakness())
# 			self.name = Radical().get_name()
# 		elif idClass == 4:
# 			self.set_attacks(Socialista().get_attacks())
# 			self.set_weakness(Socialista().get_weakness())
# 			self.name = Socialista().get_name()
#
# 	def get_name(self):
# 		return self.name
#
#
# class Enemy(Actor):
# 	"""Inheritance from Actor, instances object enemy"""
# 	def __init__(self, idClass):
# 		if idClass == 1 or idClass == 2:
# 			rival = Derecha().get_rival
# 			# random number to decide rival
# 			randomNum = randint(3,4)
# 			if randomNum == 3:
# 				self.set_attacks(Radical().get_attacks())
# 				self.set_weakness(Radical().get_weakness())
# 				self.name = Radical().get_name()
# 			elif randomNum == 4:
# 				self.set_attacks(Socialista().get_attacks())
# 				self.set_weakness(Socialista().get_weakness())
# 				self.name = Socialista().get_name()
# 		elif idClass == 3 or idClass == 4:
# 			rival = Izquierda().get_rival
# 			# random number to decide rival
# 			randomNum = randint(1,2)
# 			if randomNum == 1:
# 				self.set_attacks(Ultra().get_attacks())
# 				self.set_weakness(Ultra().get_weakness())
# 				self.name = Ultra().get_name()
# 			elif randomNum == 2:
# 				self.set_attacks(Conservador().get_attacks())
# 				self.set_weakness(Conservador().get_weakness())
# 				self.name = Conservador().get_name()
#
# 	def get_name(self):
# 		return self.name
#
#
# ################# Political Classes #################
#
# class Derecha:
# 	rival = "Izquierda"
#
# 	def get_rival(self):
# 		return self.rival
#
# class Izquierda:
# 	rival = "Derecha"
#
# 	def get_rival(self):
# 		return self.rival
#
# class Ultra(Derecha):
# 	name = "Alberto"
# 	attacks = ["Populismo", "Policia", "Franquismo", "Recortes"]
# 	weakness = ["Logica", "Corrupcion", "Escrache", "Memoria Historica"]
#
# 	def get_attacks(self):
# 		return self.attacks
#
# 	def get_weakness(self):
# 		return self.weakness
#
# 	def get_name(self):
# 		return self.name
#
# class Conservador(Derecha):
# 	name = "Rajaos"
# 	attacks = ["Demagogia", "Tribunal Justicia", "Manipulacion Mediatica", "Ilegalizacion"]
# 	weakness = ["Coherencia", "Socialismo", "Coctel", "Humor negro"]
#
# 	def get_attacks(self):
# 		return self.attacks
#
# 	def get_weakness(self):
# 		return self.weakness
#
# 	def get_name(self):
# 		return self.name
#
# class Radical(Izquierda):
# 	name = "Utegui"
# 	attacks = ["Coctel", "Escrache", "Humor negro", "Memoria Historica"]
# 	weakness = ["Populismo", "Tribunal Justicia", "Franquismo", "Ilegalizacion"]
#
# 	def get_attacks(self):
# 		return self.attacks
#
# 	def get_weakness(self):
# 		return self.weakness
#
# 	def get_name(self):
# 		return self.name
#
# class Socialista(Izquierda):
# 	name = "Xaves"
# 	attacks = ["Coherencia", "Corrupcion", "Logica", "Socialismo"]
# 	weakness = ["Demagogia", "Policia", "Recortes", "Manipulacion Mediatica"]
#
# 	def get_attacks(self):
# 		return self.attacks
#
# 	def get_weakness(self):
# 		return self.weakness
#
# 	def get_name(self):
# 		return self.name
#
# ################# Menus (Text Interface) ###################

# def initial_stage(choice):
#     player = Player(choice)
#     enemy = Enemy(choice)
#
#     print "\n"
# 	print "------------------------------"
# 	print "Presentacion de contricantes!"
# 	print "------------------------------"
# 	print "-- %r -- vs -- %r --" % (player.get_name(), enemy.get_name())
# 	print "------------------------------"
# 	print "Se trata de un combate verbal."
# 	print "Recuerda que la repeticion en politica es contraproducente"
# 	print "------------------------------"
#
# 	# decides who goes first randomly
# 	randomNum = randint(1,2)
# 	if randomNum == 1:
# 		nextTurn = "player"
# 	elif randomNum == 2:
# 		nextTurn = "enemy"
#
# 	print "Pulsa Intro para continuar!"
# 	raw_input('> ')
# 	combat_interface(player,enemy, nextTurn)
#
# def combat_interface(player,enemy, nextTurn):
# 	print "\n"
# 	print "*******************************"
# 	print "%r Stats" % player.get_name()
# 	print "HP: %r" % player.get_life()
# 	print "Ataques: "
# 	i = 1
# 	for attack in player.get_attacks():
# 		print "%d. %r" % (i, attack)
# 		i += 1
# 	print "*******************************"
#
# 	print "\n"
# 	print "*******************************"
# 	print "%r Stats" % enemy.get_name()
# 	print "HP: %r" % enemy.get_life()
# 	print "*******************************"
#
# 	if nextTurn == "player":
# 		attack_player(player, enemy)
# 	elif nextTurn == "enemy":
# 		attack_enemy(player, enemy)
#
# def attack_player(player, enemy):
# 	print "Introduzca ataque a realizar: "
# 	notFound = True
# 	while (notFound):
# 		nextAttack = int(input('> '))
# 		if nextAttack > 0 and nextAttack <= len(player.get_attacks()):
# 			notFound = False
# 		else:
# 			print "No has introducido un valor correcto. Escoge ataque por favor:"
#
# 	combat_engine(nextAttack, player, enemy)
#
# def attack_enemy(player, enemy):
# 	# attacks randomly to player
# 	randomNum = randint(1,4)
#
# 	combat_engine(randomNum, enemy, player)
#
# ################# Combat engine ###################
#
# def combat_engine(nextAttack, player, enemy):
# 	# gets the attack of the list
# 	attack = player.get_attacks()[nextAttack - 1]
#
# 	print "-------------------------------"
# 	print "%r uso %r." % (player.get_name(), attack)
#
# 	if any(usedAttack == attack for usedAttack in player.get_usedAttacks()):
# 		print "Te repites..., no ha sido muy efectivo"
# 		print "-------------------------------"
# 		enemy.set_life(enemy.get_life() - 20)
# 	else:
# 		if any(weak == attack for weak in enemy.get_weakness()):
# 			print "El ataque ha sido muy efectivo!!!"
# 			print "-------------------------------"
# 			enemy.set_life(enemy.get_life() - 50)
# 		else:
# 			print "No ha causado mucho efecto"
# 			print "-------------------------------"
# 			enemy.set_life(enemy.get_life() - 30)
#
# 	print "*******************************"
#
# 	player.add_used_attack(attack)
#
# 	if isinstance(player, Player):
# 		nextTurn = "enemy"
# 		combat_interface(player,enemy, nextTurn)
# 	elif isinstance(player, Enemy):
# 		nextTurn = "player"
# 		combat_interface(enemy, player, nextTurn)
#
# def game_over(instance):
# 	if instance == "player":
# 		print "No has podido aplastar a tu rival..."
# 	elif instance == "enemy":
# 		print "Has aplastado a tu rival!"
# 	print "******FIN DE LA PARTIDA******"
# 	exit(0)

def show_main_menu():
    print('''
    ------Debate Combat-------
    Escoge bando politico:
    --------------------------
    Derecha
    1. Ultra
    2. Conservador
    --------------------------
    Izquierda
    3. Radical
    4. Socialista
    --------------------------
    ''')
    choice = int(input('> '))
    while choice < 1 or choice > 4:
        print("No has introducido un valor correcto. Escoge bando por favor:")
        choice = int(input('> '))
    #initial_stage(choice)

if __name__ == '__main__':
    show_main_menu()
