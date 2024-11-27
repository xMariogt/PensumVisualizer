from sqlalchemy import ForeignKey, Integer
from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column

class EstudianteModel(db.Model):
    __tablename__ = "estudiante"
    
    idestudiante: Mapped[int] = mapped_column(primary_key= True, autoincrement=True)
    carnet: Mapped[str] = mapped_column(nullable=False)
    nombre: Mapped[str] = mapped_column(nullable=False)
    apellido: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    fecha_nacimiento: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    carreraid: Mapped[int] = mapped_column(Integer, ForeignKey("carrera.idcarrera"))