class Tache():
    def __init__(self, nomTache, descriptionTache):
        self.nomTache = nomTache
        self.descriptionTache = descriptionTache
        self.status = False

    def ChangerStatus(self):
        if self.status == False:
            self.status = True
        else: 
            self.status = False

