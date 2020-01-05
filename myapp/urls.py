from django.urls import path
from myapp import views
app_name='myapp'
urlpatterns=[
path('',views.home,name='home'),
path('list/',views.ComputerList,name='list'),
path('edit/<pk>/',views.ComputerEdit,name='edit'),
path('delete/<pk>/',views.computer_delete,name="delete")
]
