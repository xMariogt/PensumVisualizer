from src.common.utils import ma
from src.models.estudiante_model import EstudianteModel
from marshmallow import Schema, fields, validate

class EstudianteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EstudianteModel
        load_instance = True
        ordered = True
        include_fk = True
        
class EstudianteSchemaValidate(Schema):
    carnet = fields.Str(required=True, validate=validate.Length(min=1, max=9))
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=45))
    apellido = fields.Str(required=True, validate=validate.Length(min=1, max=45))
    email = fields.Email(required=True, validate=validate.Length(min=1, max=45))
    fecha_nacimiento = fields.Date(required=True, format='%Y-%m-%d', 
                                validate=validate.Range(min='1900-01-01', max='2021-12-31'))
    password = fields.Str(required=True, validate=validate.Length(min=1, max=45))
    carreraid = fields.Int(required=True)
    