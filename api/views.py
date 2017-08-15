import coreapi

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView

class RiverViewSet(APIView):
    """
    API endpoint that shows river data.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        return JsonResponse(coreapi.Client().get('http://riverbrain.com/api/v1/rivers'), safe=False)
