from django.shortcuts import render , HttpResponse , get_object_or_404
from .models import Event , Registration


def event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description =request.POST.get('description')
        # print(description)
        date = request.POST.get('date')
        location = request.POST.get('location')
        evn = Event(title = title , description = description , date = date , location = location)
        evn.save()
        return render(request , 'eventcreated.html')
    else:
        return render(request, 'EventForm.html' )

def RegistrationForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        event = request.POST.get('event')
        eve = Event.objects.get(title = event)
        # print(name, email )
        rega = Registration.objects.create(name = name , email = email , event = eve)
        # print(rega)
        rega.save()
        return render(request , 'registration_confirmation.html')
    else:
        return render(request, 'RegistrationForm.html')


def home(requets):
    
    events = Event.objects.all()
  
    return render(requets , 'home.html' , {'events': events})



def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # form = RegistrationForm(request)
    return render(request, 'event_detail.html', {'event': event, })