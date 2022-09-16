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
SESSION_NAME = getenv("SESSION_NAME", "BQBuIe0ARDx4m7BnicOZGmPVPhjscgAzgNnGc0BpHb95NZKxy7o0hPNTXO1oyzadU3Q9QhgEzNf8Rve7IQeOrZrZbmJOySbtqAY4XctSBotxs7LBOjVZfQ8iLeQ-VAfbNemoBgCGoPk9sBVNNPhwciTcVyAerb0-5XZ41_Hjp-RN_hzBf2bqOezud8bB6di7tOjwteaYF6ksanS1HYrMN4koqD0VPS4moc9V8G4-pCEr2KjhZMZnlOfGGddeTBTHRev_NPWt_kMTYxkjp6Xkg4ddZ1Riq1Ln9OKn8rbrdtGA4VBUusUWh3g8IOP5MkIIRwMnWVzz6zJSPJ-2wfjnPkpMN1BdKwAAAAEt1T9lAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
