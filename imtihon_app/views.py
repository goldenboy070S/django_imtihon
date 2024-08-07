from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    category = Category.objects.all()
    rasm = Photos.objects.all().order_by('-id')
    return render(request, 'index.html', {'category': category, 'rasm': rasm})

def category_photo(request, c_id):
    category = Category.objects.get(id=c_id)
    photos = Photos.objects.filter(category=category)
    return render(request, 'category_photo.html', {'photos': photos})

def detail(request, id):
    photo = Photos.objects.get(id=id)
    if not request.session.get('photo'):
        request.session['photo'] = []
        request.session['photo'].append(photo.id)
        photo.views += 1
        
    if photo.id not in request.session['photo']:
        photo.views += 1
    photo.save()
    return render(request, 'details.html', {'photo': photo})
