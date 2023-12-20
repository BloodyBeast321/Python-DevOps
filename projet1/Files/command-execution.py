import subprocess

# Commande à exécuter
commande = "ls -l"

# Exécution de la commande
try:
    # Utilisation de check_output pour récupérer la sortie de la commande
    sortie_commande = subprocess.check_output(commande, shell=True, universal_newlines=True)

    # Affichage de la sortie
    print("Sortie de la commande :\n", sortie_commande)
except subprocess.CalledProcessError as e:
    # En cas d'erreur lors de l'exécution de la commande
    print("Erreur lors de l'exécution de la commande :", e)
