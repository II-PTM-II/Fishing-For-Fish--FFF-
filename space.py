import pygame  # necessaire pour charger les images et les sons
# import de la bibliothèque random pour les nombres aleatoires
import random
# import de la bibliothèque math pour les fonctions mathematiques
import math

class Joueur:  # classe pour créer le vaisseau du joueur
    def __init__(self):
        """
        Constructeur de la classe Joueur
        :return:
        """
        self.position = 400
        self.hauteur = 0
        self.depart = self.position
        self.image = pygame.image.load('ᴘᴇᴄʜᴇᴜʀ.png')
        self.image = pygame.transform.scale(self.image, (80, 90))
        self.sens = "O"
        self.vitesse = 5
        self.score = 0
        self.temps = 0
        
    def deplacer(self):
        """
        Fonction qui permet de déplacer le vaisseau du joueur
        :return:
        """
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
            self.depart = self.position
        elif (self.sens == "gauche") and (self.position > 0):
            self.position = self.position - self.vitesse
            self.depart = self.position

    def tirer(self):
        """
        Fonction qui permet de tirer
        :return:
        """
        self.sens = "O"

    def marquer(self):
        """
        Fonction qui permet de marquer un point
        :return:
        """
        self.score = self.score + 1

    def demarquer(self):
        """
        Fonction qui permet de démarquer un point
        :return:
        """
        self.score = self.score - 0

class Balle:  # classe pour créer la balle
    def __init__(self, player):
        """
        Constructeur de la classe Balle
        :param player:
        """
        self.tireur = player
        self.depart = player.position + 16
        self.hauteur = 492
        self.etat = "chargee"
        self.vitesse = 10
        self.type=random.randint(1,2)

        if self.type == 1 :
            self.image = pygame.image.load('ᴀᴘᴘᴀᴛ.png')
            self.image = pygame.transform.scale(self.image, (25, 25))
            self.vitesse = 5
        elif self.type == 2 :
            self.image = pygame.image.load('sᴜᴘᴇʀ ᴀᴘᴘᴀᴛ.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.vitesse  = 7.5        

    def bouger(self):
        """
        Fonction pour faire bouger la balle
        :return:
        """
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree":
            self.hauteur = self.hauteur - self.vitesse
        if self.hauteur < 0:
            self.etat = "chargee"

    def toucher(self, vaisseau, player):
        """
        Fonction qui permet de savoir si la balle touche un ennemi
        :param vaisseau : vaisseau ennemi
        :return: True si la balle touche l'ennemi sinon False
        """
        """
        if (math.fabs(self.depart - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            return True
        """
        if (math.fabs(self.depart - vaisseau.depart) < 40) and (math.fabs(self.hauteur - vaisseau.hauteur) < 40):
            return True
        else:
            if (math.fabs(self.depart - vaisseau.depart) < 40) and (math.fabs(self.hauteur - vaisseau.hauteur) < 40):
                vaisseau.disparaitre()
                player.score -= 10


class Ennemi:
    NbEnnemis = 5

    def __init__(self):
        """
        Constructeur de la classe Ennemi
        """
        self.depart = random.randint(1, 700)
        self.hauteur = 10
        self.type = random.randint(1, 4)
        if self.type == 1:
            self.image = pygame.image.load('ᴘᴏɪssᴏɴ1.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 1.5
        elif self.type == 2:
            self.image = pygame.image.load('ᴘᴏɪssᴏɴ2.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 2.7
        elif self.type == 3:
            self.image = pygame.image.load('ᴘᴏɪssᴏɴ3.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 2
        elif self.type == 4:
            self.image = pygame.image.load('ᴘᴏɪssᴏɴ4.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 1.4        

    def avancer(self):
        """
        Avance l'ennemi d'une distance égale à sa vitesse
        :return:
        """
        self.hauteur = self.hauteur + self.vitesse

    def disparaitre(self):
        """
        Fait disparaitre l'ennemi
        :return:
        """
        self.depart = random.randint(1, 700)
        self.hauteur = 10
        self.type = random.randint(1, 4)
        if self.type == 1:
            self.image = pygame.image.load('ᴘᴏɪssᴏɴ1.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 1.2
        elif self.type == 2:
            self.image = pygame.image.load('ᴘᴏɪssᴏɴ2.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 2.1
        elif self.type == 3:
            self.image = pygame.image.load('ᴘᴏɪssᴏɴ3.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 1
        elif self.type == 4:
            self.image = pygame.image.load('ᴘᴏɪssᴏɴ4.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 0.8       

    def touchPlayer(self, player):
        """
        Fonction qui permet d'appeler demarquer so l'ennemie touche le joueur
        :param player:
        :return:
        """
        if self.hauteur >= 600:
            player.demarquer()
