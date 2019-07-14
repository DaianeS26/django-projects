from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
import random
from .models import Restaurant
from django.db.models import Q


# Create your views here.

def index(request):
    num = None
    some_list = [
        random.randint(0, 1000000), 
        random.randint(0, 1000000),
        random.randint(0, 100000),
    ]
    condition_bool_item = True
    if condition_bool_item:
        num = random.randint(0, 100000)

    context = {
        'num': num,
        'some_list': some_list

    }
    
    return render(request, 'index.html', context)



def restaurant_listview(request):
    queryset = Restaurant.objects.all()
    context = {
        'object_list': queryset,
    }
    
    return render(request,'restaurant/restaurant_list.html', context)


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset=Restaurant.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug) 
            )
        else:
            queryset=Restaurant.objects.all()
        return queryset


class RestaurantDetailtView(DetailView):
    queryset=Restaurant.objects.all()
    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(Restaurant, pk=rest_id) 
    #     return obj


class ContactView(View):
    def get(self, request):
        context = {}
        return render(request, 'contact.html', context)

class AboutTemplateView(TemplateView):
    template_name='about.html'

