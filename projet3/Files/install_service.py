import subprocess

def install_apache():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install","-y", "apache2"])

def install_ssh():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install","-y", "openssh-server"])

if __name__ == "__main__":
    install_apache()
    install_ssh()
