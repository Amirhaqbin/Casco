from django.db import models


class Deck(models.Model):

    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='static/images/icons/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    views_count = models.PositiveSmallIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = 'Decks'



class Card(models.Model):

    title = models.CharField(max_length=200)
    answer = models.CharField(max_length=300)
    icon = models.ImageField(upload_to='static/images/icons/%Y/%m/%d', null=True, blank=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = 'Cards'