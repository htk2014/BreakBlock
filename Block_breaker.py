import sys, pygame ,os,time

size = width, height = 500, 500

def collision(o1,o2):
		o1_width = o1.image.get_width();
		o1_hight = o1.image.get_height();
		o2_width = o2.image.get_width();
		o2_hight = o2.image.get_height();
                #rectangle
		o1_rectX = o1.rect.x
		o1_rectY = o1.rect.y
		o2_rectX = o2.rect.x
		o2_rectY = o2.rect.y + 10
	                
		if (o2_rectX >= o1_rectX and o2_rectX <= o1_rectX  + o1_width and		
			o2_rectY > o1_rectY and o2_rectY < o1_rectY  + o1_hight):		
			return True

class Ball():
	def __init__(self):
		self.image = pygame.image.load("./img/ball.bmp")
		self.image = pygame.transform.scale(self.image,(10,10)) 
		self.rect = self.image.get_rect() 
		self.rect.x = 100
		self.rect.y = 250
		self.speed = [5, 6]	

	def _break(self,blocks):
		breakFlag = False
		for block in blocks:
			if collision(block,self):
				blocks.remove(block)
				breakFlag = True
		return breakFlag

	def update(self,panel,blocks):
		self.rect = self.rect.move(self.speed)
		colli = collision(panel,self)
		breakFlag = self._break(blocks)
	
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]
		if (self.rect.top < 0 or self.rect.bottom > height or colli or breakFlag):
			self.speed[1] = -self.speed[1]

	def draw(self,screen):
		screen.blit(self.image, self.rect)
	
	def tuchBottom(self):
		if (self.rect.y + self.rect.height)  >= height:
			return True
		else: return False

class Panel():
	def __init__(self):
		self.image = pygame.image.load("./img/rec.bmp")
		self.image = pygame.transform.scale(self.image,(100,10)) 
		self.rect = self.image.get_rect() 
		self.rect.x = 100
		self.rect.y = 450
		self.width = self.image.get_width()
		self.speed = 10

	def update(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			if (self.rect.x - self.speed) >= 0:
				self.rect.x -= self.speed
		if keys[pygame.K_RIGHT]:
			if (self.rect.x + self.width + self.speed ) <= width:
				self.rect.x += self.speed
	def draw(self,screen):
		screen.blit(self.image, self.rect)
		

blocks = pygame.sprite.Group()

class Blocksprite(pygame.sprite.Sprite):
	
	def __init__(self,location):
		pygame.sprite.Sprite.__init__(self,blocks)
	
                self.image = pygame.image.load("./img/block1.bmp")
		self.image = pygame.transform.scale(self.image,(50,50)) 
		self.rect = self.image.get_rect() 
		self.rect.topleft = location 

def makeBlocks(n):
	for j in range(0,n):
		for i in range(0,10):
        		Blocksprite([50*i,50*j])

class Block_breaker:

	def __init__(self):
		pygame.init()
		self.black = 0, 0, 0

		self.screen = pygame.display.set_mode(size)

		self.ball = Ball()
		self.panel = Panel()
		makeBlocks(2)
	
	def _run(self):
		
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()

			self.panel.update()
			self.ball.update(self.panel,blocks)

			self.screen.fill(self.black)
			
			if self.ball.tuchBottom():
				break

			self.ball.draw(self.screen)
			self.panel.draw(self.screen)
			blocks.draw(self.screen)

			pygame.display.flip()
                        pygame.time.wait(10)

	
def main():
	while 1:
        	Block_breaker()._run()
                time.sleep(0.5)
                

main()
