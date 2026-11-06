from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from db import collection
from models import Alumno

router = APIRouter()


@router.post("/alumno", response_description="Add new student")
async def create_alumno(item: Alumno = Body(...)):
    alumno = jsonable_encoder(item)
    new_alumno = await collection.insert_one(alumno)
    return {"message": "Alumno added successfully", "id": str(new_alumno.inserted_id)}


@router.get("/alumnos", response_description="Get all students")
async def get_alumnos():
    alumnos = await collection.find({}).to_list(length=None)
    return [jsonable_encoder({**alumno, "_id": str(alumno.get("_id"))}) for alumno in alumnos]