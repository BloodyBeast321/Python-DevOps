import psutil

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Utilisation CPU : {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    print(f"Utilisation mémoire : {memory_info.percent}%")

def check_disk_space():
    disk_info = psutil.disk_usage('/')
    print(f"Espace disque utilisé : {disk_info.percent}%")

if __name__ == "__main__":
    print("Vérification de l'état du serveur :")
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
