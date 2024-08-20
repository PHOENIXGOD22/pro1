from django.urls import path
from.import views

urlpatterns=[
    path('',views.fun1),
    path('disp',views.disp,name='disp'),
    path('upd',views.update1,name='upd'),
    path('upd',views.delete,name='upd'),
    # path('home',views.disp,name='home'),
    path('phonebook',views.addphone),
    path('two',views.display),
    path('update',views.update1),
    path('delete',views.delete),
    path('back',views.back,name='back'),
]