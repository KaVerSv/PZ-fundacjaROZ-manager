from rest_framework.serializers import ModelSerializer
from .models import *

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


class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'surname', 'e_mail', 'password')


















