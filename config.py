# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "7217645"))
API_HASH = getenv("API_HASH", "78ba6352dd5cdc166fdef5aa84ba7c67")
BOT_TOKEN = getenv("BOT_TOKEN", "2100096282:AAEls5EFlORYva-cCFiXQ_xQZW2wbXIR2Wo")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DUSHMANXRONIN")
BOT_USERNAME = getenv("FantasticFighterbot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Ronin_Fighters_fd")
BOT_NAME = getenv("BOT_NAME","Fantastic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("SESSION_NAME", "BQA3m-8BYKvOPnAsbtUrk2w6mv0rIY5Nnm2e5Y8HdqT6C3Gl_-Gw2eGi0PdJJ-ZEMiviwcq_i19qje5YGvjge1JIlAzG4m8yiUkOy6q19btC87QA38pn9ENjJVsp3S_fcz8wBJWWb2ju-ZRNyoqsBkaArkf5yvK9_81pOJ5_p1Jqo8JJAW03pDV8XMQm0sWdSnhqXfxcvouXcbNlBUJKUC89nFEJuf8m59Vfk4827f6ByrTUaway0MaotzVuW5TOCro_N653Z2B9RCGYxzDx9N-VucOJu_20pu1wy9qRbffgz9I6P4-cgnL9fi54C2o8q7tGLyvMFBI9AZbbJ3DnXJADAAAAAUK509kA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
