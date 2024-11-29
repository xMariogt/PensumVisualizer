from flask_restx import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy import func
from src.models.carrera_model import CarreraModel
from src.models.curso_model import CursoModel
from src.common.utils import db
from src.models.carrera_curso_model import CarreraCursoModel
from src.schemas.carrera_curso_schema import CarreraCursoSchema, CarreraCursoSchemaValidate


class CarreraCursoController(Resource):

    #@jwt_required()
    def get(self):
        
        carreras = CarreraCursoModel.query.order_by(CarreraCursoModel.semestre).where(CarreraCursoModel.carreraid == 1).all()
        
        return CarreraCursoSchema(many=True).dump(carreras), 200