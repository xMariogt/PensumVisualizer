from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

class AsignacionCursoModel(db.Model):
    __tablename__= "asignacion_curso"
    
    idasignacion: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    estado: Mapped[str] = mapped_column(nullable=False)
    nota: Mapped[int] = mapped_column(nullable=False)
    cursoid: Mapped[int] = mapped_column(Integer, ForeignKey("curso.idcurso"), nullable=False)
    estudianteid: Mapped[int] = mapped_column(Integer, ForeignKey("estudiante.idestudiante"), nullable=False)