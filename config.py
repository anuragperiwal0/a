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
    SESSION = os.environ.get("SESSION", "BQA53JaqcpUg6XtUDZqOAjPSEjOZAz_ZvUZAjTegfxWKazMSBWU0pp5RvzGlXf-6HCTO4Cv-NMh13lDYCxdO7iztArA3QHJ84xBpMD5_WiaVGFm5Okea7OabP9BAOs6aJ6dgw9wwwkvSl2zzECH8cCRxiehGO6-AzvCQ995Xd511hbnTby3zejhl3BlxDe06-I6zG6RfcbjRtooyCt-keRNpn4vUTpCg8ASKAqn-VjnksyzPmRlqmoJUbxYdU0zj8MSN3CNJ5IVUDD7aFq6C_vEjsW8In3-tQA0fd1ML8nODJw9DjUBmkm8_a50a1LjYWHhcWKisFh-PYSTTeu32J0qMOg1h6AA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001787652537"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "forwardro_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
