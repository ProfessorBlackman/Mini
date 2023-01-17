from rest_framework import serializers


class ShortenUrlSerializer(serializers.Serializer):

    """
    Serializer for url shortening endpoint.
    """
    long_url = serializers.CharField(min_length=8, required=True, write_only=True)
