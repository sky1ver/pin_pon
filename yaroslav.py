import pygame


back = (150, 0, 150) 
wind_width = 500 
wind_height = 500 
window = display.set_mode((wind_width, wind_height)) 
window.fill(back) 
 
class GameSprite(sprite.Sprite): 
    def init(self, player_image, player_x, player_y, player_speed, player_width, player_height): 
        super(). init() 
        self.image = image.load(loadimage) 
        self.speed = player_speed 
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_f(self):
        keys = key.get_pressed()
        if key[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed
    def update_s(self):
        keys = key.get_pressed()
        if key[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

game = True
game_over = False

clock = time.Clock()
FPS = 60 

platform1 = Player("", 30, 250, 4, 20, 100)
platform2 = Player("", 440, 250, 4, 20, 100)
ball = GameSprite("", 250, 250, 4, 35)

font.init()
font = font.Font('Arial', 30)
loser1 = font. render('Player 1 Lose!', True, (255,215,0))
loser2 = font. render('Player 2 Lose!', True, (250,10,3))

while game:
    for e in envent.get():
        if e.type ==quit:
            geme = geme_over
    if geme_over != True:
        window.fill(back)
        platform1.update_f()
        platform2.update_s()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.colide_rect(ball, platform1) or sprite.colide_rect(ball, platforn2):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > wind_height -10 or ball.rect.y < 0:
            speed_y*=-1
        if boll.rect.x >= wind_width:
            game = False
            window.blit(loser1, (200, 200))
        if ball. rect.x <= 0:
            game = False
            window.blit(loser2, (200, 200))
            platform1.reset()
            platform2.reset()
            ball.reset()

platform1.update_f()


clock(FPS)