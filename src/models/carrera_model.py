from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column

class CarreraModel(db.Model):
    __tablename__ = "carrera"

    idcarrera: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(nullable=False)