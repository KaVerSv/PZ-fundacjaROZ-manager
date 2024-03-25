from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
# from django.contrib.auth import get_user_model

class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id', 'pesel','first_name','second_name','surname',
                  'birth_date','birthplace','residential_address','registered_address',
                  'admission_date','leaving_date','photo_path', 'relatives'
                  )
        
class RelativesSerializer(ModelSerializer):
    class Meta:
        model = Relatives
        fields = ('id','first_name','second_name','surname',
                  'phone_number', 'residential_address','e_mail'
                  )
        
class ChildrenSerializer2(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id','pesel','first_name','surname','photo_path')

class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id','child_id', 'title', 'contents')


# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'surname', 'e_mail', 'password')

# class UserRegistrationSerializer(serializers.ModelSerializer):
# 	password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
# 	class Meta:
# 		model = get_user_model()
# 		fields = ['email', 'username', 'password']

# 	def create(self, validated_data):
# 		user_password = validated_data.get('password', None)
# 		db_instance = self.Meta.model(email=validated_data.get('email'), username=validated_data.get('username'))
# 		db_instance.set_password(user_password)
# 		db_instance.save()
# 		return db_instance



# class UserLoginSerializer(serializers.Serializer):
# 	email = serializers.CharField(max_length=100)
# 	username = serializers.CharField(max_length=100, read_only=True)
# 	password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
# 	token = serializers.CharField(max_length=255, read_only=True)


















