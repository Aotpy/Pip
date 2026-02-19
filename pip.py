import os
import subprocess
import sys

packages = [
	"os",
    "requests",
    "pytelegrambotapi",  
    "selenium",
    "youtube-dl",
    "colorama",
    "beautifulsoup4",
    "pafy",
    "bs4",
    "instagram-private-api",  # instead of "InstagramAPI"
    "fake-useragent",
    "pysocks",
    "rich",
    "pycryptodome",
    "python-telegram-bot",
    "mechanize",
    "pyfiglet",
    "cfonts",
    "pystyle",
    "pycountry",
    "instaloader",
    "stdiomask",
    "user-agent",
    "generate-user-agent",
    "selenium",
    "curl2pyreqs"
]

def install_packages():
    print("="*50)
    print("Installing Python Packages")
    print("="*50)
    
    for package in packages:
        try:
            print(f"\nInstalling {package}...")
            subprocess.run([sys.executable, "-m", "pip", "install", package], 
                         check=True)
            print(f"✓ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"✗ Failed to install {package}")

if __name__ == "__main__":
    install_packages()
    print("\n" + "="*50)
    print("Installation process completed")
    print("="*50)
