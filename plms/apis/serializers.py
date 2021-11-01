from rest_framework import fields, serializers
from .models import Book, Feedback, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

