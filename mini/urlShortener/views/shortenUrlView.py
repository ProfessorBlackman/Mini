# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

# from mini.urlShortener.serializers.shortenUrlSerializer import ShortenUrlSerializer
from ..serializers.shortenUrlSerializer import ShortenUrlSerializer


class ShortenUrl(generics.GenericAPIView):
    serializer_class = ShortenUrlSerializer

    @swagger_auto_schema(operation_summary='Shortening a url')
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {
                'status': 'success',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            response = {
                'status': 'error',
                'errors': serializer.errors
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
