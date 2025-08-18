from django.urls import path
from . import views

urlpatterns = [
    path('register/<int:tree_id>', views.register_member, name='register_member'),
]