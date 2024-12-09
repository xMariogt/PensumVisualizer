from src.models.asignacion_curso_model import AsignacionCursoModel
from src.common.utils import db
from src.models.requisito_curso_model import RequisitoCursoModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class CursoModel(db.Model):
    __tablename__ = "curso"
    
    idcurso: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codigocurso: Mapped[str] = mapped_column(nullable=False)
    nombre: Mapped[str] = mapped_column(nullable=False)
    obligatorio: Mapped[bool] = mapped_column(nullable=False)
    creditos: Mapped[int] = mapped_column(nullable=False)

    requisito_base: Mapped[list[RequisitoCursoModel]] = relationship(
        RequisitoCursoModel, 
        foreign_keys="RequisitoCursoModel.curso_base", 
        back_populates="curso_base_rel")
    
    requisitos_requisito: Mapped[list[RequisitoCursoModel]] = relationship(
        RequisitoCursoModel,
        foreign_keys="RequisitoCursoModel.curso_requisito",
        back_populates="requisito_rel",
    )
    requisitos_posterior: Mapped[list[RequisitoCursoModel]] = relationship(
        RequisitoCursoModel,
        foreign_keys="RequisitoCursoModel.curso_posterior",
        back_populates="curso_posterior_rel",
    )
    
    asignacion_curso: Mapped[AsignacionCursoModel] = relationship()