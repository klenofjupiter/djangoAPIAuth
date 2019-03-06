from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
	class Meta: #this establishes what is "exposed" when you send forward a model instance
		model = Todo
		fields = ('id', 'title', 'body')