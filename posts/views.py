from django.shortcuts import render, get_object_or_404

from .models import *

def travel_view(request):
    travels = Travel.objects.all()
    return render(request, 'travels/travels.html', {'travels':travels})

def detail_view(request, id):
    travel = get_object_or_404(Travel, id=id)
    days = Day.objects.filter(travel=travel).order_by('-day')
    Locations = []
    for day in days:
        Locations.append(TravelLocation.objects.filter(day=day))
    return render(request, 'travels/detail.html', {
        'travel':travel,
        'days' : days,
        'locations':Locations
    })
    
def detail_day_view(request, id, date):
    locations = TravelLocation.objects.filter(id=date)
    pictures = []
    for location in locations:
        pictures.append([])
        photos = TravelLocationImage.objects.filter(TravelLocation=location)
        for photo in photos:
            pictures[-1].append(photo)
    return render(request, 'travels/detail_day.html',{
        'day' : date,
        'locations': locations,
        'photos' : pictures
    })