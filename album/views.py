from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from album.models import Category, Photo


class PhotoListView(ListView):
    model = Photo



class ProtoDetailView(DetailView):
    model = Photo



def first_view(request):
    return HttpResponse("<h1 align='center'>Hola DJango</h1>")

def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'album/category_list.html', context)

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request, 'album/category_detail.html', context)
