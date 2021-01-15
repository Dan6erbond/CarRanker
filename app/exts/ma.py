import json


from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError

ma = Marshmallow()


class Json(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return json.dumps(value)

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return [json.loads(value)]
        except ValueError as error:
            raise ValidationError("Pin codes must contain only digits.") from error
