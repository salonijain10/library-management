from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('admin_signup/',views.admin_signup, name='admin_signup'),
    path('login_admin/',views.login_admin, name='login_admin'),    
    path('addbook/',views.addbook, name='addbook'),  
    path('viewbook/',views.viewbook, name='viewbook'), 
    path('adminhome/',views.adminhome, name='adminhome'), 
    path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
]