from functions.generalfunctions import*
from classes.characters import*

# lists to screen raw imput for valid commands\which function
cmds_consumables = [
	"drink philter",
	"drink poison"
]
cmds_combat = [
	"attack",
	"flee"
]
cmds_request = [
	"status",
	"look around",
	"exit",
	"map"
]
cmds_move = [
	"go north","north","n",
	"go south","south","s",
	"go west","west","w",
	"go east","east","e"
]

def consume(cmd):
	showmap()
	if (cmd == "drink poison"):
		Player.hp -= 100
		print str(Player.name) + " now has " + str(Player.hp) + " health."

	if (cmd == "drink philter"):
		Player.hp += 20
		print str(Player.name) + " now has " + str(Player.hp) + " health."

	print ""

def move(cmd): 
	if (cmd == "go north") or (cmd == "north") or (cmd == "n"):
		dx = 0
		dy = 1
	if (cmd == "go south") or (cmd == "south") or (cmd == "s"):
		dx = 0
		dy = -1
	if (cmd == "go east") or (cmd == "east") or (cmd == "e"):
		dx = 1
		dy = 0
	if (cmd == "go west") or (cmd =="west") or (cmd == "w"):
		dx = -1
		dy = 0

	detectlocation(dx,dy)

	if Player.id_location.obstacle == False:
		Player.x += dx
		Player.y += dy
		showmap()
	else:
		showmap()
		detectlocation(dx,dy) #If not refreshed, shows the player's locale instead of his attempted move, not sure why...
		print "You can't cross into the " + str(Player.id_location.name)
	print""

# includes all raw imput requests linked to pure info
def request(cmd):
	showmap()

	if (cmd == "exit"):
		Player.mainloop = False

	if (cmd == "status"):
		print str(Player.name) + " has " + str(Player.hp) + " health..."
		if (Player.hp <= 10):
			print "you're practically dead!"
		if (Player.hp > 10) and (Player.hp < 50):
			print "you might want to drink a philter"
		if (Player.hp >= 50):
			print "you'll be just fine."
		print ""
	
	if (cmd == "look around"):
		lookaround()