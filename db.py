import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv("atlas-credentials.env")

mongodb_uri = os.getenv("MONGODB_URI")
if not mongodb_uri:
    raise ValueError("La variable MONGODB_URI no está configurada.")
# Conexión de cliente
client = AsyncIOMotorClient(mongodb_uri)

#Selección de la base de datos
db = client.my_database

#Selección de una colección
collection = db.get_collection("my_collection")

