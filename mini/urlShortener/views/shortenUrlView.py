# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

from ..serializers.shortenUrlSerializer import ShortenUrlSerializer
from ..utils.generate_url import urlgen


#  view for shortening the long url
class ShortenUrl(generics.GenericAPIView):
    serializer_class = ShortenUrlSerializer

    @swagger_auto_schema(operation_summary='Shortening a url')
    def post(self, request):
        data = request.data
        long = data.get('long_url')
        name = data.get('name')
        print(long)
        print(name)
        self.serializer_class(data=data)
        generate_url = urlgen(name, long)
        if generate_url:
            response = {
                'status': 'success',
                'data': generate_url
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
