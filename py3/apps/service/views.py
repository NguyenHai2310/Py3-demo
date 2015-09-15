from rest_framework.response import Response
from py3.apps.service.appmodels import ServiceListAppModel
from py3.apps.service.mappers import ServiceListMapper
from py3.apps.service.mappers.service_list import CategoryMapper, StoreMapper, ServiceListStoreMapper, CategoryForStoreMapper
from py3.apps.service.appmodels.service_list import CategoryListAppModel, StoreList
from py3.apps.service.mappers.colanderr import Service, ListStore, Services
from py3.lib.rest_framework.custom_views import FramgiaAPIView
import colander


class ServiceListView(FramgiaAPIView):

    def get(self, request, category=None, service=None, store=None):

        search_query = self.convert_querydict_to_dict(request.QUERY_PARAMS)

        if category:
            search_query['category'] = category
        if service:
            search_query['service'] = service

        qs = ServiceListAppModel.get_service_list(search_query)
        data = [ServiceListMapper(service).as_dict() for service in qs]
        self.get_response_data(data)
        return Response(self.response_data)


class CategoryListView(FramgiaAPIView):

    def get(self, request, category=None):
        search_query = self.convert_querydict_to_dict(request.QUERY_PARAMS)

        if category:
            search_query['category'] = category
            qs = CategoryListAppModel.get_store_list(category)
            data = [CategoryForStoreMapper(category).as_dict() for category in qs]
        else:
            qs = CategoryListAppModel.get_store_list()
            data = [CategoryMapper(category).as_dict() for category in qs]

        self.get_response_data(data)
        return Response(self.response_data)


class ServiceListViewByStore(FramgiaAPIView):
    """

    :params request list stores or store's service
    :params string store:
         store's name
    :rtype  json or error
        if validator have a error, json will not return
    """

    def get(self, request, store=None):
        search_query = self.convert_querydict_to_dict(request.QUERY_PARAMS)
        self.response_data['errors']=[]
        self.response_data['results']={}

        if store:
            schema = Service()
            qs = StoreList.get_store_list(store)
            # try serialize
            try:
                result = [schema.serialize(st.__dict__) for st in qs]
                self.get_response_data(result)
            except colander.Invalid as e:
                errors = e.asdict()
                # response error
                self.response_data['errors']+=[errors]
        else:
            schema = ListStore()
            qs = StoreList.get_store_list()
            try:
                result = [schema.serialize(st.__dict__) for st in qs]
                self.get_response_data(result)
            except colander.Invalid as e:
                errors = e.asdict()
                self.response_data['errors']+=[errors]

        return Response(self.response_data)
