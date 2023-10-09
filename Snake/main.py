import pygame
import sys, random



class Game:
    #contenir toutes les variables + fonctions utiles pour le bon déroulement du jeu

    def __init__(self) -> None:
        #variables pour création de la fenêtre du jeu
        self.x, self.y = 800, 600
        self.ecran = pygame.display.set_mode((self.x,self.y))
        pygame.display.set_caption('Snake Game')
        self.jeu_encours = True
        self.clock = pygame.time.Clock() 
        self.image = pygame.image.load('snake_game.jpg').convert_alpha()
        self.image_titre = pygame.transform.scale(self.image, (200,100))
        self.image_head = pygame.image.load('snake_head.png')
        self.ecran_du_debut = True

        #variable pous création du snake
        self.snake_position_x = 300
        self.snake_position_y = 300
        self.snake_direction_x = 0
        self.snake_direction_y = 0
        self.snake_body = 10
        self.snake_taille = 1
        self.score = 0

        #variables pour création de la pomme
        self.pomme = 10
        self.position_pomme_x = random.randrange(10,(self.x-10),10)
        self.position_pomme_y = random.randrange(10,(self.y-10),10)

        #créer une liste qui recense les positions du snake
        self.snake_positions = []

    
    def begin(self):
        while self.ecran_du_debut :
            for evenement in pygame.event.get():
            #pour quitter le jeu
                if evenement.type == pygame.QUIT:
                    sys.exit()
                
                #pour commencer le jeu
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.ecran_du_debut = False
                self.ecran.fill((0,0,0))
                self.ecran.blit(self.image_titre, (290,50,100,50))
                self.creer_message("grande", (255,255,255), "Bienvenue sur le jeu du Snake", (220,170,100,50))
                self.creer_message("moyenne", (255,255,255), "Le but du jeu est de bouffer le max de pomme", (200,400,100,50))
                self.creer_message("moyenne", (255,255,255), "Attention à ne pas toucher les bords !!", (230,430,100,50))
                self.creer_message("petite", (255,255,255), "Appuyer sur entrer pour jouer !!", (290,500,100,50))
                pygame.display.flip()
        self.start_game()
        
    
    def creer_message(self, font, couleur, message, position_message):
        if font == 'petite':
            font = pygame.font.SysFont('Cambria Math', 15, False)
        if font == 'moyenne':
            font = pygame.font.SysFont('Calibri', 20, False)
        if font == 'grande':
            font = pygame.font.SysFont('Calibri', 30, True)
        
        message = font.render(message, True, couleur)
        self.ecran.blit(message, position_message)

    def start_game(self):   
        while self.jeu_encours:
            for evenement in pygame.event.get():
            #pour quitter le jeu
                if evenement.type == pygame.QUIT:
                    sys.exit()
            #réduire les fps
            self.clock.tick(15)
            self.screen_limit() 
            self.snake()
            self.la_pomme()
            self.snake_move()
            self.snake_grow_up()
            self.snake_dead()
            self.creer_message("petite", (255,255,255), "Score: {}".format(self.score), (10,10,100,50))
            #actualiser la fenêtre
            pygame.display.flip()
            self.ecran.fill((0,0,0))

    def screen_limit(self):
        pygame.draw.rect(self.ecran, (255,255,255), (0,0,800,600), 3)
        #créer la cond si le snake dépasse la limite de l'écran
        if self.snake_position_x >= self.x or self.snake_position_x < 0 \
            or self.snake_position_y >= self.y or self.snake_position_y < 0:
            print('Game Over')
            sys.exit()
    
    def snake(self):
        #créer le snake
        # pygame.draw.rect(self.ecran, (0,255,0), (self.snake_position_x, self.snake_position_y, self.snake_body, self.snake_body))
        self.ecran.blit(self.image_head, (self.snake_position_x, self.snake_position_y, self.snake_body, self.snake_body))
        #créer une liste pour stocker la position de la tête du serpent
        self.snake_head = []
        self.snake_head.append(self.snake_position_x)
        self.snake_head.append(self.snake_position_y)
        #append la tête du snake dans la liste des ses positions
        self.snake_positions.append(self.snake_head)

        if len(self.snake_positions) > self.snake_taille:
            self.snake_positions.pop(0)
        print(self.snake_positions)

        #afficher les autres parties du snake      
        for snake_parts in self.snake_positions[:-1]:
            pygame.draw.rect(self.ecran, (0,255,0), (snake_parts[0], snake_parts[1], self.snake_body, self.snake_body))
            
    def la_pomme(self):
        #créer la pomme
        pygame.draw.rect(self.ecran, (255,0,0), (self.position_pomme_x, self.position_pomme_y, self.pomme, self.pomme))

    def snake_move(self):
        for evenement in pygame.event.get():
            #bouger le snake
            if evenement.type == pygame.KEYUP:
                if evenement.key == pygame.K_RIGHT:
                    self.snake_direction_x = 10
                    self.snake_direction_y = 0
                if evenement.key == pygame.K_DOWN:
                    self.snake_direction_x = 0
                    self.snake_direction_y = 10
                if evenement.key == pygame.K_LEFT:
                    self.snake_direction_x = -10
                    self.snake_direction_y = 0
                if evenement.key == pygame.K_UP:
                    self.snake_direction_x = 0
                    self.snake_direction_y = -10

        self.snake_position_x += self.snake_direction_x
        self.snake_position_y += self.snake_direction_y
    
    def snake_grow_up(self):
        #créer la cond si le snake mange une pomme
        if self.snake_position_x == self.position_pomme_x and self.snake_position_y == self.position_pomme_y:
            print('Good')
            self.position_pomme_x = random.randrange(10,(self.x-10),10)
            self.position_pomme_y = random.randrange(10,(self.y-10),10)
            #augmenter la taille du snake
            self.snake_taille += 1
            self.score += 1

    def snake_dead(self):
        #créer la cond si le snake se mord la queue
        for snake_part in self.snake_positions[:-1]:
            if self.snake_head == snake_part:
                print("Game Over")
                sys.exit()


if __name__ == "__main__":
    pygame.init()     
    Game().begin()
    pygame.quit()
    
        