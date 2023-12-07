import subprocess
import sys

def check_installation(package_name):
    try:
        # Intenta cargar el paquete
        __import__(package_name)
        print(f"{package_name} ya está instalado.")
        return True
    except ImportError:
        print(f"{package_name} no está instalado.")
        return False

def install_pip():
    try:
        # Intenta instalar pip
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
        print("pip ha sido instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar pip: {e}")

def install_package(package_name):
    try:
        # Intenta instalar el paquete
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} ha sido instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar {package_name}: {e}")

if __name__ == "__main__":
    package_name = "unicode"

    # Verificar si pip está instalado
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        print("pip ya está instalado.")
    except subprocess.CalledProcessError:
        print("pip no está instalado.")
        install_pip()

    # Verificar e instalar el paquete unicode
    if not check_installation(package_name):
        install_package(package_name)