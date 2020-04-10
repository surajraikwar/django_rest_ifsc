from rest_framework import serializers
from .models import Bank, Branch

class BranchSerializer(serializers.ModelSerializer):
    bank = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Branch
        fields = (
            'ifsc', 'name', 'bank', 'address',
            'city', 'state')
