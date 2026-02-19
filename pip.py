import subprocess
import sys

# ===============================
# OBITO CLEAN AUTO INSTALLER
# ===============================

packages = [
    "requests",
    "pyfiglet",
    "colorama",
    "rich",
    "fake-useragent",
    "user-agent",
    "beautifulsoup4",
    "pysocks",
    "selenium",
    "pycryptodome",
    "python-telegram-bot",
    "pyTelegramBotAPI",
    "instaloader",
    "instagrapi",
    "generate-user-agent",
    "mechanize",
    "pystyle",
    "fade",
    "cfonts"
]

def install(package):
    try:
        __import__(package.replace("-", "_"))
        print(f"[✓] {package} already installed")
    except ImportError:
        print(f"[+] Installing {package} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("="*60)
print("     OBITO ULTRA SMART INSTALLER")
print("="*60)

# Upgrade core tools first
subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

for pkg in packages:
    install(pkg)

print("\nAll required packages installed successfully ✅")
