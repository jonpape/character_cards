from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterList.as_view(), name='character_list'),
    path('character-create', views.CharacterCreate.as_view(), name='character_create'),
    path('character-detail/<int:pk>', views.CharacterDetail.as_view(), name='character_detail'),
    path('character-update/<int:pk>', views.CharacterUpdate.as_view(), name='character_update'),
    path('character-delete/<int:pk>', views.CharacterDelete.as_view(), name='character_delete'),
    path('search/', views.search_results, name='search_results'),
]