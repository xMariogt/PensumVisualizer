from flask_restx import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy import func
from src.schemas.curso_schema import CursoSchema
from src.models.carrera_model import CarreraModel
from src.models.curso_model import CursoModel
from src.common.utils import db
from src.models.carrera_curso_model import CarreraCursoModel
from src.schemas.carrera_curso_schema import CarreraCursoSchema, CarreraCursoSchemaValidate


class CarreraCursoController(Resource):

    #@jwt_required()
    def get(self):
        
        carreras = CarreraCursoModel.query.where(CarreraCursoModel.carreraid == 3).all()
        
        return CarreraCursoSchema(many=True).dump(carreras), 200