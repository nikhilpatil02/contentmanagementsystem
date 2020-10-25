from user.serializers import UsersSerializer
from rest_framework import serializers
from .models import Categories, Content

class ContentSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)
    #user = serializers.IntegerField()
    class Meta:
        model = Content
        #fields = ('title','body','summary','user')
        fields = '__all__'
        
class CategoriesSerializer(serializers.ModelSerializer):
    content = ContentSerializer(read_only=True)
    class Meta:
        model = Categories
        fields = '__all__'