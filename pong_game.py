import pygame

pygame.init()

win = pygame.display.set_mode((750,500))

pygame.display.set_caption("Let's Play Pong!")
clock = pygame.time.Clock()

white_color = (255,255,255)
black_color = (0,0,0)
red_color = (255,0,0)
blue_color = (0,0,255)

paddle_width = 75
paddle_inc_width = 10

class Paddle(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,paddle_width])
		self.image.fill(white_color)
		self.rect = self.image.get_rect()
		self.points = 0

class Ball(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,10])
		self.image.fill(white_color)
		self.rect = self.image.get_rect()
		self.speed = 10
		self.dirnx = 1
		self.dirny = 1

paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong)

def redrawWindow():
	win.fill(black_color)
	font = pygame.font.SysFont("comicsans", 30)
	text = font.render("PONG", False, red_color)
	textRect = text.get_rect()
	textRect.center = (750 // 2, 25)
	win.blit(text, textRect)

	p1_score = font.render(str(paddle1.points), False, blue_color)
	p1Rect = p1_score.get_rect()
	p1Rect.center = (50, 50)
	win.blit(p1_score, p1Rect)

	p2_score = font.render(str(paddle2.points), False, red_color)
	p2Rect = p2_score.get_rect()
	p2Rect.center = (700, 50)
	win.blit(p2_score, p2Rect)

	all_sprites.draw(win)
	pygame.display.update()

run = True
while run:
	# pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	key = pygame.key.get_pressed()
	if key[pygame.K_w]:
		paddle1.rect.y += -10

	if key[pygame.K_s]:
		paddle1.rect.y += 10

	if key[pygame.K_UP]:
		paddle2.rect.y += -10

	if key[pygame.K_DOWN]:
		paddle2.rect.y += 10

	pong.rect.x += pong.speed*pong.dirnx
	pong.rect.y += pong.speed*pong.dirny

	if pong.rect.y > 490:
		pong.dirny = -1

	if pong.rect.x > 740:
		pong.rect.x, pong.rect.y = 375, 225
		pong.dirnx = -1
		paddle1.points += 1

	if pong.rect.y < 10:
		pong.dirny = 1

	if pong.rect.x < 10:
		pong.rect.x, pong.rect.y = 375, 225
		pong.dirnx = 1
		paddle2.points += 1
		paddle_width += paddle_inc_width

	if paddle1.rect.colliderect(pong.rect):
		pong.dirnx = 1

	if paddle2.rect.colliderect(pong.rect):
		pong.dirnx = -1

	redrawWindow()
	clock.tick(15)

pygame.quit()