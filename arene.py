from personnage import Personnage
from guerrier import Guerrier
from mage import Mage
from archer import Archer
from soldat import Soldat

class Arene :
    
    def __init__(self):
        self._combattants = []
    
    def __len__(self) -> int :
        return len(self.combattants)
    @property
    def combattants(self) -> list :
        return self._combattants
    
    @combattants.setter
    def combattants(self, perso : Personnage) -> None :
        self._combattants.append(perso)

    def ajouter_personnage(self) -> None :
        """Fonction pour créer un personnage
        """
        nom = input("Entrez le nom de votre personnage : ")
        pv = int(input("Entrez le nombre de points de vie de votre personnage (entre 0 et 500) : "))
        attaque = int(input("Entrez l'attaque de votre personnage (entre 0 et 50) : "))
        classe = int(input("Choississez la classe du personnage. Guerrier(1), Mage(2), Archer(3) ou Soldat(4) : "))

        match classe :
            case 1 :
                force = int(input("Entrez la force de votre personnage (entre 0 et 50) : "))
                perso = Guerrier(nom, pv, attaque, force)
            case 2 :
                mana = int(input("Entrez le niveau de mana de votre personnage (entre 0 et 100) : "))
                perso = Mage(nom, pv, attaque, mana)
            case 3 :
                dexterite = int(input("Entrez le niveau de dextérité de votre personnage (entre 40 et 70) : "))
                perso = Archer(nom, pv, attaque, dexterite)
            case 4 :
                perso = Soldat(nom, pv, attaque)
        
        self.combattant = perso

    def afficher_perso(self) -> None :
        """Fonction pour afficher la liste de perso
        """
        x = 0
        for perso in self.combattant :
            print(f"({x}) {perso}, {perso.armure}")
            x += 1

    def combat(self) -> None :
        """Fonction pour effectuer un combat
        """
        self.afficher_perso()

        perso1 = int(input("Choississez un premier personnage : "))
        perso2 = int(input("Choississez un second peronnage : "))

        combat = True

        while combat :
            dommage = self.combattant[perso1].attaque

            self.combattant[perso2].subir_degat(dommage)

            if self.combattant[perso2].pv <= 0 :
                print(f"{self.combattant[perso1].nom} à gagné")
                combat = False
            
            dommage2 = self.combattant[perso1].attaque

            self.combattant[perso2].subir_degat(dommage2)

            if self.combattant[perso1].pv <= 0 :
                print(f"{self.combattant[perso2].nom} à gagné")
                combat = False