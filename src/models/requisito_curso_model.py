from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey

class RequisitoCursoModel(db.Model):
    __tablename__ = "requisito_curso"
    
    idrequisito: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    creditos_requisito: Mapped[int] = mapped_column(Integer, nullable=True)
    curso_base: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcurso"), nullable=True)
    curso_requisito: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcurso"), nullable=True)
    curso_posterior: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcurso"), nullable=True)
    
    curso_base_rel = relationship(
        "CursoModel", 
        foreign_keys=[curso_base], 
        back_populates="requisito_base")
    
    requisito_rel = relationship(
        "CursoModel",
        foreign_keys=[curso_requisito],
        back_populates="requisitos_requisito",
    )
    curso_posterior_rel = relationship(
        "CursoModel",
        foreign_keys=[curso_posterior],
        back_populates="requisitos_posterior",
    )