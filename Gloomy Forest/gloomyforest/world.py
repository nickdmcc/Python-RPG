import os.path

_world = {}
starting_position = (0, 0)

def load_tiles():
	"""Parses a file that describes the world space into the _world object"""
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, "../resources/map.txt")
	with open(path, 'r') as f:
		rows = f.readlines()
	x_max = len(rows[0].split('\t')) #Assumes the rest of the rows have the same number of tabs.
	for y in range(len(rows)):
		cols = rows[y].split('\t')
		for x in range(x_max):
			tile_name = cols[x].replace('\n', '') #Windows users may need to replace '\n' with '\r\n'
			if tile_name == "StartingRoom":
				global starting_position
				starting_position = (x, y)
			_world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
	return _world.get((x,y))