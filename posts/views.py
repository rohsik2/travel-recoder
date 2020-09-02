from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
    
def post_new(request):
    if request.method == "POST":
       form = TravelForm(request.POST, request.FILES)
       if form.is_valid():
           trip = form.save(commit=False)
           trip.image = form.cleaned_data['image']
           trip.start_date = form.cleaned_data['start_date']
           trip.end_date = form.cleaned_data['end_date']
           trip.save()
           return redirect('detail',id=trip.pk)
    else:
        form = TravelForm()
    return render(request, 'travels/new_travel.html', {'form': form})

def test_view(request):
    return render(request,'travels/test.html')

def travel_view(request):
    travels = Travel.objects.all()
    return render(request, 'travels/travels.html', {'travels':travels})

def detail_view(request, id):
    travel = get_object_or_404(Travel, id=id)
    days = Day.objects.filter(travel=travel).order_by('-day')
    Locations = []
    images = []
    for day in days:
        Locations.append(TravelLocation.objects.filter(day=day))
        for location in Locations[-1]:
            images.append(TravelLocationImage.objects.filter(TravelLocation=location))
    return render(request, 'travels/detail.html', {
        'travel':travel,
        'days' : days,
        'locations':Locations,
        'images':images
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