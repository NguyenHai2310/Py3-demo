from marshmallow import Schema, fields
from py3.apps.models import Store


class StoreSchema(Schema):
    name = fields.Str()


class ListStoreSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)
    description = fields.Str()

    def make_object(self, data):
        return Store(**data)