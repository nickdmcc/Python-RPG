import pygame, world
from player import Player

#Fix text render on screen. DONE
#Fix actions and buttons. WIP
#Fix inventory
#Fix enemies and fighting

pygame.init()

#Window size
SIZE = display_width, display_height = (640,638)

#Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
light_red = (180,25,25)

font = pygame.font.SysFont("Franklin Gothic",28)
FPS = 60
screen = pygame.display.set_mode(SIZE,pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption('Gloomy Forest')


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def blit_text(surface, text, pos, font, color=pygame.Color('white')):
	screen.fill(black)
	words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
	space = font.size(' ')[0]  # The width of a space.
	max_width, max_height = surface.get_size()
	x, y = pos
	for line in words:
		for word in line:
			word_surface = font.render(word, 0, color)
			word_width, word_height = word_surface.get_size()
			if x + word_width >= max_width:
				x = pos[0]  # Reset the x.
				y += word_height  # Start on new row.
			surface.blit(word_surface, (x, y))
			x += word_width + space
		x = pos[0]  # Reset the x.
		y += word_height  # Start on new row.

#Need to fix loop
def action_text_tile(action_list,player):
	actionloop = False
	action_string = ["North","South","East","West","Attack","Flee"]
	largeText = pygame.font.SysFont("Franklin Gothic", 30)
	TextSurf, TextRect = text_objects("Choose an action:",largeText,red)
	TextRect.center = (400,330)
	screen.blit(TextSurf,TextRect)
	
	while not actionloop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()	
			if event.type == pygame.MOUSEBUTTONDOWN:
				actionloop = True
				
		for action in action_list:
			if str(action) in action_string:
				if "North" == str(action):
					north_button = button("North",410,350,50,50,red,light_red,action_method,player,action)
				elif "South" == str(action):
					south_button = button("South",410,450,50,50,red,light_red,action_method,player,action)
				elif "East" == str(action):
					east_button = button("East",460,400,50,50,red,light_red,action_method,player,action)
				elif "West" == str(action):
					west_button = button("West",360,400,50,50,red,light_red,action_method,player,action)
				elif "View Inventory" == str(action):
					button("Inventory",100,100,50,50,red,light_red,action_method,player,action)
				elif "Attack" == str(action):
					button("Attack",300,500,50,50,red,light_red,action_method,player,action)
				elif "Flee" == str(action):
					button("Flee",500,500,50,50,red,light_red,action_method,player,action)
					
		update()	
	update()
	
def update():
	pygame.display.update()
	clock.tick(FPS)
	
def action_method(player,action):
	print(action)
	player.do_action(action)

	
def intro_text_tile(intro_text):
	screen.fill(white)
	largeText = pygame.font.SysFont("Franklin Gothic", 20)
	TextSurf, TextRect = text_objects(intro_text,largeText,black)
	TextRect.center = ((display_width/2.5),(display_height/2.5))
	screen.blit(TextSurf,TextRect)
	
def text_objects(text, font, color):
	textSurface = font.render(text,True,color) #True for anti-aliasing
	return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,inactivecolor,activecolor,action=None,*args):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(screen,activecolor,(x,y,w,h))
		if click[0] == 1 and action != None:
			action(*args)
			
	else:
		pygame.draw.rect(screen,inactivecolor,(x,y,w,h))
			
	smallText = pygame.font.SysFont("Franklin Gothic",20)
	textSuf, textRect = text_objects(msg,smallText,black)
	textRect.center = ((x+(w/2)),(y+(h/2)))
	screen.blit(textSuf,textRect)

def quitgame():
	pygame.quit()
	quit()

def get_inventory(player):
	text = "Inventory"
	font = pygame.font.SysFont("Franklin Gothic",40)
	blit_text(screen,text,(40,40),font)
	
	for item in player.inventory:
		break
	
def game_intro():
	intro = False
	while not intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
		
		BackGround = Background('forest_bg.jpg', [0,0])
		screen.fill([255, 255, 255])
		screen.blit(BackGround.image, BackGround.rect)
		largeText = pygame.font.SysFont("Franklin Gothic",80)
		TextSurf, TextRect = text_objects("Gloomy Forest",largeText,red)
		TextRect.center = ((display_width/2),(display_height/3))
		screen.blit(TextSurf,TextRect)
		
		button("Begin",275,275,80,40,red,light_red,game_loop)
		button("Leave",275,340,80,40,red,light_red,quitgame)
		
		pygame.display.update()
		
def game_loop():
	
	world.load_tiles()
	player = Player()
	room = world.tile_exists(player.location_x, player.location_y)
	
	while player.is_alive() and not player.victory:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
	
		#get starting tile for intro text
		#These lines load the starting room and display the text
		room = world.tile_exists(player.location_x, player.location_y)
		print(room)
		room.modify_player(player)
		text = room.intro_text()
		blit_text(screen,text,(40,40),font)
		
		if player.is_alive() and not player.victory:
			
			#put player actions in button format at bottom of the screen
			available_actions = room.available_actions()
			action_list = []
			for action in available_actions:
				action_list.append(action)
			action_text_tile(action_list,player)
			
		update()
		
		#connect tiles for player to traverse through
		#end game when player lands on exit tile
				
game_intro()
quitgame()