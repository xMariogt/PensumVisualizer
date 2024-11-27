from src.common.utils import ma
from src.models.carrera_curso_model import CarreraCursoModel
from marshmallow import Schema, fields, validate

class CarreraCursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CarreraCursoModel
        load_instance = True
        ordered = True
        include_fk = True
        
class CarreraCursoSchemaValidate(Schema):
    carreraid = fields.Int(required=True)
    cursoid = fields.Int(required=True)
    semestre = fields.Str(required=True, validate=validate.Length(min=1, max=6))