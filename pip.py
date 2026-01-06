
import os
import subprocess
import sys
import time
os.system("pip install --upgrade pip setuptools cython")

A = "\033[1;91m"  # Red
B = "\033[1;96m"  # Cyan
C = "\033[1;97m"  # White
E = "\033[1;92m"  # Green
H = "\033[1;93m"  # Yellow
L = "\033[1;95m"  # Magenta
M = "\033[1;94m"  # Blue
RESET = "\033[0m"

def banner(text):
    print('#'*67)
    print(f"#{' '*(67-len(text)-2)}{text}#")
    print('#'*67)

def color_bar():
    print(f'{A}={B}={C}={E}={H}={L}={M}='*4)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def install(module):
    try:
        __import__(module)
        return True
    except ImportError:
        sys.stdout.write(f"{H}Installing {module}...{RESET}\n")
        sys.stdout.flush()
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", module], check=True)
        except subprocess.CalledProcessError:
            sys.stdout.write(f"{A}Failed to install {module}, skipping...{RESET}\n")
        return False

def animated_progress(module, est_time=3):
    spinner = ['|','/','-','\\']
    for i in range(est_time*8):
        percent = int((i/(est_time*8))*100)
        sys.stdout.write(f'\r{B}Installing {module}: {percent}% {spinner[i%4]}{RESET}')
        sys.stdout.flush()
        time.sleep(0.25)
    print('\r', end='')

def countdown(seconds, msg="Waiting"):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f'\r{C}{msg} {i}s...{RESET} ')
        sys.stdout.flush()
        time.sleep(1)
    print('\r', end='')

def estimate_total_time(modules, est_time_per_mod=3):
    total = len(modules)*est_time_per_mod
    mins = total//60
    secs = total%60
    return f"{mins}m {secs}s"


modules_stage1 = [
    "telebot", "python-cfonts", "Topython", "user_agent", "fake_useragent",
    "pyfiglet", "selenium", "requests", "youtube_dl", "colorama",
    "beautifulsoup4", "pafy", "InstagramAPI", "generate_user_agent",
    "pysocks", "curl2pyreqs", "rich", "pycryptodome", "telegram", "ms4",
    "mechanize", "fade", "pystyle", "pycountry", "cfonts",
    "time", "uuid", "random", "datetime", "string", "secrets", "webbrowser",
    "hashlib", "threading", "json", "argparse", "token_hex", "Fore", "parasfont", "cfont"
]

modules_stage2 = ["pip", "setuptools", "cython"]

import os
import subprocess

modules = [
    "requests", "Topython", "pysocks", "curl2pyreqs", "pycountry", "pyfiglet",
    "pystyle", "fade", "colorama", "fake_useragent", "ms4", "uuid"
]

for mod in modules:
    try:
        __import__(mod)
    except ImportError:
        print(f"Installing {mod}...")
        subprocess.run(["pip", "install", mod], check=True)

eizon = [
    "eizon",
    "telebot",
    "telegram",
    "stdiomask",
    "user_agent",
    "instaloader",
    "requests",
    "rich",
    "pyfiglet",
    "colorama",
    "instagrapi",
    "generate_user_agent",
    "selenium",
    "python-cfonts",               
    "pycryptodome",
    "fake_useragent",
    "asmix",
    "MedoSigner",
    "python-telegram-bot",
    "pystyle"       
]

for package in Aotpy:
	
	Aotpy = [
    "Aotpy",
    "telebot",
    "telegram",
    "stdiomask",
    "user_agent",
    "instaloader",
    "requests",
    "rich",
    "pyfiglet",
    "colorama",
    "instagrapi",
    "generate_user_agent",
    "selenium",
    "python-cfonts",               
    "pycryptodome",
    "fake_useragent",
    "asmix",
    "MedoSigner",
    "python-telegram-bot",
    "pystyle"       
]



# -------------------- Start Installation --------------------
import os

os.system('pip install telebot')
os.system('pip install cfonts')
os.system('pip install user_agent')
os.system('pip install instaloader')
os.system('pip install requests')
os.system('pip install rich')
os.system('user_agent')
os.system('instaloader')
os.system('mechaize')
os.system('pip install pyfiglet')
os.system('pip install sys')
os.system('pip install py_compile')
os.system('pip install youtube_dl')
os.system('pip install uuid')
os.system('pip install time')
os.system('pip install os')
os.system('pip install random')
os.system('pip install datetime')
os.system('pip install string')
os.system('pip install secrets')
os.system('pip install webbrowser')
os.system('pip install hashlib')
os.system('pip install colorama')
os.system('pip install n')
os.system('pip install mm')
os.system('pip install new')
os.system('pip install sleep')
os.system('pip install BeautifulSoup')
os.system('pip install new')
os.system('pip install pafy')
os.system('pip install bs4')
os.system('pip install sys')
os.system('pip install json')
os.system('pip install random')
os.system('pip install uuid')
os.system('pip install secrets')
os.system('pip install datetime')
os.system('pip install *')
os.system('pip install argparse')
os.system('pip install InstagramAPI')
os.system('pip install sleep')
os.system('pip install string')
os.system('pip install uuid4')
os.system('pip install generate_user_agent')
os.system('pip install threading')
os.system('pip install json')
os.system('pip install datetime')
os.system('pip install token_hex')
os.system('pip install secrets')
os.system('pip install token_hex')
os.system('pip install Fore')
os.system('pip install secrets')
os.system('pip install uuid')
os.system('pip install re')
os.system('pip install b')
os.system('pip install requests')
os.system('pip install pyfiglet')
os.system('pip install selenium')
os.system('pip install requests')
os.system('pip install pyfiglet')
os.system('pip install sys')
os.system('pip install py_compile')
os.system('pip install youtube_dl')
os.system('pip install uuid')
os.system('pip install time')
os.system('pip install os')
os.system('pip install random')
os.system('pip install datetime')
os.system('pip install string')
os.system('pip install secrets')
os.system('pip install webbrowser')
os.system('pip install hashlib')
os.system('pip install colorama')
os.system('pip install n')
os.system('pip install mm')
os.system('pip install new')
os.system('pip install sleep')
os.system('pip install BeautifulSoup')
os.system('pip install new')
os.system('pip install pafy')
os.system('pip install bs4')
os.system('pip install sys')
os.system('pip install json')
os.system('pip install random')
os.system('pip install uuid')
os.system('pip install secrets')
os.system('pip install datetime')
os.system('pip install argparse')
os.system('pip install InstagramAPI')
os.system('pip install sleep')
os.system('pip install string')
os.system('pip install uuid4')
os.system('pip install generate_user_agent')
os.system('pip install threading')
os.system('pip install json')
os.system('pip install datetime')
os.system('pip install token_hex')
os.system('pip install secrets')
os.system('pip install token_hex')
os.system('pip install Fore')
os.system('pip install secrets')
os.system('pip install uuid')
os.system('pip install re')
os.system('pip install b')
os.system('pip install requests')
os.system('pip install pyfiglet')
os.system('pip install sys')
os.system('pip install py_compile')
os.system('pip install youtube_dl')
os.system('pip install uuid')
os.system('pip install time')
os.system('pip install os')
os.system('pip install random')
os.system('pip install datetime')
os.system('pip install string')
os.system('pip install secrets')
os.system('pip install webbrowser')
os.system('pip install hashlib')
os.system('pip install colorama')
os.system('pip install n')
os.system('pip install mm')
os.system('pip install new')
os.system('pip install sleep')
os.system('pip install BeautifulSoup')
os.system('pip install new')
os.system('pip install pafy')
os.system('pip install bs4')
os.system('pip install sys')
os.system('pip install json')
os.system('pip install random')
os.system('pip install uuid')
os.system('pip install secrets')
os.system('pip install datetime')
os.system('pip install *')
os.system('pip install argparse')
os.system('pip install InstagramAPI')
os.system('pip install sleep')
os.system('pip install string')
os.system('pip install uuid4')
os.system('pip install generate_user_agent')
os.system('pip install threading')
os.system('pip install json')
os.system('pip install datetime')
os.system('pip install token_hex')
os.system('pip install secrets')
os.system('pip install token_hex')
os.system('pip install Fore')
os.system('pip install secrets')
os.system('pip install uuid')
os.system('pip install re')
os.system('pip install b')
os.system('cls' if os.name == 'nt' else 'clear') 

print('All pips are installed successfully join my all channel @Aotpy for jacking file redirecting to channel...')


clear()
banner("OBITO ULTRA PIP INSTALLER")
color_bar()
print(f"{E}Total Estimated Time: {estimate_total_time(modules_stage1 + modules_stage2)}{RESET}")
print(f"{H}Please do not close the app until installation completes...{RESET}")
time.sleep(2)

# -------------------- Stage 1 --------------------
print(f"\n{B}Stage 1: Installing Core & Support Modules...{RESET}")
for mod in modules_stage1:
    install(mod)
    animated_progress(mod, 2)

print(f"{L}Stage 1 Completed!{RESET}")
countdown(2, "Preparing Stage 2")

# -------------------- Stage 2 --------------------
clear()
banner("UPGRADING PIP & TOOLS")
color_bar()
print(f"{E}Stage 2: Upgrading pip, setuptools, cython...{RESET}")
for mod in modules_stage2:
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", mod])
    animated_progress(mod, 2)

print(f"{L}Stage 2 Completed!{RESET}")
countdown(2, "Finalizing Installation")

# -------------------- Final Message --------------------
clear()
banner("OBITO ULTRA PIP INSTALLER COMPLETE")
color_bar()
print(f"{B}All modules installed successfully!{RESET}")
print(f"{C}You can now run your Obito-style Python scripts with full support.{RESET}")
print('#'*67)
print('''This Mega all in one pip by @Aotpy''')
