from src.common.utils import ma
from src.models.requisito_curso_model import RequisitoCursoModel
from marshmallow import Schema, fields, validate

class RequisitoCursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RequisitoCursoModel
        load_instance = True
        ordered = True
        include_fk = True
        include_relationships = True
        
    curso_base_rel = fields.Nested("CursoSchema", exclude=("requisitos_requisito", "requisitos_posterior", "requisito_base", "asignacion_curso"))
    requisito_rel = fields.Nested("CursoSchema",exclude=("requisitos_requisito", "requisitos_posterior", "requisito_base", "asignacion_curso"))
    curso_posterior_rel = fields.Nested("CursoSchema", exclude=("requisitos_requisito", "requisitos_posterior", "requisito_base", "asignacion_curso"))

class RequisitoCursoSchemaValidate(Schema):
    cursoid = fields.Int(required=True)
    curso_requisito = fields.Int(required=False)
    curso_posterior = fields.Int(required=False)
    creditos_requisidto = fields.Int(required=False, validate=validate.Range(1, 250))