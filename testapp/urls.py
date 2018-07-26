from django.urls import path

from .views import TestTableAddView


app_name = 'testapp'

urlpatterns = [
    # list | add | /1/show/ | 1/update | 3/delete
    path('add/', TestTableAddView.as_view(), name='Add Test App'),

]
