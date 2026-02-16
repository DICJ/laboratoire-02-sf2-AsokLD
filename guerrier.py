import random
from personnage import Personnage
from armure import Armure

guerrier = Armure("Armure de plaque", 12)

class Guerrier(Personnage) :
    """Classe pour la création de guerrier
    """
    def __init__(self, nom :str , pv :int, attaque :int, force :int) :
        super().__init__(nom, pv, attaque)
        self.force = force
        self.armure = guerrier

    def __str__(self) -> str :
        return f"Classe : Guerrier, Nom : {self.nom}, Points de vie : {self.pv}, Attaque : {self.attaque}, Force : {self.force}"
    
    @property
    def force(self) -> int :
        return self._force
    
    @force.setter
    def force(self, nouveau_force :int) -> None :
        if nouveau_force < 0 :
            self._force = 0
        elif nouveau_force > 50 :
            self._force = 50
        else :
            self._force = nouveau_force
    
    def degat_attaque(self) -> int :
        """Méthode pour attaquer

        Returns:
            int: Nbr de dégâts de l'attaque
        """
        degat = self.attaque + (self.force/2) + random.randint(-2, 2)

        return degat