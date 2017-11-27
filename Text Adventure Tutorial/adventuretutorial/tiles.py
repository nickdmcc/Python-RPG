import items, enemies

#MapTile is an abstract base class
class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def intro_text(self):
		raise NotImplementedError() #warns when MapTile is being created directly. Instead, we want to create subclasses of tiles.
		
	def modify_player(self, player):
		raise NotImplementedError()
		
class StartingRoom(MapTile):
	def intro_text(self):
		return """You find yourself lost in a forest taking a detour to Big City.
				  There are four distinct paths to follow, each equally as confusing and twisted as the last.
			   """
	
	def modify_player(self, player):
		#Room has no action on player
		pass #Needed so that the superclass doesn't throw an exception

class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)
		
	def add_loot(self, player):
		player.inventory.append(self.item)
	
	def modify_player(self, player):
		self.add_loot(player)
		
class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)
		
	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
			
class EmptyForestPath(MapTile):
	def intro_text(self):
		return """
		Another path that seems to circle around to where you started. It is hard to distiguish what part of the forest you have been through already.
		"""
		
	def modify_player(self, player):
		pass
		
class WaspRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Wasp())
		
	def intro_text(self):
		if self.enemy,is_alive():
			return """
			A fist sized Wasp emerges from a hole in a tree and attacks!
			"""
		else:
			return """
			The Wasp has been squished.
			"""
			
class FindDaggerRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.Dagger())
		
	def intro_text(self):
		return """
		A rusted dagger is lodged into the top of a lonely tree stump.
		You pick it up!
		"""

class FindGoldRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.Gold())
		
	def intro_text(self):
		return """
		A patch of dirt on the ground sparkles brightly. Quickly digging it up, you find a Gold coin!
		"""
		
class MantisRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Mantis())
		
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			A small tree suddenly moves. The roots stick out like long insect legs.
			You recognize what it is, a Mantis, and it is racing towards you with its arms ready to strike!
			"""
		else:
			return """
			The Mantis has been defeated.
			"""
		
		