from src.models.curso_model import CursoModel
from src.models.carrera_model import CarreraModel
from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey

class CarreraCursoModel(db.Model):
    __tablename__="carrera_curso"
    
    idcarrera_curso: Mapped [int] = mapped_column(primary_key=True, autoincrement=True)
    cursoid: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcurso"), nullable=False)
    carreraid: Mapped[int] = mapped_column(Integer, ForeignKey("carrera.idcarrera"), nullable=False)
    semestre: Mapped[str] = mapped_column(nullable=False)
    
    carrera: Mapped[CarreraModel] = relationship("CarreraModel", backref="carreras")
    curso: Mapped[list[CursoModel]] = relationship("CursoModel", backref="cursos")