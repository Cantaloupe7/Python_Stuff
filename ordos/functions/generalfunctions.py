from functions.playercmds import*
from classes.characters import*
import os

def clear():
	if (os.name in ('ce', 'nt', 'dos')):
		os.system('cls')
	elif ('posix' in os.name):
		os.system('clear')
	else:
		clear_l = "\n" * 100
		print str(clear_l)

# Checks location list (see classes.charachters) for any location objects at the player's coords or
# plus a certain x (dx) or y (dy) value to check a desired location near the player,
def detectlocation(dx,dy):
	for location in location_list:
		if (location.x == (Player.x + dx)) and (location.y == (Player.y + dy)):
			Player.id_location = location
			break	
	else:
		Player.id_location = Empty_desert

def detectmap(dx,dy):
	for location in location_list:
		if (dx == 0) and (dy == 0):
			return "@"
		elif (location.x == (Player.x + dx)) and (location.y == (Player.y + dy)):
			return location.mapsymbol
			break	
	else:
		return Empty_desert.mapsymbol

#clears the screen and draws a map, this needs to be exectuted before any new text
#is placed on the screen, as to "refresh" and create a game-like GUI
def showmap():
	clear()
	xcount = -8
	ycount = 6
	print ""
	while xcount <= 8:
		xcount += 1
		if (xcount < 8):
			print str(detectmap(xcount,ycount)),

		if (xcount == 8):
			xcount = -8
			print str(detectmap(xcount,ycount))
			ycount -= 1

		if (ycount == -6):
			break	

	print ""
	detectlocation(0,0)
	print str(Player.name) + " is at " + str(Player.x) + "," + str(Player.y) + ", " + str(Player.id_location.name)
	print ""

# uses detectlocation(dx,dy) in functions.generalfunctions to display all locations in a 
# 3x3 grid around the player
def lookaround():
	showmap()
	print "You see..."
	detectlocation(0,1) 
	print str(Player.id_location.name) + "to the north."
	detectlocation(1,1) 
	print str(Player.id_location.name) + "to the northeast."
	detectlocation(1,0) 
	print str(Player.id_location.name) + "to the east."
	detectlocation(1,-1) 
	print str(Player.id_location.name) + "to the southeast."
	detectlocation(0,-1) 
	print str(Player.id_location.name) + "to the south."
	detectlocation(-1,-1) 
	print str(Player.id_location.name) + "to the southwest."
	detectlocation(-1,0) 
	print str(Player.id_location.name) + "to the west."
	detectlocation(-1,1) 
	print str(Player.id_location.name) + "to the northwest."
	print ""

# Checks Enemy list (see classes.characters) for any located at the player's coords,
# if so, enable attack loop as long as the enemy is not dead
def detectenemy():
	for Enemy in Enemy_list:
		if (Enemy.x == Player.x) and (Enemy.y == Player.y) and (Enemy.hp > 0):	
			Player.attackloop = True
			Player.id_enemy = Enemy
			break


def attack(cmd):
	showmap()
	if (cmd == "attack"):
		Player.id_enemy.hp -= Player.damage #todo: randomize and base on player pwr variable
		print "You hit the " + str(Player.id_enemy.name) + " for " + str(Player.damage) + " damage."
		print "The " + str(Player.id_enemy.name) + " has " + str(Player.id_enemy.hp) + " health"

		if (Player.id_enemy.hp > 0):
			Player.id_enemy.attack()
			print "The " + str(Player.id_enemy.name) + " hits you for " + str(2*Player.id_enemy.pwr) + " damage."
			print "You have " + str(Player.hp) + " health."

	if (cmd == "flee"):
		chance_flee = random(0,1) #todo: change these randrange values based on player agility stat variable
		if (chance_flee == 0):
			Player.id_enemy.attack()
			print "The " + str(Player.id_enemy.name) + " hits you as you attempt to flee for " + str(2*Player.id_enemy.pwr) + " damage."
			print "You have " + str(Player.hp) + " health."
		if (chance_flee == 1):
			chance_movex = random(-1,1)  
			chance_movey = random(-1,1)
			Player.y += chance_movex
			Player.x += chance_movey
			Player.attackloop = False
			print "You sucessfully escape to " + str(Player.x) + "," + str(Player.y) + "... "
			detectlocation(0,0)
	print ""

# for less dense recalculation
def random(a,b):
	import random
	return random.randint(a,b)

def intro():
	Player.name = raw_input("To begin, enter your name: ")
	print ""
	print "Welcome to Ordos, " + str(Player.name)
	print ""
	print "Ordos is an arid land divided by tiles, they are organized by coordinates of the form (x,y) or (west-east,south-north)"
	print ""
	print "Simply type 'go north' or just 'north' to head from tile (0,0) to (0,1) and you will see your new tile location and its description."
	print ""
	print "This works in all four cardinal directions, but be careful."
	print ""
	print "Type 'look around' to see descriptions of nearby tiles so you know where you're going."
	print ""
	print "Empty deserts are open regs and ergs with nothing of interest, but moving to any other type of tile can have unforseen consequences!"
	print ""
	print "Type 'status' to view your health at any time, 'exit' to quit or 'help' for more commands!"
	print ""