import os
import subprocess

def configure_apache():
    subprocess.run(["echo", "<Configuration Apache>", "|", "tee", "/etc/apache2/sites-available/000-default.conf"])

def configure_ssh():
    # Configuration de ssh
    #
    #
    pass

def restart_apache():
    os.system('sudo systemctl restart apache2')

def restart_ssh():
    os.system('sudo systemctl restart ssh')


if __name__ == "__main__":
    configure_apache()
    restart_apache()

    configure_ssh()
    restart_ssh()
