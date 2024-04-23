from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model

class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id', 'pesel','first_name','second_name','surname',
                  'birth_date','birthplace','residential_address','registered_address',
                  'admission_date','leaving_date','photo_path', 'relatives'
                  )
        
class ChildrenSerializer1(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id', 'pesel','first_name','second_name','surname',
                  'birth_date','birthplace','residential_address','registered_address',
                  'admission_date','leaving_date','photo_path'
                  )
    
class RelativesSerializer(serializers.ModelSerializer):
    relation = serializers.SerializerMethodField()

    class Meta:
        model = Relatives
        fields = ['first_name', 'second_name', 'surname', 'phone_number', 'residential_address', 'e_mail', 'legal_status', 'relation']

    def get_relation(self, obj):
        child_id = self.context.get('child_id')
        relation = FamilyRelationship.objects.filter(child_id=child_id, relative=obj).first()
        return relation.relation if relation else None
          
class ChildrenSerializer2(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id','pesel','first_name','surname','photo_path')

class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id','child_id', 'title', 'contents')

class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','first_name','surname','email')

class DocumentsSerializer(ModelSerializer):
    class Meta:
        model = Documents
        fields = ('id','name','date','file_name', 'child_id')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'surname', 'password']

    def create(self, validated_data):
        user_password = validated_data.get('password', None)
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        surname = validated_data.get('surname')

        db_instance = self.Meta.model(
            email=email,
            first_name=first_name,
            surname=surname
        )
        db_instance.set_password(user_password)
        db_instance.save()
        return db_instance

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
    token = serializers.CharField(max_length=255, read_only=True)