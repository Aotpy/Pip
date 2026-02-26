import os,sys
Y = "\033[0;33m"
G = "\033[0;32m"
W = "\033[0m"

ADMIN = "t.me/Aotpy"
CHANNEL = "t.me/ObitoStuffs"

packages = [
"requests", "mechanize", "names", "user_agent", "telethon", "python-cfonts",
"pyfiglet", "colorama", "rich", "uuid", "bs4", "pysocks", "pycryptodome",
"selenium", "instaloader", "httpx", "brotli", "fake_useragent", "youtube_dl",
"yt-dlp", "pytube", "tweepy", "discord.py", "instagram-private-api", "aiohttp",
"scrapy", "lxml", "cloudscraper", "curl_cffi", "tls_client", "cfscrape",
"pyautogui", "pynput", "keyboard", "mouse", "schedule", "python-telegram-bot",
"aiogram", "pywhatkit", "pywinauto", "numpy", "pandas", "matplotlib", "seaborn",
"scipy", "scikit-learn", "tensorflow", "torch", "keras", "opencv-python",
"pillow", "imageio", "moviepy", "pydub", "cryptography", "bcrypt", "passlib",
"pymongo", "mysql-connector-python", "psycopg2", "sqlalchemy", "redis", "tqdm",
"loguru", "click", "argparse", "python-dotenv", "pyyaml", "jsonschema", "faker",
"random-password", "zstandard", "lz4", "pypdf2", "reportlab", "openpyxl",
"python-docx", "asyncio", "aiofiles", "uvicorn", "pytest", "coverage", "psutil",
"watchdog", "pendulum", "arrow", "python-dateutil", "pytz", "yagmail", "flask",
"django", "fastapi", "bottle", "tornado", "emoji", "art", "termcolor",
"ascii-magic", "prettytable", "tabulate", "progress", "halo", "spinner",
"yaspin", "paramiko", "scapy", "netifaces", "dnspython", "shodan", "whois",
"python-whois", "ipaddress", "validators", "email-validator", "phonenumbers",
"pycountry", "geopy", "folium", "gmaps", "googlemaps", "twilio", "vonage",
"plivo", "nexmo", "africastalking", "clickatell", "infobip", "msg91",
"textlocal", "bulksms", "smtplib", "imapclient", "secure-smtplib", "premailer",
"jinja2", "mako", "gunicorn", "werkzeug", "markupsafe", "itsdangerous",
"blinker", "flask-sqlalchemy", "flask-login", "flask-mail", "flask-wtf",
"flask-restful", "flask-cors", "flask-socketio", "django-rest-framework",
"django-cors-headers", "django-allauth", "celery", "rabbitmq", "kafka-python",
"pika", "stomp.py", "websockets", "socket.io-client", "engineio",
"python-socketio", "requests-html", "requests-toolbelt", "requests-oauthlib",
"oauthlib", "authlib", "pyjwt", "python-jose", "ecdsa", "mnemonic", "bip32utils",
"bip39", "eth-account", "web3", "solana", "near-api-py", "ton", "tronapi",
"waves", "stellar-sdk", "xrpl-py", "cardano", "ada", "polkadot",
"substrate-interface", "pytezos", "cosmospy", "terra-sdk", "avalanche",
"harmony", "elrond", "algorand", "near", "flow", "aptos", "sui", "axelar",
"osmosis", "juno", "evmos", "cronos", "fantom", "polygon", "arbitrum",
"optimism", "base", "zksync", "starknet", "immutablex", "loopring", "zksync2",
"starknet-py", "eth-brownie", "ape", "hardhat", "truffle", "ganache"
]
print(f"{Y}Upgrading pip...{W}")
os.system(f"{sys.executable} -m pip install --upgrade pip -q")

total = len(packages)
for i, pkg in enumerate(packages, 1):
    print(f"{Y}[{i}/{total}] Installing {pkg}...{W}")
    os.system(f"{sys.executable} -m pip install {pkg} -q")

os.system('cls' if os.name == 'nt' else 'clear')

print(f"{G}✓ Installation Complete!{W}")
print(f"{G}Admin: {ADMIN}{W}")
print(f"{G}Channel: {CHANNEL}{W}")
