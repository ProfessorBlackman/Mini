from rest_framework import serializers


#  serializer for RedirectUrlView.py
class RedirectUrlSerializer(serializers.Serializer):

    """
    Serializer for url shortening endpoint.
    """
    # url = serializers.CharField(max_length=300, required=True, write_only=True)
