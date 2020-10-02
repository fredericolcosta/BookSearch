from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
NAME = os.getenv("NAME")

