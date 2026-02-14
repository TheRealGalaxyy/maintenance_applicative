
from classes.Tache import Tache

def ajouterTache(nomTache,descriptionTache,taches):
    tache = Tache(nomTache, descriptionTache)
    taches.append(tache)
    print("Tache ajoutée avec succès !\n")

def listerTaches(taches):
    for i in range(len(taches)):
        tache = taches[i]
        status = "En cours"
        if tache.status == True:
            status = "Complété"
        print("\n" + str(i) + " - " + tache.nomTache + " : " + tache.descriptionTache + " (" + status + ").")
    print("\n")
    
def changerStatus(taches, numeroTache):
    tache = taches[int(numeroTache)]
    tache.ChangerStatus()