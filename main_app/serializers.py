# Needed to convert model Instances to JSON so frontend can receive data

from rest_framework import serializers
from .models import User
#Model to work with and the fields to convert to JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'ticker', 'investmentAmount',  'tickerarray')
