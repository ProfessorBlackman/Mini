from rest_framework import serializers


#  serializer for ShortenUrlView
class ShortenUrlSerializer(serializers.Serializer):

    """
    Serializer for url shortening endpoint.
    """
    name = serializers.CharField(max_length=300)
    long_url = serializers.CharField(max_length=300, required=True)
