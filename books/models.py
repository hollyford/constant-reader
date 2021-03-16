from django.db import models


class Genres(models.Model):

    class Meta:
        verbose_name_plural = 'Genres'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Books(models.Model):

    class Meta:
        verbose_name_plural = 'Books'

    genres = models.ForeignKey('Genres', null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=15)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    # Check the contents of the brackets below. Would like to know if need to 
    # add auto_now and auto_now_add as definitely want these to be false
    # Also want to understand how to use the options to format the imput
    published = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    binding = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

