#Author: 	Nicholas McCarty 
#Date: 		11/27/17

#Edits (TBD):
#---------------------------------------------------------------------------------

class Item():
	"""The base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
	def __init__(self, amount):
		self.amount = amount
		"""The superclass constuctor must always be called by a subclass constructor"""
		super().__init__(name="Gold", description="A round coin with {} stamped on the front.".format(str(self.amount)),
					value=self.amount)


class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDamage:

class Rock(Weapon):
	def __init__(self):
		super().__init__(name="Rock", description="A fist-sized rock, suitable for bludgeoning.",
					value=0, damage=5)
	
class Dagger(Weapon):
	def __init__(self):
		super().__init__(name="Dagger", description="A small rusty dagger. The pointed end is still sharp.",
					value=10, damage=10)