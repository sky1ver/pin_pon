from pygame import*
back = (123,90,780)
window_width= 500
wind_height= 500
window= display.set_mode((window_width, wind_height))
window.fill(back)

class GameSpraite(sprite.Sprite):
    def __init__(self, plair_image, player_x, player_y, player_speed, player_width, player_neignt):
    super().__init__()
    self.imege= imege.load()
    self.speed=player_speed
    self.rect.x= player_x
    self.rect.y= player_y