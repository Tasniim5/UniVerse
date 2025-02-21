from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Event, Review

# Create your views here.
class Events(generic.ListView):
  queryset = Event.objects.all()
  template_name = 'events/events.html'
  paginate_by = 4

def event_detail(request, slug):
  queryset = Event.objects.all()
  event = get_object_or_404(queryset, slug=slug)

  return render(
    request,
    "events/event_detail.html",
    {
      "event": event,
    }
  )
