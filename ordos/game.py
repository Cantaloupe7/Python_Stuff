""""
Sands of Ordos

A Text Based Survival/Adventure: The Movie: The Novel

By Brian Gregory

-variable naming convention based on highly chaotic pendulum/the humble sea cucumber-
"""

from classes.characters import*
from functions.playercmds import*
from functions.generalfunctions import*

# for functions with arguments given as direct imput from the player, see functions.playercmds
# for functions with arguments given by variables\me\no args, see functions.generalfunctions

Player.mainloop = True
Player.attackloop = False

intro()

#This loop is the game. The game in this loop is better than Bioshock Infinite, but so is everything.
while Player.mainloop is True:

	cmd = raw_input(">>: ").lower().strip()

	if (cmd in cmds_consumables):
		consume(cmd)

	elif (cmd in cmds_move):
		move(cmd)

	elif (cmd in cmds_request):
		request(cmd)

	else:
		print "I'm sorry, I don't know what you mean."
		print ""

	detectenemy()

	while Player.attackloop is True:
		
		cmd = raw_input("You've encountered a " + str(Player.id_enemy.name) + ", attack or flee? : ").lower()

		if cmd in cmds_combat:
			attack(cmd)
		
		if Player.id_enemy.hp <= 0:
			Player.id_enemy.hp = 0
			print "The " + str(Player.id_enemy.name) + " is dead."
			print ""
			Player.attackloop = False
