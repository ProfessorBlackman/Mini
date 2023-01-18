import random
import string

from rest_framework import status
from rest_framework.response import Response

from ..models.urlmodel import UrlData


#  function to generate short url from long url
def urlgen(name, long):
    if UrlData.objects.filter(long_url=long).exists():  # see if any object with long as long_url exists
        response = {
            'status': 'error',
            'errors': 'url already exists',
        }
        return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(6)) # generate slug from ascii characters
        new_url = f'http://127.0.0.1:8000/{result_str}'
        print("Random string of length", long, "is:", result_str)
        print(new_url)
        try:
            new = UrlData(name=name, long_url=long, short_url=new_url, slug=result_str)  # storing info in database
            new.save()
        except:
            response = {
                'status': 'error',
                'errors': 'Invalid Details'
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    return True, new_url
