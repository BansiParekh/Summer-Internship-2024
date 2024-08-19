from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index' ),
    path('newnote',views.new_note,name='new_note' ),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete' ),
    path('search',views.search,name='search' ),
    path('index1/',views.index1,name='index1' ),


]