from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='insert'),
    path('<int:id>/',views.home,name='update'),
    path('searchbar/',views.searchbar,name='search-expert'),
    path('showexperts/',views.show_experts,name='show-experts'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('collections/', views.collections,name='collections'),

]