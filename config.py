import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
    APP_ID = os.environ.get("APP_ID")
    API_HASH = os.environ.get("API_HASH")

    if not TG_BOT_TOKEN or not APP_ID or not API_HASH:
        raise ValueError("❌ خطأ: تأكد من ضبط متغيرات البيئة TG_BOT_TOKEN, APP_ID, و API_HASH")
