from django.shortcuts import render
from django.http import HttpResponse

from .models import Nonprofit

# Create your views here.
def index(request):
    nonprofits = Nonprofit.objects.all().filter(needs_review=None)[:3]
    context = {'nonprofits': nonprofits}
    return render(request, 'main/index.html', context)

def detail(request, nonprofit_id):
    nonprofit = Nonprofit.objects.get(id=nonprofit_id)
    return HttpResponse(f"hello detail {nonprofit.name}")

def results(request, nonprofit_id):
    return HttpResponse(f"hello results {nonprofit_id}")

def review(request, nonprofit_id):
    return HttpResponse(f"hello review {nonprofit_id}")
