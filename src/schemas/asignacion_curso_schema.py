from src.common.utils import ma
from src.models.asignacion_curso_model import AsignacionCursoModel
from marshmallow import Schema, fields, validate

class AsignacionCursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AsignacionCursoModel
        load_instance = True
        ordered = True
        include_fk = True
        
class AsignacionCursoSchemaValidate(Schema):
    cursoid = fields.Int(required=True)
    estudianteid = fields.Int(required=True)
    estado = fields.Str(required=True, validate=validate.OneOf(['reproved', 'approved']))
    nota = fields.Int(required=False, validate=validate.Range(min=61, max=100))
    