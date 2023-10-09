import sys
import pygame




pygame.init()


       
    

class Music :

    def __init__(self):

        self.background_sound_start = 'ressources/Sound/background_sound_start.wav'
        self.background_sound_game = 'ressources/Sound/background_sound_game.wav'
        # self.explosion_sound = pygame.mixer.Sound('ressources/Sound/explosion.wav')
        # self.laser_sound = pygame.mixer.Sound('ressources/Sound/shoot.wav')
    
    def play_sound(self, sound):
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(-1)
    

class Background:

    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Space Invader Game')
        self.background_start = pygame.image.load('ressources/Image/background_start.png').convert_alpha()
        self.background_start = pygame.transform.scale(self.background_start, (800,600))
        self.background_game = pygame.image.load('ressources/Image/background_game.jpg').convert_alpha()
        self.background_game = pygame.transform.scale(self.background_game, (800,600))
        self.space_invader_logo = pygame.image.load('ressources/Image/space_invader_logo.png').convert_alpha()
        self.space_invader_logo = pygame.transform.scale(self.space_invader_logo, (300,200))
        self.press_start = pygame.image.load('ressources/Image/press_start.gif').convert_alpha()
        self.press_start = pygame.transform.scale(self.press_start, (150,70))
        self.player_1 = pygame.image.load('ressources/Image/player_ship.png')
        self.player_1 = pygame.transform.scale(self.player_1, (50,80))
        self.ennemy = pygame.image.load('ressources/Image/ennemy.gif').convert_alpha()
        self.ennemy = pygame.transform.scale(self.ennemy, (50,80))

    def display_background(self, image, x, y):
        self.x, self.y = x, y
        self.screen.blit(image, (self.x, self.y))


class Character:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.direction_x = 0
        self.direction_y = 0
        self.background = Background()

    def ch_body(self, body):
        self.background.screen.blit(body, (self.x, self.y))


class Player(Character):
    
    def move(self):

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.direction_x = 0
                    self.direction_y = -10
                if event.key == pygame.K_DOWN:
                    self.direction_x = 0
                    self.direction_y = 10
                if event.key == pygame.K_RIGHT:
                    self.direction_x = 10
                    self.direction_y = 0
                if event.key == pygame.K_LEFT:
                    self.direction_x = -10
                    self.direction_y = 0
                
        self.x += self.direction_x
        self.y += self.direction_y

# class Ennemy(Character):


class Game:

    def __init__(self):
        player_x, player_y = 380, 500
        ennemy_x, ennemy_y = 480, 100
        self.background = Background()
        self.music = Music()
        self.character_player = Character(player_x, player_y)
        self.character_ennemy = Character(ennemy_x, ennemy_y)
        self.player = Player(player_x, player_y)
        self.gameintro = True
        self.gameplay = True

    def game_intro(self):
        
        self.music.play_sound(self.music.background_sound_start)

        while self.gameintro :
            self.background.display_background(self.background.background_start, 0, 0)
            self.background.display_background(self.background.space_invader_logo, 250, 100)
            self.background.display_background(self.background.press_start, 320, 450)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.gameintro = False
            pygame.display.flip()

        self.game_play()

    def game_play(self):

        self.music.play_sound(self.music.background_sound_game)

        while self.gameplay :
            self.background.display_background(self.background.background_game, 0, 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.character_player.ch_body(self.background.player_1)
            self.character_ennemy.ch_body(self.background.ennemy)
            self.player.move()
            pygame.display.flip()



    # def display_background_game(self):

    #     game_processing = True
    #     while game_processing :
    #         self.screen.blit(background_game, (0,0,0,0))
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 sys.exit()
    #         character_player = Character(player_x, player_y)
    #         character_ennemy = Ennemy(ennemy_x, ennemy_y)
    #         character_player.body()
    #         character_ennemy.body()
    #         character_player.player_move()
    #         pygame.display.flip()
    

    

# class Character:
    
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#         self.direction_x = 0
#         self.direction_y = 0
#         self.body = player_1

#     def body(self):
#         screen.blit(self.body, (self.x, self.y,0,0))
    


# class Ennemy(Character):
#     def __init__(self, x, y) -> None:
#         super().__init__(x, y)
#         self.body = ennemy





if __name__ == '__main__':
    Game().game_intro()