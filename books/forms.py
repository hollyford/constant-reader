from django import forms
from .models import Books, Genres


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    genres = Genres.objects.all()
    friendly_names = [(g.id, g.get_friendly_name()) for g in genres]

    self.fields['genre'].choices = friendly_names
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'border-black rounded-0'
