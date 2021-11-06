from rest_framework import fields, serializers
from .models import Book, Borrowing_Log, Message, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BorrwingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing_Log
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
