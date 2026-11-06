from pydantic import BaseModel, Field

class Alumno(BaseModel):
    matricula: str = Field(..., description="The unique identifier for the student")
    nombre: str = Field(..., description="The name of the student")
    edad: int = Field(..., description="The age of the student")
    apellidos: str = Field(..., description="The last names of the student")
    materias: list[str] = Field(..., description="The subject the student is enrolled in")


class Config:
    json_schema_extra = {
        "example": {
            "matricula": "123456",
            "nombre": "Juan",
            "edad": 20,
            "apellidos": "Pérez Gómez",
            "materias": ["Matemáticas", "Física", "Química"]
        }
    }