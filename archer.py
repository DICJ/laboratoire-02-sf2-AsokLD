import random
from personnage import Personnage
from armure import Armure

archer = Armure("Tunique de cuir", 5)

class Archer(Personnage) :
    """Classe pour la création de guerrier
    """
    def __init__(self, nom :str , pv :int, attaque :int, dexterite :int) :
        super().__init__(nom, pv, attaque)
        self.dexterite = dexterite
        self.armure = archer

    def __str__(self) -> str :
        return f"Classe : Archer, Nom : {self.nom}, Points de vie : {self.pv}, Attaque : {self.attaque}, Dextérité : {self.dexterite}"
    
    @property
    def dexterite(self) -> int :
        return self._dexterite
    
    @dexterite.setter
    def dexterite(self, nouveau_dexterite :int) -> None :
        if nouveau_dexterite < 40 :
            self._dexterite = 40
        elif nouveau_dexterite > 70 :
            self._dexterite = 70
        else :
            self._dexterite = nouveau_dexterite
    
    def degat_attaque(self) -> int :
        """Méthode pour attaquer

        Returns:
            int: Nbr de dégâts de l'attaque
        """
        if self._dexterite > random.randint(0, 100) :
            degat = (self.attaque + 15) * 15
        else :
            degat = self.attaque + 15
        
        return degat