#!/bin/bash

# Vérifie s'il y a des paramètres passés
if [ $# -eq 0 ]; then
    echo "Aucun paramètre n'a été passé."
else
    # Affiche les paramètres un par un
    echo "Les paramètres passés sont :"
    for param in "$@"; do
        echo "$param"
    done
fi
