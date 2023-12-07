import subprocess
import sys

MODULE = "unidecode"

def check_installation():
    try:
        __import__(f"{MODULE}")
        print(f"{MODULE} ya está instalado.")
        return True
    except ImportError:
        print(f"{MODULE} no está instalado.")
        return False

def install_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
        print("pip ha sido instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar pip: {e}")

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} ha sido instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar {package_name}: {e}")

if __name__ == "__main__":
    package_name = "unicode"

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        print("pip ya está instalado.")
    except subprocess.CalledProcessError:
        print("pip no está instalado.")
        install_pip()

    if not check_installation():
        install_package(package_name)