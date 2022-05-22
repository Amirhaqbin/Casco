from django.urls import path
from .views import (
    DeckListView,
    DeckDetailView,
    DeckDeleteView,
    DeckCreateView,
    DeckUpdateView,
    CardCreateView,
    CardDeleteView,
    CardUpdateView,
)


app_name = 'flash_card'
urlpatterns = [
    path('decks/', DeckListView.as_view(), name='deck-list'),
    path('decks/<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('decks/create/', DeckCreateView.as_view(), name='deck-create'),
    path('decks/<int:pk>/update/', DeckUpdateView.as_view(), name='deck-update'),
    path('decks/<int:pk>/delete/', DeckDeleteView.as_view(), name='deck-delete'),

    path('decks/<int:pk>/card-create/', CardCreateView.as_view(), name='card-create'),
    path('decks/<int:pk>/card<int:id>-update/', CardUpdateView.as_view(), name='card-update'),
    path('decks/<int:pk>/card<int:id>-delete/', CardDeleteView.as_view(), name='card-delete'),
]
