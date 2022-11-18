import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "15939361"))
    API_HASH = os.environ.get("API_HASH", "f8beb0bd0054a717d84fbe9be12a23ea")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5984638204:AAG2oTXKedFkRfnR1MftvOIsKUrMhpXVits") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "5543917190")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://anurag:xC6QOmRI7j9i8yj6@anurag.co63n.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Anurag")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'AForward_data')
    SESSION = os.environ.get("SESSION", "BQDAeWLYkw-sE04Te_kiUhwK678o5xeb5wpTzW3kqjX15pGgcubrEPR3l3MZNvtONLMMpMzvu2bdjFTCrJeCaI6JuPGkwwn-j5JtEPJjEw-stEhBGJhcNqwnHv-t4GxnUN5KvZpwyYvSmC3Zs-5AVgJCcqylzamwNF_ugByM-mgdz2woIrTxYzrd8dDUhGqfGkBLsJyuo-9YDSlL8IUq7z55YcEEulF2QtsGrAeFezlcBtc3EIuI9Bs-iQM6nkrn1FUHUa9hzV8Ddc6_8RT1JT2RMyAaSWAw5DSjIAYUXSEplNSY8NdKTg3Nqyw2JNB0vMDYVCJETEQOPIEi1FN4SPRLOg1h6AA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001787652537"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "forwardro_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
