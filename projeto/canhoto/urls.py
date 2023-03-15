from django.urls import path
from projeto.canhoto import views

app_name = 'canhoto'

urlpatterns = [
    path('', views.CanhotoList.as_view(), name='canhoto_list'),
    path('<int:pk>', views.canhoto_detail, name='canhoto_detail'),
    path('add/', views.CanhotoCreate.as_view(), name='canhoto_add'),
    path('<int:pk>/edit/', views.CanhotoUpdate.as_view(), name='canhoto_edit'),
]

