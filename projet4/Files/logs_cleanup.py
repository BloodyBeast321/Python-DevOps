import os
import datetime

def cleanup_logs(log_directory, days_to_keep):
    try:
        # Obtient la date actuelle
        current_date = datetime.datetime.now()

        # Calcule la date limite pour laquelle les fichiers seront conservés
        threshold_date = current_date - datetime.timedelta(days=days_to_keep)

        # Liste tous les fichiers dans le répertoire des logs
        log_files = [f for f in os.listdir(log_directory) if os.path.isfile(os.path.join(log_directory, f))]

        for log_file in log_files:
            log_file_path = os.path.join(log_directory, log_file)

            # Vérifie si le fichier est plus ancien que la date limite
            if os.path.getmtime(log_file_path) < threshold_date.timestamp():
                # Supprime le fichier
                os.remove(log_file_path)
                print(f"Fichier supprimé : {log_file_path}")

        print("Nettoyage des logs terminé.")

    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

if __name__ == "__main__":
    # Spécifiez le répertoire des logs et le nombre de jours à conserver
    log_directory = "/var/log"
    days_to_keep = 10

    # Appelle la fonction cleanup_logs avec les paramètres spécifiés
    cleanup_logs(log_directory, days_to_keep)
