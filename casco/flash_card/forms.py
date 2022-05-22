from django import forms
from .models import Deck, Card


class DeckCreateForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = (
            'title',
            'icon',
            'description',
        )


class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = (
            'title',
            'answer',
            'icon',
        )

    def __init__(self, *args, **kwargs):
        self.deck = kwargs.pop('deck')
        super().__init__(*args, **kwargs)

    def save(self, commit=False):
        obj = super().save(commit)
        obj.deck = self.deck
        return super().save(commit=True)


class CardUpdateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = (
            'title',
            'answer',
            'icon',
        )
