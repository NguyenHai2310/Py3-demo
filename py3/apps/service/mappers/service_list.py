from bpmappers import Mapper, djangomodel
from bpmappers.fields import (
    NonKeyDelegateField,
    RawField,
    ListDelegateField,
)
from py3.apps.models import Service

class ServiceMapperForServiceList(Mapper):
    service_id = RawField('id')
    service_name = RawField('name')


class ServiceCategoryMapperForServiceList(Mapper):
    service_category = RawField('name')


class StoreMapperForServiceList(Mapper):
    store_name = RawField('name')


class ServiceListMapper(Mapper):

    service = NonKeyDelegateField(ServiceMapperForServiceList,
                                  attach_parent=True)
    service_category = NonKeyDelegateField(
        ServiceCategoryMapperForServiceList,
        attach_parent=True
    )

    def filter_service(self):
        return self.data[0]

    def filter_service_category(self):
        return self.data[1]


class CategoryForStoreMapper(Mapper):
    name = RawField('Category.name')
    store = RawField('Store.name')


class CategoryMapper(Mapper):
    name = RawField('name')
    description = RawField('description')

    # description = RawField('description')
    # stores = ListDelegateField(StoreMapperForServiceList)

#
# class StoreListMapper(Mapper):
#     name = RawField('name')
#     description = RawField('description')
#     phone_number = RawField('phone_number')
#     address = RawField('address')
#     categories = ListDelegateField(CategoryListMapper)


class StoreMapper(Mapper):
    store_id = RawField('id')
    store_name = RawField('name')
    description = RawField('description')


class ServiceListStoreMapper(djangomodel.ModelMapper):
    name = RawField()



