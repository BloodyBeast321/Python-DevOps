#!/usr/bin/env python

import subprocess
import os

def execute_shell_script(script_name, *args):
    script_path = os.path.join(os.path.dirname(__file__), "Files", script_name)
    command = [script_path, *args]
    try:
        # Utilisation de check_output pour récupérer la sortie du script shell
        sortie_script = subprocess.check_output(command, shell=False, universal_newlines=True)

        # Affichage de la sortie du script
        print("Sortie du script {} :\n{}".format(script_name, sortie_script))
    except subprocess.CalledProcessError as e:
        # En cas d'erreur lors de l'exécution du script shell
        print("Erreur lors de l'exécution du script {} : {}".format(script_name, e))

if __name__ == "__main__":
    # Exemple d'exécution d'un script sans paramètres
    execute_shell_script("script.sh")

    # Exemple d'exécution d'un script avec des paramètres
    execute_shell_script("parm.sh", "parametre1", "parametre2")
