
from rest_framework import serializers
from .models import Songs
from django.contrib.auth.models import User
 

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")  
        # print (fields)    

    # def __str__(self):
    #     return '%s: %s' % (self.title, "Mr. "+self.artist)   
    # 

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)  
    print (token) 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")    