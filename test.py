from func import ajouterTache, changerStatus

taches = [] 

# Tests de l'ajout
ajouterTache("Tache1","Desc1",taches)
assert len(taches) == 1
assert taches[0].nomTache == "Tache1"
assert taches[0].descriptionTache == "Desc1"

# Tests du changement de status
changerStatus(taches,0)
assert taches[0].nomTache == True
changerStatus(taches,0)
assert taches[0].nomTache == False