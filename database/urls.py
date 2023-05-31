from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('contact/create/', views.create_contact, name='create_contact'),
    path('contact/view/<int:id>', views.view_contact, name='view_contact'),
    path('contact/update/<int:id>', views.update_contact, name='update_contact'),
    path('contact/delete/<int:id>', views.delete_contact, name='delete_contact'),
    path('contact/members/', views.members, name='members'),
]
