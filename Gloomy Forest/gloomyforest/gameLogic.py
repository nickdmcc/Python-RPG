import world
from player import Player

def play():
	world.load_tiles()
	player = Player()
	#These lines load the starting room and display the text
	room = world.tile_exists(player.location_x, player.location_y)
	while player.is_alive() and not player.victory:
		room = world.tile_exists(player.location_x, player.location_y)
		room.modify_player(player)
		if player.is_alive() and not player.victory:
			available_actions = room.available_actions()
			action_input = input('Action: ')
			for action in available_actions:
				if action_input == action.hotkey:
					player.do_action(action)
					break

if __name__ == "__main__":
	play()