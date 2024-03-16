from rest_framework.serializers import ModelSerializer
from ..models import Children
class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = Children
        fields = ('pesel','first_name','second_name','surname',
                  'birth_date','birthplace','residential_address','registered_address',
                  'admission_date','leaving_date','photo_path'
                  )