from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column

class CursoModel(db.Model):
    __tablename__ = "curso"
    
    idcurso: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codigocurso: Mapped[str] = mapped_column(nullable=False)
    nombre: Mapped[str] = mapped_column(nullable=False)
    creditos: Mapped[int] = mapped_column(nullable=False)