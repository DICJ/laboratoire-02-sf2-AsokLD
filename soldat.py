from personnage import Personnage
from armure import Armure

soldat = Armure("Cotte de mailles", 15)

class Soldat(Personnage) :

    def __init__(self, nom, pv, attaque):
        super().__init__(nom, pv, attaque)
        self.armure = soldat

    def __str__(self) -> str :
        return f"Classe : Soldat, Nom : {self.nom}, Points de vie : {self.pv}, Attaque : {self.attaque}"

    def subir_degat(self, degat):
        
        degat = int(degat * 0.9)

    def degat_attaque(self) -> int :
        """Méthode pour attaquer

        Returns:
            int: Nbr de dégâts de l'attaque
        """
        degat = self.attaque

        return degat
    
