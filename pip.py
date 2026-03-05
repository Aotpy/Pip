import os
import sys
import subprocess

Y = "\033[0;33m"
G = "\033[0;32m"
W = "\033[0m"

ADMIN = "t.me/Aotpy"
CHANNEL = "t.me/ObitoStuffs"

packages = [
"parascode", "aotpkg",
"requests", "mechanize", "httpx", "aiohttp", "curl_cffi", 
"urllib3", "http3", "hyper", "tls_client", "httpx-socks",
"beautifulsoup4", "bs4", "lxml", "html5lib", "parsel", 
"selectolax", "cloudscraper", "cfscrape", "scrapy", 
"selenium", "webdriver-manager", "playwright", "pyppeteer",
"requests-html", "requests-toolbelt", "socksipy-branch", "pysocks",
"telethon", "pyrogram", "tgCrypto", "telegram", "python-telegram-bot",
"discord.py", "discord-webhook", "tweepy", "instaloader", 
"facebook-scraper", "youtube-dl", "yt-dlp", "pytube",
"reddit", "praw", "twitchAPI", "spotipy",
"colorama", "rich", "pyfiglet", "termcolor", "art", 
"emoji", "tabulate", "prettytable", "progress", "tqdm",
"halo", "yaspin", "alive-progress", "python-cfonts",
"cryptography", "pycryptodome", "bcrypt", "passlib", 
"pyjwt", "python-jose", "ecdsa", "rsa", "fernet",
"pyOpenSSL", "cffi", "nacl", "pynacl", "m2crypto",
"numpy", "pandas", "matplotlib", "pillow", "opencv-python",
"pydub", "moviepy", "imageio", "wand", "qrcode",
"pymongo", "mysql-connector-python", "psycopg2-binary", "sqlalchemy", "redis",
"dnspython", "paramiko", "scp", "netmiko", "napalm",
"flask", "fastapi", "django", "aiofiles", "uvicorn",
"jinja2", "werkzeug", "asyncio", "python-dotenv", "pyyaml",
"faker", "names", "user_agent", "fake-useragent", "uuid",
"validators", "email-validator", "phonenumbers", "pycountry", "geopy",
"psutil", "platform", "distro", "cpuinfo", "gputil",
"schedule", "apscheduler", "celery", "redis", "rabbitmq",
"loguru", "winsound", "playsound", "pygame", "wave",
"pyautogui", "pynput", "keyboard", "mouse", "pygetwindow",
"pyperclip", "pywhatkit", "qrcode", "pyzbar", "opencv-python",
"whois", "python-whois", "shodan", "censys", "zoomeye",
"scapy", "pcap", "dpkt", "pyshark", "netifaces",
"smtplib", "imapclient", "yagmail", "premailer", "flask-mail",
"twilio", "vonage", "plivo", "africastalking", "clickatell",
"websockets", "python-socketio", "flask-socketio", "socketio-client", "engineio",
"pyserial", "python-rtmidi", "mido", "pyusb", "hid",
"pytest", "unittest2", "mock", "coverage", "pytest-cov",
"attrs", "trio", "httpcore"
]

print(f"{Y}Upgrading pip...{W}")
os.system(f"{sys.executable} -m pip install --upgrade pip -q")

total = len(packages)
for i, pkg in enumerate(packages, 1):
    print(f"{Y}[{i}/{total}] Installing {pkg}...{W}")
    
    try:
        __import__(pkg.replace("-", "_"))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)

os.system('cls' if os.name == 'nt' else 'clear')

print(f"{G}✓ Installation Complete!{W}")
print(f"{G}Admin: {ADMIN}{W}")
print(f"{G}Channel: {CHANNEL}{W}")
