import colander


# schema store and store's service
class Service(colander.MappingSchema):
    name = colander.SchemaNode(colander.String(), validator=colander.Length(10, 100))
    price = colander.SchemaNode(colander.Float(), validator=colander.Range(10, 100))
    store_id = colander.SchemaNode(colander.Int())


class ListStore(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int())
    name = colander.SchemaNode(colander.String(), validator=colander.Length(10, 100))
    description = colander.SchemaNode(colander.String(), validator=colander.Length(10, 100))
    phone_number = colander.SchemaNode(colander.Int(), validator=colander.Length(8, 20))
    address = colander.SchemaNode(colander.String(), validator=colander.Length(max=200))
    # services = Services()


class Services(colander.SequenceSchema):
    service = Service()
