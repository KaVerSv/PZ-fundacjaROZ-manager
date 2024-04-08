from rest_framework.serializers import ModelSerializer
from ..models import Children, Relatives

class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = Children
        fields = ('pesel','first_name','second_name','surname',
                  'birth_date','birthplace','residential_address','registered_address',
                  'admission_date','leaving_date','photo_path'
                  )
        
class RelativesSerializer(ModelSerializer):
    class Meta:
        model = Relatives
        fields = ('first_name','second_name','surname',
                  'phone_number', 'residential_address','e_mail',
                  'association_type', 'child_pesel'
                  )
