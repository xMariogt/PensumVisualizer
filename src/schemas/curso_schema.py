from src.common.utils import ma
from src.models.curso_model import CursoModel
from marshmallow import Schema, fields, validate

class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CursoModel
        load_instance = True
        ordered = True
        include_fk = True
        
class CursoSchemaValidate(Schema):
    codigocurso = fields.Str(required=True, validate=[validate.Length(min=1, max=10)])
    nombre = fields.Str(required=True, validate=[validate.Length(min=1, max=45)])
    creditos = fields.Int(required=True, validate=validate.Range(1, 12))