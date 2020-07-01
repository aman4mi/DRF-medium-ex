
from rest_framework import serializers
from .models import Songs
from django.contrib.auth.models import User
 

class SongsSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    print ('hi' + str(owner))

    class Meta:
        model = Songs
        fields = ("title", "artist", "owner")  
        print (fields)    
        print ('hi' + str(model))

    # def __str__(self):
    #     return "My name is %s %s %s" % (self.title, self.artist, self.owner)   
    

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)  
    # print (token) 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")    