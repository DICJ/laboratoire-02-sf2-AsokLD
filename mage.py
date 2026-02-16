import random
from personnage import Personnage
from armure import Armure

mage = Armure("Arnure magique", 7)

class Mage(Personnage) :
    """Classe pour la création de guerrier
    """
    def __init__(self, nom :str , pv :int, attaque :int, mana :int) :
        super().__init__(nom, pv, attaque)
        self.mana = mana
        self.armure = mage

    def __str__(self) -> str :
        return f"Classe : Mage, Nom : {self.nom}, Points de vie : {self.pv}, Attaque : {self.attaque}, Mana : {self.mana}"
    
    @property
    def mana(self) -> int :
        return self._mana
    
    @mana.setter
    def mana(self, nouveau_mana :int) -> None :
        if nouveau_mana < 0 :
            self._mana = 0
        elif nouveau_mana > 100 :
            self._mana = 100
        else :
            self._mana = nouveau_mana
    
    def degat_attaque(self) -> int :
        """Méthode pour attaquer

        Returns:
            int: Nbr de dégâts de l'attaque
        """
        if self.mana != 0 :
            degat = self.attaque + 60
        else :
            degat = 0
        
        return degat
    
    def diminuer_mana(self) -> None :
        """Méthode pour diminuer la mana après une attaque
        """
        self.mana = random.randint(15, 25)