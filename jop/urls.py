from django.urls import path ,include
from . import views
app_name='jop'
urlpatterns = [
    path('',views.jop_list,name='jop_list'),
    path('<str:slug>',views.jop_detail, name='jop_detail'),
    
    path('cbv',views.JopList.as_view(), name='jop_list'),
    path('cbv/<int:pk>',views.JopDetail.as_view(), name='jop_detail'),
    
    
    
]
