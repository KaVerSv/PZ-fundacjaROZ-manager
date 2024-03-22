from rest_framework.serializers import ModelSerializer
from .models import Children, Relatives, Association, Notes

class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id', 'pesel','first_name','second_name','surname',
                  'birth_date','birthplace','residential_address','registered_address',
                  'admission_date','leaving_date','photo_path'
                  )
        
class RelativesSerializer(ModelSerializer):
    class Meta:
        model = Relatives
        fields = ('id','first_name','second_name','surname',
                  'phone_number', 'residential_address','e_mail'
                  )

class RelativesSerializer2(ModelSerializer):
    class Meta:
        model = Relatives, Association
        fields = ('association_type', 'relative_id','id','first_name','second_name','surname',
                  'phone_number', 'residential_address','e_mail', 'associations'
                  )

class ChildrenSerializer2(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id','pesel','first_name','surname','photo_path')

class AssociationSerializer(ModelSerializer):
    class Meta:
        model = Association
        fields = ('id','child_id','relative_id','association_type')

class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id','child_id', 'title', 'contents')