from src.common.utils import ma
from src.models.requisito_curso_model import RequisitoCursoModel
from marshmallow import Schema, fields, validate

class RequisitoCursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RequisitoCursoModel
        load_instance = True
        ordered = True
        include_fk = True
        
class RequisitoCursoSchemaValidate(Schema):
    cursoid = fields.Int(required=True)
    curso_requisito = fields.Int(required=False)
    curso_posterior = fields.Int(required=False)
    creditos_requisidto = fields.Int(required=False, validate=validate.Range(1, 250))