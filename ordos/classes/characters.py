class Char:
	def __init__(self, name, hp, pwr, x, y):
		self.name = name
		self.hp = hp
		self.pwr = pwr
		self.x = x
		self.y = y

class Enemy:
	def __init__(self, name, hp, pwr, x, y):
		self.name = name
		self.hp = hp
		self.pwr = pwr
		self.x = x
		self.y = y

	def attack(self):
		Player.hp -= (2*self.pwr)

class location:
	def __init__(self, name, mapsymbol, obstacle, x, y):
		self.name = name
		self.x = x
		self.y = y
		self.obstacle = obstacle
		self.mapsymbol = mapsymbol

Empty_desert = location("empty desert ", "-", False, 0, 0)

Player = Char("default", 100, 2, 0, 0)
Player.damage = 4*Player.pwr
Player.id_location = Empty_desert

# lists of objects with coordinates so they can be found by thier variables,
# such as x and y, instead of thier name for object detection by location
# or other exciting properties!
location_list = []
Enemy_list = []

mapsymbol_palm = "*"
mapsymbol_cactus = "+"
mapsymbol_water = "~"
mapsymbol_wetland = "="

mapsymbol_dungeon = "O"


location_list.append(location("palm grove ", mapsymbol_palm, False, 1, 1))
location_list.append(location("palm grove ", mapsymbol_palm, False, 0, 1))

location_list.append(location("cactus grove ", mapsymbol_cactus, False, -1, -1))
location_list.append(location("cactus grove ", mapsymbol_cactus, False, -2, -1))

location_list.append(location("river ", mapsymbol_water, True, 2, 0))
location_list.append(location("river ", mapsymbol_water, True, 2, 1))
location_list.append(location("river ", mapsymbol_water, True, 2, 2))
location_list.append(location("river ", mapsymbol_water, True, 1, 2))
location_list.append(location("river ", mapsymbol_water, True, 1, 3))
location_list.append(location("shallow marsh ", mapsymbol_wetland, False, 1, 4))
location_list.append(location("river ", mapsymbol_water, True, 1, 5))
location_list.append(location("river ", mapsymbol_water, True, 2, 5))

location_list.append(location("collapsed barrow ", mapsymbol_dungeon, False, 1, -1))
location_list.append(location("crumbling tower ", mapsymbol_dungeon, False, 3, 3))

Enemy_list.append(Enemy("large scorpion", 10, 2, 1, 1))