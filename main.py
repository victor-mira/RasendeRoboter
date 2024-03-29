import GraphSearchStrategies
import affichage
import etat
import mission
import plateau
from robot import *

class Jeu(object):
    nbJoueur = 1
    listePoint = [0]*999#liste contenant les point
    listeScore = [0]*999#liste contenat les scores des joueurs à chaque manche

    def __init__(self,nbJoueur,listeMission,activeMission):
        self.nbJoueur = int(nbJoueur)
        #Initialise l'état initial
        self.initialState = etat.Etat(plateau.plateauJeu, robotRouge, robotJaune, robotVert, robotBleu,activeMission, 0)

        #Met les points à 0
        print("\n----------------------DEBUT DE LA PARTIE----------------------\n")
        for i in range(self.nbJoueur+1):
            self.listePoint[i] = 0
        while listeMission != []:
            print("\n----------------------DEBUT DE LA MANCHE----------------------\n")
            print("Mission : " + activeMission.accessContenu())#Montre la mission
            affichage.affichagePlateau(self.initialState.robotRouge, self.initialState.robotJaune, self.initialState.robotVert,self.initialState.robotBleu,activeMission)
            print("recherche de solution...\n")
            self.node = GraphSearchStrategies.Astar(self.initialState, 1)#Cherche une solution pour IA
            if self.node == False :
                self.listeScore[0] = 999
            else :
                self.initialState = self.node.State
                self.listeScore[0] = self.initialState.cost
            self.tour()
            listeMission.remove(activeMission)
            if listeMission != []:#Si non vide alors retire et change de mission
                activeMission = random.choice(listeMission)
                self.initialState.mission = activeMission
                self.initialState.cost = 0
        self.finPartie()

    def comptagePoint(self):#Compte les points en fonction du vainqueur de la manche
        maxi = 999
        global meilleurJoueur
        for i in range(self.nbJoueur+1):
            if self.listeScore[i] <= maxi:
                maxi = self.listeScore[i]
                meilleurJoueur = i
        self.listePoint[meilleurJoueur] = self.listePoint[meilleurJoueur] + 1
        print("\n----------------------FIN DE LA MANCHE----------------------\n")
        #Print le vainqueur de la manche
        if meilleurJoueur == 0:
            print("IA gagne la manche")
        else:
            print("Joueur n°" + str(meilleurJoueur) + " gagne la manche")
        print("Les scores sont :")
        #Print les scores
        print("IA : " + str(self.listePoint[0]) + " Points")
        for i in range(self.nbJoueur):
            print("Joueur n°" + str(i+1) + " :" + str(self.listePoint[i+1]) + " Points")
    def tour(self):#Joue le tour de jeu
        #demande les scores de chaque joueur
        for i in range(self.nbJoueur):
            self.listeScore[i+1] = input("Joueur n°" + str(i + 1) + " quel est votre résultat:")
            self.listeScore[i+1] = int(self.listeScore[i+1])
        if self.listeScore[0] == 999:
            print("L'IA n'a pas trouvé :/ \n")
        else :
            print("L'IA a trouvé {} \n".format(self.listeScore[0]))
            GraphSearchStrategies.getStringPath(GraphSearchStrategies.getPathFrom(self.node)) #affiche la solution de l'IA
        self.comptagePoint()

    def finPartie(self):#Donne le vainqueur et les scores final
        maxi = 0
        global meilleurJoueur
        for i in range(self.nbJoueur+1):
            if self.listePoint[i] >= maxi:
                maxi = self.listePoint[i]
                meilleurJoueur = i
        print("\n----------------------FIN DE LA PARTIE----------------------\n")
        if meilleurJoueur == 0:
            print("IA gagne la partie avec " + str(maxi) + " Point")
        else:
            print("Joueur n°" + str(meilleurJoueur) + " gagne la partie avec " + str(maxi) + " Point")
        input()



#mission.triangleJaune, mission.triangleRouge,mission.triangleBleu, mission.triangleVert, mission.carreJaune, mission.carreVert, mission.carreRouge,
    # mission.carreBleu, mission.losangeJaune, mission.losangeVert, mission.losangeRouge, mission.losangeBleu, mission.cercleJaune, mission.cercleVert, mission.cercleBleu, mission.cercleRouge
listeMission =  [mission.multicolore,mission.carreRouge, mission.carreBleu, mission.carreVert, mission.carreJaune, mission.triangleRouge, mission.triangleVert,mission.triangleBleu]
print("Bonjour Bienvenue dans le Jeu Rasende Roboter")
print("Combien de joueur êtes vous ? ")
nbJoueur = input("Nombre de joueur:")
print("generation de l'etat initial...\n")

jeu = Jeu(nbJoueur,listeMission,random.choice(listeMission))#Démarrage du jeu




