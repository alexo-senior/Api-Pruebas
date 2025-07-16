from dotenv import load_dotenv
import os

load_dotenv()

print("CLIENT_ID:", os.getenv("CLIENT_ID"))
print("AUTH_URL:", os.getenv("AUTH_URL"))
print("REDIRECT_URI:", os.getenv("REDIRECT_URI"))
print("PORT:", os.getenv("PORT"))


