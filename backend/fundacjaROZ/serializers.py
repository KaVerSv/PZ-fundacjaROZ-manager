from rest_framework.serializers import ModelSerializer
from .models import Children, Relatives#, Association

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
        
# class AssociationSerializer(ModelSerializer):
#     class Meta:
#         model = Association
#         fields = ('association_type',)  # tylko pole 'association_type'

# class RelativesSerializer2(ModelSerializer):
#     associations = AssociationSerializer(many=True, source='association_set')

#     class Meta:
#         model = Relatives
#         fields = ('id','first_name','second_name','surname',
#                   'phone_number', 'residential_address','e_mail', 'associations'
#                   )

class ChildrenSerializer2(ModelSerializer):
    class Meta:
        model = Children
        fields = ('id','pesel','first_name','surname','photo_path')