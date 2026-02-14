from classes.Tache import Tache

continuer = True
taches = []

def ajouterTache():
    nomTache = input("Quel est le nom de votre tache ? :")
    descriptionTache = input("Description de votre tache ? :")
    tache = Tache(nomTache, descriptionTache)
    taches.append(tache)
    print("Tache ajoutée avec succès !\n")

def listerTaches():
    for i in range(len(taches)):
        tache = taches[i]
        status = "En cours"
        if tache.status == True:
            status = "Complété"
        print("\n" + str(i) + " - " + tache.nomTache + " : " + tache.descriptionTache + " (" + status + ").")
    print("\n")
    
def changerStatus():
    numeroTache = input("Veuillez référencer le numéro attribué à la tache :")
    tache = taches[int(numeroTache)]
    status = "En cours"
    if tache.status == True:
        status = "Complété"
    validation = input("Status actuel : " + status + ". Etes vous sur de vouloir changer le status ? (y/n)")
    if validation == "y":
        tache.ChangerStatus()
        print("Status modifié !\n")
    else:
        print ("Opération annulée\n")

while continuer:
    print("Que voulez-vous faire ? Taper le chiffre correspondant :")
    print("1. Ajouter une tache :")
    print("2. Lister vos taches :")
    print("3. Changer le status d'une tache :")
    print("4. Quitter l'application")
    
    choix = input()
    
    if choix == "4":
        continuer = False
    elif choix == "1":
        ajouterTache()
    elif choix == "2":
        listerTaches()
    elif choix == "3":
        changerStatus()
    else:
        print("Choix non reconnu")
        
