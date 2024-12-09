from flask_restx import Resource
from src.models.curso_model import CursoModel
from src.schemas.curso_schema import CursoSchema

class CursoController(Resource):
    def get(self):
        
        cursos = CursoModel.query.all()
        
        return CursoSchema(many=True).dump(cursos), 200