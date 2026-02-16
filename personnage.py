class Personnage :
    """Classe pour la création de personnage
    """

    def __init__(self, nom :str, pv :int, attaque :int) :
        self.nom = nom
        self.pv_max = pv
        self.pv = pv
        self.attaque = attaque

    @property
    def pv_max(self) -> int:
        return self._pv_max
    
    @pv_max.setter
    def pv_max(self, nouveau_pv :int) -> None :
        if nouveau_pv < 0 :
            self._pv_max = 0
        elif nouveau_pv > 500 :
            self._pv_max = 500
        else :
            self._pv_max = nouveau_pv

    @property
    def pv(self) -> int:
        return self._pv
    
    @pv.setter
    def pv(self, nouveau_pv :int) -> None :
        if nouveau_pv < 0 :
            self._pv = 0
        elif nouveau_pv > 500 :
            self._pv = 500
        else :
            self._pv = nouveau_pv

    @property
    def attaque(self) -> int :
        return self._attaque
    
    @attaque.setter
    def attaque(self, nouveau_attaque :int) -> None :
        if nouveau_attaque < 0 :
            self._attaque = 0
        elif nouveau_attaque > 50 :
            self._attaque = 50
        else :
            self._attaque = nouveau_attaque
    
    def subir_degat(self, degat :int) -> None :
        """Méthode pour faire subir des dégâts à un personnage

        Args:
            degat (int): Dégâts reçu
        """
        if degat - self.armure.pts_armure < 0 :
            self.pv = self.pv
        else :
            self.pv = self.pv - (degat - self.armure.pts_armure)

    def soigner(self, perso) -> None :
        """Permet de soigner un personnage
        """
        perso.pv = perso.pv_max