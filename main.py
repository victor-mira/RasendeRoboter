#j'ai juste créé un main même si y a rien dedans pour l'instant
import affichage
import mission
import plateau
from robot import *
import etat
import GraphSearchStrategies
activeMission = mission.multicolore
initialState = etat.Etat(plateau.plateauJeu, robotRouge, robotJaune, robotVert, robotBleu, activeMission, 0)

GraphSearchStrategies.Astar(initialState, 1)
affichage.window.mainloop()

"""
class Jeu(object):
    nbJoueur = 1
    difficulty = 1

    def __init__(self,nbJoueur,difficulty):
        self.nbJoueur = nbJoueur
        self.difficulty = difficulty
        for i in range(0, 16):
            for j in range(0, 16):
                # DrawCase(fenetre, plaque.plaque1.element[j][i]).grid(row = i, column = j)
                affichage.DrawCase(affichage.fenetre, plateau.plateauJeu.plat[j][i]).grid(row=i, column=j)

        affichage.fenetre.pack(expand=True)
        affichage.window.mainloop()

print("Bonjour Bienvenue dans le Jeu Rasende Roboter")
print("Combien de joueur êtes vous ? ")
nbJoueur = input("Nombre de joueur:")
print("Quel niveau de difficulté:")
print("Entre:")
print("1 : Facile")
print("2 : normal")
print("3 : difficile")
difficulty = input("Niveau de difficulté:")
jeu = Jeu(nbJoueur,difficulty)
"""




