from rest_framework.serializers import ModelSerializer
from .models import Children, Relatives, FamilyRelationship, Enrollment, Schools, Notes, User, Documents
from rest_framework import serializers
from django.contrib.auth import get_user_model

class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id', 'pesel','first_name','second_name','surname',
                  'birth_date','birthplace','residential_address','registered_address',
                  'admission_date','leaving_date','photo_path'
                  )
    
class RelativesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatives
        fields = ['id', 'first_name', 'second_name', 'surname', 'phone_number', 'residential_address', 'e_mail', 'legal_status', 'alive']


class ChildrenRelativesSerializer(serializers.ModelSerializer):
    relation = serializers.SerializerMethodField()

    class Meta:
        model = Relatives
        fields = ['id', 'first_name', 'second_name', 'surname', 'phone_number', 'residential_address', 'e_mail', 'legal_status', 'alive', 'relation']

    def get_relation(self, obj):
        child_id = self.context.get('child_id')
        relation = FamilyRelationship.objects.filter(child_id=child_id, relative=obj).first()
        return relation.relation if relation else None

class ChildrenSchoolsSerializer(serializers.ModelSerializer):
    start_date = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = Schools
        fields = ['id', 'name', 'address', 'start_date', 'end_date', 'phone_number','e_mail']

    def get_start_date(self, obj):
        child_id = self.context.get('child_id')
        print(obj)
        if isinstance(obj, Schools):
            school=obj
        else:
            school_name = obj.get('name') 
            school_address = obj.get('address') 

            school = Schools.objects.filter(name=school_name, address=school_address).first()

        if school:
            start_date = Enrollment.objects.filter(child_id=child_id, school=school).first()
            return start_date.start_date if start_date else None
        else:
            return None  
        
    def get_end_date(self, obj):
        child_id = self.context.get('child_id')
        if isinstance(obj, Schools):
            school=obj
        else:
            school_name = obj.get('name') 
            school_address = obj.get('address') 

            school = Schools.objects.filter(name=school_name, address=school_address).first()

        if school:
            end_date = Enrollment.objects.filter(child_id=child_id, school=school).first()
            return end_date.end_date if end_date else None
        else:
            return None  

    
class RelativeChildrensSerializer(serializers.ModelSerializer):
    relation = serializers.SerializerMethodField()

    class Meta:
        model = Children
        fields = ['pesel','first_name','second_name','surname',
                  'birth_date','birthplace','residential_address','registered_address',
                  'admission_date','leaving_date','photo_path','relation']
                  
    def get_relation(self, obj):
        relative_id = self.context.get('relative_id')
        relation = FamilyRelationship.objects.filter(child=obj, relative_id=relative_id).first()
        return relation.relation if relation else None
   
    
class ShortChildrenSerializer(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id','pesel','first_name','surname','photo_path','birth_date','admission_date','leaving_date')

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
        fields = ('id','signature','specification','date','file_name', 'child_id', 'relative_id')

class SchoolsSerializer(ModelSerializer):
    class Meta:
        model = Schools
        fields = ('id', 'name', 'address','phone_number','e_mail')

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