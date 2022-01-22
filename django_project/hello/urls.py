from django.urls import path

from hello.serializers import HelloSerializer
from . import views
from .models import Hello
urlpatterns =[
    # path("",views.HelloViewSet.as_view(), name="hello"),
    path("", views.HelloView.as_view(), name='hello-list')
# queryset=Hello.objects.all(), serializer_class=HelloSerializer
]
