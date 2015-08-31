from rest_framework.response import Response
from py3.apps.service.appmodels import ServiceListAppModel
from py3.apps.service.mappers import ServiceListMapper
from py3.apps.service.mappers.service_list import CategoryListMapper
from py3.apps.service.appmodels.service_list import CategoryListAppModel

from py3.lib.rest_framework.custom_views import FramgiaAPIView


class ServiceListView(FramgiaAPIView):

    def get(self, request, category=None, service=None, format=None):

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

    def get(self, request):
        qs = CategoryListAppModel.get_category_list()
        data = [CategoryListMapper(category).as_dict() for category in qs]
        self.get_response_data(data)
        return Response(self.response_data)


