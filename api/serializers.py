from rest_framework import serializers
from .models import Users, Categories, Content

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
         

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