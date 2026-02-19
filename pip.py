import os
import sys
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

ALL_PACKAGES = [
    "requests", "selenium", "beautifulsoup4", "bs4", "mechanize", "pysocks",
    "curl2pyreqs", "user_agent", "fake_useragent", "generate_user_agent", "urllib3",
    "pytelegrambotapi", "python-telegram-bot", "telegram", "telebot", "instaloader",
    "instagrapi", "instagram-private-api", "colorama", "rich", "pyfiglet", "cfonts",
    "python-cfonts", "pystyle", "fade", "termcolor", "colored", "pycryptodome",
    "youtube-dl", "pafy", "uuid", "secrets", "argparse", "twython", "tweepy",
    "facebook-sdk", "discord.py", "scrapy", "lxml", "html5lib", "pyquery",
    "selenium-wire", "undetected-chromedriver", "numpy", "pandas", "matplotlib",
    "pillow", "opencv-python", "cryptography", "bcrypt", "passlib", "jwt",
    "oauthlib", "tqdm", "progress", "pyperclip", "pyautogui", "keyboard", "mouse",
    "pygetwindow", "pytest", "unittest2", "debugpy", "pymongo", "mysql-connector-python",
    "redis", "asyncio", "aiohttp", "multiprocessing", "pydub", "playsound", "pygame",
    "moviepy", "google-api-python-client", "spotipy", "giphy-client", "imgurpython",
    "psutil", "glob2", "pathlib", "zipfile36", "pypiwin32", "sympy", "scipy"
]

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'

def printc(text, color=RESET):
    print(f"{color}{text}{RESET}")

def install_package(package):
    """Package install karo - error aaye toh ignore"""
    try:
        # Package name normalize
        pip_name = package
        if package == "discord.py":
            pip_name = "discord.py"
        elif package == "glob2":
            pip_name = "glob2"
        elif package == "zipfile36":
            pip_name = "zipfile36"
            
        # Try install
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet", pip_name],
            capture_output=True,
            text=True,
            timeout=30
        )
        return package, True if result.returncode == 0 else False
    except:
        return package, False  # Error ignore karo

def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Banner
    printc("="*60, CYAN)
    printc("#           MEGA PIP INSTALLER v2.0           #", YELLOW)
    printc("#           All Modules Included              #", GREEN)
    printc("#           @Aotpy                           #", BLUE)
    printc("="*60, CYAN)
    
    printc(f"\n📊 Total Packages: {len(ALL_PACKAGES)}", YELLOW)
    printc("⏳ Starting installation...\n", CYAN)
    
    # Pehle pip upgrade
    printc("📦 Upgrading pip...", CYAN)
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "--quiet"], 
                   capture_output=True)
    
    # Built-in modules (check nahi karenge, seedha install karenge)
    builtin = ['os', 'sys', 'time', 'datetime', 'random', 'string', 
               'json', 're', 'math', 'hashlib', 'threading', 'argparse',
               'logging', 'platform', 'shutil', 'subprocess', 'concurrent',
               'multiprocessing', 'asyncio', 'pathlib', 'pickle']
    
    # Filter karo sirf external packages
    to_install = [p for p in ALL_PACKAGES if p not in builtin]
    
    printc(f"📦 Installing {len(to_install)} packages...\n", GREEN)
    
    installed = []
    failed = []
    
    # Threads ke saath fast installation
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(install_package, pkg): pkg for pkg in to_install}
        
        for i, future in enumerate(as_completed(futures), 1):
            package, success = future.result()
            
            if success:
                installed.append(package)
                printc(f"✅ [{i}/{len(to_install)}] {package}", GREEN)
            else:
                failed.append(package)
                printc(f"⚠️  [{i}/{len(to_install)}] {package} - Skipped", YELLOW)
            
            # Thoda delay for smooth output
            time.sleep(0.1)
    
    # Final Report
    printc("\n" + "="*60, CYAN)
    printc("🎉 INSTALLATION COMPLETE!", YELLOW)
    printc("="*60, CYAN)
    
    printc(f"\n📊 FINAL STATISTICS:", BLUE)
    printc(f"   ✅ Successfully installed: {len(installed)}", GREEN)
    printc(f"   ⚠️  Failed/Skipped: {len(failed)}", YELLOW)
    printc(f"   📦 Total processed: {len(to_install)}", CYAN)
    
    # Log save
    with open('install_log.txt', 'w') as f:
        f.write(f"Installed ({len(installed)}): {', '.join(installed[:20])}\n")
        if len(installed) > 20:
            f.write(f"... and {len(installed)-20} more\n")
        f.write(f"\nFailed/Skipped ({len(failed)}): {', '.join(failed[:20])}\n")
    
    printc("\n📝 Log saved to install_log.txt", GREEN)
    
    # Final message
    printc("\n" + "="*60, CYAN)
    printc("🔗 Press Enter to open - t.me/Aotpy", GREEN)
    printc("="*60, CYAN)
    
    # Enter press karne ka option
    input()
    
    # Try to open telegram link
    try:
        if os.name == 'nt':  # Windows
            os.system(f"start https://t.me/Aotpy")
        else:  # Linux/Mac
            os.system(f"xdg-open https://t.me/Aotpy")
    except:
        pass  # Agar link na khule toh ignore

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        printc("\n\n⚠️  Installation interrupted by user!", RED)
        sys.exit(1)
    except Exception as e:
        # Koi bhi error aaye toh ignore karo aur continue karo
        printc(f"\n⚠️  Minor error: {e}", YELLOW)
        printc("Continuing anyway...", GREEN)
        main()
