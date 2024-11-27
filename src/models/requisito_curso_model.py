from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

class RequisitoCursoModel(db.Model):
    __tablename__ = "requisito_curso"
    
    idrequisito: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    creditos_requisito: Mapped[int] = mapped_column(nullable=True)
    cursoid: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcurso"), nullable=True)
    curso_requisito: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcurso"), nullable=True)
    curso_posterior: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcurso"), nullable=True)