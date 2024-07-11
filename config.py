from dotenv import load_dotenv
import os

load_dotenv()

TEXT = open("message.txt", "r").read()

ACCESS_TOKEN = str(os.environ.get("ACCESS_TOKEN"))
POST_ID = str(os.environ.get("POST_ID"))
MSG_TEXT = str(os.environ.get("MSG_TEXT"))
TRIGGER = str(os.environ.get("TRIGGER"))