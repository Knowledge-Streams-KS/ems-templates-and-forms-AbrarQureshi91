from django.forms import ModelForm
from eventapp.models import Event

class Eventform(ModelForm):
    class Meta:
        model = Event
        fields = ['title' , 'description' , 'date ' , 'location']

form = Eventform

event = Event.objects.get('title')
form = Eventform(instance=event)