import os
import sys
import subprocess
import pkg_resources
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
    "youtube-dl",
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
    "glob2",
    "pathlib",
    "zipfile36",
    "pypiwin32",
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

def is_package_installed(package_name):
    """Check if package is installed using pkg_resources (more reliable)"""
    try:
        pkg_resources.get_distribution(package_name)
        return True
    except:
        return False

def install_package(package):
    """Install single package with better error handling"""
    try:
        # Handle special package names
        pip_package = package
        if package == "discord.py":
            pip_package = "discord.py"
        elif package == "glob2":
            pip_package = "glob2"
        elif package == "zipfile36":
            pip_package = "zipfile36"
            
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", pip_package],
            capture_output=True,
            text=True,
            timeout=60
        )
        return package, result.returncode == 0, result.stdout
    except subprocess.TimeoutExpired:
        return package, False, "Timeout"
    except Exception as e:
        return package, False, str(e)

def upgrade_pip():
    """Upgrade pip and setuptools"""
    print_color("📦 Upgrading pip and setuptools...", 'cyan')
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"],
        capture_output=True
    )

def main():
    """Main installation function"""
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Banner
    print_color("="*60, 'cyan')
    print_color("#           MEGA PIP INSTALLER v2.0           #", 'yellow')
    print_color("#           All Modules Included              #", 'green')
    print_color("#           @Aotpy                           #", 'purple')
    print_color("="*60, 'cyan')
    
    print_color(f"\n📊 Total Packages: {len(ALL_PACKAGES)}", 'white')
    print_color("⏳ Starting installation...\n", 'cyan')
    
    # Upgrade pip first
    upgrade_pip()
    
    # Separate built-in modules (these don't need installation)
    builtin_modules = ['os', 'sys', 'time', 'datetime', 'random', 'string', 
                       'json', 're', 'math', 'hashlib', 'threading', 'argparse',
                       'logging', 'platform', 'shutil', 'subprocess', 'concurrent',
                       'multiprocessing', 'asyncio', 'pathlib', 'pickle']
    
    # Filter packages to install
    to_install = []
    skipped = []
    
    print_color("\n🔍 Checking installed packages...", 'cyan')
    
    for package in ALL_PACKAGES:
        if package in builtin_modules:
            skipped.append(package)
            continue
            
        # Handle special package names for checking
        check_name = package
        if package == "discord.py":
            check_name = "discord"
        elif package == "glob2":
            check_name = "glob2"
        elif package == "zipfile36":
            check_name = "zipfile36"
            
        if is_package_installed(check_name):
            skipped.append(package)
        else:
            to_install.append(package)
    
    print_color(f"\n📦 Packages to install: {len(to_install)}", 'yellow')
    print_color(f"✅ Already installed/skipped: {len(skipped)}", 'green')
    
    if len(to_install) == 0:
        print_color("\n✨ All packages are already installed!", 'green')
    else:
        print_color(f"\n⚡ Installing {len(to_install)} packages...", 'green')
        
        installed = []
        failed = []
        
        # Install with threads for speed
        with ThreadPoolExecutor(max_workers=3) as executor:
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
    
    # Final Report
    print_color("\n" + "="*60, 'cyan')
    print_color("🎉 INSTALLATION COMPLETE!", 'yellow')
    print_color("="*60, 'cyan')
    
    print_color(f"\n📊 FINAL STATISTICS:", 'purple')
    print_color(f"   ✅ Total packages processed: {len(ALL_PACKAGES)}", 'cyan')
    
    if 'installed' in locals():
        print_color(f"   ✅ Newly installed: {len(installed)}", 'green')
    print_color(f"   ⏭️  Already installed/skipped: {len(skipped)}", 'yellow')
    
    if 'failed' in locals() and failed:
        print_color(f"   ❌ Failed: {len(failed)}", 'red')
        print_color(f"\n⚠️  Failed packages ({len(failed)}):", 'red')
        for f in failed[:10]:
            print_color(f"   • {f}", 'red')
        if len(failed) > 10:
            print_color(f"   ... and {len(failed)-10} more", 'red')
    
    print_color("\n" + "="*60, 'cyan')
    print_color("🔗 Join @Aotpy for more tools!", 'green')
    print_color("="*60, 'cyan')
    
    # Save log
    with open('install_log.txt', 'w') as f:
        f.write(f"Total packages: {len(ALL_PACKAGES)}\n")
        if 'installed' in locals():
            f.write(f"Newly installed: {', '.join(installed)}\n")
        if 'failed' in locals() and failed:
            f.write(f"Failed: {', '.join(failed)}\n")
        f.write(f"Skipped: {', '.join(skipped)}\n")
    
    print_color("\n📝 Log saved to install_log.txt", 'white')
    
    # Press Enter to continue
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
