import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5702183929:AAH2_oIzX98z-DWMl_zrCf2MX8jstzL01_I")
    
    API_ID = int(os.environ.get("API_ID", 18791409))
    
    API_HASH = os.environ.get("API_HASH", "389c73d03dc1e98d973a125065d67b3d")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5163444566"))

    SESSION_NAME = "AnicadeUploaderBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://kacbusiness:hrituzee123@kacbusiness.dahr62x.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
