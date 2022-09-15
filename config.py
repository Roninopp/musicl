# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "7217645"))
API_HASH = getenv("API_HASH", "78ba6352dd5cdc166fdef5aa84ba7c67")
BOT_TOKEN = getenv("BOT_TOKEN", "2100096282:AAHFgMRR_kkW_Mj05OyunSrjMrnhIk3VnEc")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DUSHMANXRONIN")
BOT_USERNAME = getenv("FantasticFighterbot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Ronin_Fighters_fd")
BOT_NAME = getenv("BOT_NAME","Fantastic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("SESSION_NAME", "BQCF6yCjri750hPj2Bhz9HxKKbpyisEgbRZ8twLRLxrE4Rvra7m1H-b5QinWN41ZnHm01fDXASJODPbT1zpamD96cajaOR-oH0edQv9SpJ9LeF8LCkoBj6ldB5EnEWf-cHG94y4xJNmOkm4tWQW82gUXadJ6ea5Fdds2FQhLiqON39RyVKoG1ATlXEs1Ci5YyICyWdb35LiLprzvB89RAiK_epIu9vSlURQWAyRaSJRw4eBL1IL3i4J0hkY0PvhofzkkSGHKKPmBBlp_g2PfA_4wXjrDBekBlBOkeVB4B2SoqjV75Pf42kWbz7MgI2hskdg70knYUVg71oQkip2EZrKuAAAAAS3VP2UA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
