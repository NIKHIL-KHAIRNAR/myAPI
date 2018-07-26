from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import TestTable
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView


class TestTableAddView(GenericAPIView):
    from .serializers import TestAppAddSerializer
    
    serializer_class = TestAppAddSerializer
    renderer_classes = (JSONRenderer, )
    queryset = TestTable.objects.all()


class TestTableDetail(RetrieveUpdateDestroyAPIView):
    from .serializers import TestAppAddSerializer

    queryset = TestTable.objects.all()
    serializer_class = TestAppAddSerializer


