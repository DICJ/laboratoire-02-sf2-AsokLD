class Armure :

    def __init__(self, nom :str, pts_armure :int) :
        self.nom = nom
        self.pts_armure = pts_armure

    def __str__(self):
        return f"Type d'armure : {self.nom}, Points d'armure {self.pts_armure}"

    @property
    def pts_armure(self) -> int :
        return self._pts_armure
    
    @pts_armure.setter
    def pts_armure(self, nouveau_pts :int) -> None :
        if nouveau_pts < 0 :
            self._pts_armure = 0
        elif nouveau_pts > 15 :
            self._pts_armure = 15
        else :
            self._pts_armure = nouveau_pts