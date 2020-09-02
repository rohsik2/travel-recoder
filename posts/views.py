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
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            loc = form.save(commit=False)
            loc.travel = get_object_or_404(Travel, id=id)
            loc.save()
            return redirect('detail', id=loc.travel.pk)
    else:
        form = LocationForm()
    travel = get_object_or_404(Travel, id=id)
    Locations = TravelLocation.objects.filter(travel=travel).order_by('-day')
    images = []
    for location in Locations:
        images.append(
            TravelLocationImage.objects.filter
            (TravelLocation=location)
        )
    return render(request, 'travels/detail.html', {
        'travel':travel,
        'locations':Locations,
        'images':images,
        'form': form
    })