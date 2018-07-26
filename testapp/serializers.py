from rest_framework import serializers
from testapp.models import TestTable


class TestAppAddSerializer(serializers.ModelSerializer):
    class Meta:
        models = TestTable
        ordering = ('-name',)




