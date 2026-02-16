from personnage import Personnage
from arene import Arene
arene = Arene()

# Programme principal
quitter = 1000

while quitter != 0 :
    # Menu principal
    print("------- RAID SHADOW LEGENDS -------")
    print("(1) Ajouter un personnage")
    print("(2) Voir les personnages dans l'arène")
    print("(3) Faire combattre deux personnages")
    print("(4) Soigner un personnage")
    print("(5) Nettoyer l'arène")
    print("(6) Nombre de combattants dans l'arène")
    print("(7) Lancer un fornite battle royal")
    print("(0) Quitter 😢")
    print()

    choix = int(input("Entrez votre choix : "))

    # Choix
    match choix :
        case 1 :
            arene.ajouter_personnage()
        case 2 : 
            arene.afficher_perso()
        case 3 :
            arene.combat()
        case 4 :
            arene.afficher_perso
            perso = int(input("Choississez un perso pour le soigner : "))
            arene.combattants(perso).soigner
        case 5 :
            pass
        case 6 :
            pass
        case 7 :
            pass
        case 0 :
            quitter = 0
        case _ :
            print("Choix invalide, réessayez")
    print()