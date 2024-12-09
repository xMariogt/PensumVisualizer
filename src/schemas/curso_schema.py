from src.schemas.asignacion_curso_schema import AsignacionCursoSchema
from src.common.utils import ma
from src.models.curso_model import CursoModel
from src.schemas.requisito_curso_schema import RequisitoCursoSchema
from marshmallow import Schema, fields, validate

class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CursoModel
        load_instance = True
        ordered = True
        include_fk = True
        include_relationships = True
        
    requisito_base = fields.Nested("RequisitoCursoSchema", many=True, exclude=("curso_base_rel", ))
    asignacion_curso = fields.Nested(AsignacionCursoSchema)
    #requisitos_requisito = fields.Nested("RequisitoCursoSchema", many=True, exclude=("curso_posterior_rel", "curso_base_rel"))
    #requisitos_posterior = fields.Nested("RequisitoCursoSchema", many=True)

class CursoSchemaValidate(Schema):
    codigocurso = fields.Str(required=True, validate=[validate.Length(min=1, max=10)])
    nombre = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    creditos = fields.Int(required=True, validate=validate.Range(1, 12))
    
