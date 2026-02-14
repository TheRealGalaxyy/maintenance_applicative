from func import ajouterTache, listerTaches, changerStatus

continuer = True
taches = []

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
        nomTache = input("Quel est le nom de votre tache ? :")
        descriptionTache = input("Description de votre tache ? :")
        ajouterTache(nomTache, descriptionTache, taches)
    elif choix == "2":
        listerTaches(taches)
    elif choix == "3":
        changerStatus(taches)
    else:
        print("Choix non reconnu")
        
