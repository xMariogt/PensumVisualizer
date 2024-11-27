from src.common.utils import ma
from src.models.carrera_model import CarreraModel
from marshmallow import Schema, fields, validate

class CarreraSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CarreraModel
        load_instance = True
        ordered = True
        include_fk = True
        
        
class CarreraSchemaValidate(Schema):
    nombre = fields.Str(required=True, validate=[validate.Length(min=1, max=45)])