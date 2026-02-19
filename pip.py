import os
import sys
import subprocess
import importlib.util
from concurrent.futures import ThreadPoolExecutor, as_completed

ALL_PACKAGES = [
    "requests",
    "selenium",
    "beautifulsoup4",
    "bs4",
    "mechanize",
    "pysocks",
    "curl2pyreqs",
    "user_agent",
    "fake_useragent",
    "generate_user_agent",
    "urllib3",
    "pytelegrambotapi",
    "python-telegram-bot",
    "telegram",
    "telebot",
    "instaloader",
    "instagrapi",
    "instagram-private-api",
    "colorama",
    "rich",
    "pyfiglet",
    "cfonts",
    "python-cfonts",
    "pystyle",
    "fade",
    "termcolor",
    "colored",
    "pycryptodome",
    "youtube_dl",
    "pafy",
    "uuid",
    "secrets",
    "argparse",
    "twython",
    "tweepy",
    "facebook-sdk",
    "discord.py",
    "scrapy",
    "lxml",
    "html5lib",
    "pyquery",
    "selenium-wire",
    "undetected-chromedriver",
    "numpy",
    "pandas",
    "matplotlib",
    "pillow",
    "opencv-python",
    "cryptography",
    "bcrypt",
    "passlib",
    "jwt",
    "oauthlib",
    "tqdm",
    "progress",
    "pyperclip",
    "pyautogui",
    "keyboard",
    "mouse",
    "pygetwindow",
    "pytest",
    "unittest2",
    "logging",
    "debugpy",
    "pymongo",
    "mysql-connector-python",
    "sqlite3",
    "redis",
    "asyncio",
    "aiohttp",
    "multiprocessing",
    "concurrent",
    "pydub",
    "playsound",
    "pygame",
    "moviepy",
    "google-api-python-client",
    "spotipy",
    "giphy-client",
    "imgurpython",
    "psutil",
    "platform",
    "shutil",
    "glob",
    "subprocess",
    "pathlib",
    "zipfile",
    "tarfile",
    "pickle",
    "math",
    "statistics",
    "sympy",
    "scipy",
]

COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m'
}

def print_color(text, color='white'):
    print(f"{COLORS.get(color, COLORS['white'])}{text}{COLORS['reset']}")

def check_package(package):
    return importlib.util.find_spec(package) is not None

def install_package(package):
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet", package],
            capture_output=True,
            text=True,
            timeout=30
        )
        return package, result.returncode == 0, result.stdout
    except:
        return package, False, "Timeout/Error"

def upgrade_pip():
    print_color("📦 Upgrading pip...", 'cyan')
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
        capture_output=True
    )

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_color("="*60, 'cyan')
    print_color("#           MEGA PIP INSTALLER v2.0           #", 'yellow')
    print_color("#           All Modules Included              #", 'green')
    print_color("#           @Aotpy                           #", 'purple')
    print_color("="*60, 'cyan')
    
    print_color(f"\n📊 Total Packages: {len(ALL_PACKAGES)}", 'white')
    print_color("⏳ Starting installation...\n", 'cyan')
    
    upgrade_pip()
    
    builtin = ['os', 'sys', 'time', 'datetime', 'random', 'string', 
               'json', 're', 'math', 'hashlib', 'threading', 'argparse']
    
    to_install = [p for p in ALL_PACKAGES if p not in builtin]
    
    print_color(f"📦 External packages to install: {len(to_install)}", 'yellow')
    print_color(f"✅ Built-in modules: {len(builtin)}", 'green')
    
    installed = []
    failed = []
    skipped = []
    
    print_color("\n🔍 Checking installed packages...", 'cyan')
    for package in to_install:
        if check_package(package.replace('-', '_')):
            skipped.append(package)
    
    to_install = [p for p in to_install if p not in skipped]
    
    print_color(f"\n⚡ Installing {len(to_install)} packages...", 'green')
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(install_package, pkg): pkg for pkg in to_install}
        
        for i, future in enumerate(as_completed(futures), 1):
            package, success, _ = future.result()
            
            if success:
                installed.append(package)
                status = f"✅ [{i}/{len(to_install)}] {package}"
                print_color(status, 'green')
            else:
                failed.append(package)
                status = f"❌ [{i}/{len(to_install)}] {package}"
                print_color(status, 'red')
    
    print_color("\n" + "="*60, 'cyan')
    print_color("🎉 INSTALLATION COMPLETE!", 'yellow')
    print_color("="*60, 'cyan')
    
    print_color(f"\n📊 FINAL STATISTICS:", 'purple')
    print_color(f"   ✅ Successfully installed: {len(installed)}", 'green')
    print_color(f"   ⏭️  Already installed: {len(skipped)}", 'yellow')
    print_color(f"   ❌ Failed: {len(failed)}", 'red')
    print_color(f"   📦 Total modules: {len(ALL_PACKAGES)}", 'cyan')
    
    if failed:
        print_color(f"\n⚠️  Failed packages ({len(failed)}):", 'red')
        for f in failed[:10]:
            print_color(f"   • {f}", 'red')
        if len(failed) > 10:
            print_color(f"   ... and {len(failed)-10} more", 'red')
    
    print_color("\n" + "="*60, 'cyan')
    print_color("🔗 Join @Aotpy for more tools!", 'green')
    print_color("="*60, 'cyan')
    
    with open('install_log.txt', 'w') as f:
        f.write(f"Installed: {', '.join(installed)}\n")
        f.write(f"Failed: {', '.join(failed)}\n")
        f.write(f"Skipped: {', '.join(skipped)}\n")
    
    print_color("\n📝 Log saved to install_log.txt", 'white')
    input("\nPress Enter to open owner's contact - t.me/Aotpy")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_color("\n\n⚠️  Installation interrupted by user!", 'red')
        sys.exit(1)
    except Exception as e:
        print_color(f"\n❌ Error: {e}", 'red')
        sys.exit(1)
