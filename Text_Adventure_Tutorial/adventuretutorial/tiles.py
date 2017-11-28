import items, enemies, actions, world

#MapTile is an abstract base class
class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def intro_text(self):
		raise NotImplementedError() #warns when MapTile is being created directly. Instead, we want to create subclasses of tiles.
		
	def modify_player(self, the_player):
		raise NotImplementedError()
		
	def adjacent_moves(self):
		"""Returns all move actions for adjacent tiles."""
		moves = []
		if world.tile_exists(self.x, self.y - 1):
			moves.append(actions.MoveNorth())
		if world.tile_exists(self.x, self.y + 1):
			moves.append(actions.MoveSouth())
		if world.tile_exists(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		return moves
		
	def available_actions(self):
		"""Return all of the available actions in this room."""
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())
		
		return moves
		
class StartingRoom(MapTile):
	def intro_text(self):
		return """
		You find yourself lost in a forest taking a detour to Big City.
		There are four distinct paths to follow, each equally as confusing and twisted as the last.
		"""
	
	def modify_player(self, the_player):
		#Room has no action on player
		pass #Needed so that the superclass doesn't throw an exception

class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)
		
	def add_loot(self, the_player):
		the_player.inventory.append(self.item)
	
	def modify_player(self, the_player):
		if self.item.still_exists():
			self.add_loot(the_player)
			self.item.stock -= 1
		
class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)
		
	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
			
	def available_actions(self):
		if self.enemy.is_alive():
			return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
		else:
			return self.adjacent_moves()
			
class EmptyForestPath(MapTile):
	def intro_text(self):
		return """
		Another path that seems to circle around to where you started. 
		It is hard to distiguish what part of the forest you have been through already.
		"""
		
	def modify_player(self, player):
		pass
		
class WaspRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Wasp())
		
	def intro_text(self):
		if self.enemy.is_alive():
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
		if self.item.still_exists():
			return """
			A rusted dagger is lodged into the top of a lonely tree stump.
			You pick it up!
			"""
		else:
			return """
			The stump is lonely, leaving you wondering where the dagger came from.
			"""

class Find5GoldRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.Gold(5))
		
	def intro_text(self):
		if self.item.still_exists():
			return """
			A patch of dirt on the ground sparkles brightly. Quickly digging it up, you find a Gold coin!
			"""
		else:
			return """
			The patch of dirt on the ground is now a muddy dark color.
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
		
class LeaveForestRoom(MapTile):
	def intro_text(self):
		return """
		You see a bright light in the distance...
		... it grows are you get closer! It's sunlight shining through a thicket of thorns!
		"""
		
	def modify_player(self, player):
		player.victory = True
		