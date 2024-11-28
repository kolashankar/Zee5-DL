import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7533694883:AAHFXlu5s_PZ_pJbL7jpVFxXDcu0WHoZu9U")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 24271861))
    API_HASH = os.environ.get("API_HASH", "fc5e782b934ed58b28780f41f01ed024")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1636733122").split())

    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://kolashankar423:Wtd7zv86jhdrsE0g@cluster0.uyj6b.mongodb.net/?retryWrites=true&w=majority")
    
