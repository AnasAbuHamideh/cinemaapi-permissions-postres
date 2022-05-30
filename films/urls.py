from django.urls import path
from films.api.viewsets import (
                            FilmsDetailView, 
                            FilmsListView
                        )

urlpatterns = [
    path('films-list', FilmsListView.as_view(), name = 'flims_list'),
    path('film-detail/<int:pk>', FilmsDetailView.as_view(), name = 'film_detail'),
]