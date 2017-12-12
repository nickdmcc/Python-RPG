from player import Player

class Action():
	def __init__(self, method, name):
		self.method = method
		self.name = name
		
	def __str__(self):
		return "{}".format(self.name)
		
class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=Player.move_north, name="North")

class MoveSouth(Action):
	def __init__(self):
		super().__init__(method=Player.move_south, name="South")
		
class MoveEast(Action):
	def __init__(self):
		super().__init__(method=Player.move_east, name="East")
		
class MoveWest(Action):
	def __init__(self):
		super().__init__(method=Player.move_west, name="West")
		
class ViewInventory(Action):
	"""Prints the player's inventory"""
	def __init__(self):
		super().__init__(method=Player.print_inventory, name="View Inventory")
		
class Attack(Action):
	def __init__(self, enemy):
		super().__init__(method=Player.attack, name="Attack", enemy=enemy)
		
class Flee(Action):
	def __init__(self, tile):
		super().__init__(method=Player.flee, name="Flee", tile=tile)