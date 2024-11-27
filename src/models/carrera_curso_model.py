from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

class CarreraCursoModel(db.Model):
    __tablename__="carrera_curso"
    
    idcarrera: Mapped [int] = mapped_column(primary_key=True, autoincrement=True)
    cursoid: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcuros"), nullable=False)
    carreraid: Mapped[int] = mapped_column(Integer, ForeignKey("carrera.idcarrera"), nullable=False)
    semestre: Mapped[str] = mapped_column(nullable=False)