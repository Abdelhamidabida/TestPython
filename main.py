def verifier_securite(ligne):
    croissante = True
    decroissante = True

    for i in range(len(ligne) - 1):
        difference = ligne[i + 1] - ligne[i]
        if difference == 0 or difference > 3 or difference < -3:
            return False
        if difference > 0:
            decroissante = False
        if difference < 0:
            croissante = False

    return croissante or decroissante


compteur_lignes_sures = 0

with open("test.txt") as fichier:
    for ligne in fichier:
        ligne = list(map(int, ligne.split()))
        if verifier_securite(ligne):
            compteur_lignes_sures += 1

print(compteur_lignes_sures)
