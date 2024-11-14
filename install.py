import subprocess
import sys

packages = ['pynput']


def install_packages(package_list):
    for package in package_list:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"'{package}' installed successfully!")
        except Exception as e:
            print(f"An error occurred while installing {package}: {e}")


if __name__ == "__main__":
    install_packages(packages)
