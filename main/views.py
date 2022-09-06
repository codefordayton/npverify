from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Nonprofit

def get_nonprofit():
    return Nonprofit.objects.all().filter(complete=False)[:1][0]

def none_check(value):
    return None if value == 'None' else value

def index(request):
    context = {'nonprofit': get_nonprofit()}
    return render(request, 'main/index.html', context)

def detail(request, nonprofit_id):
    nonprofit = get_object_or_404(Nonprofit, pk=nonprofit_id)
    context = {'nonprofit': nonprofit}
    return render(request, 'main/detail.html', context)

def review(request, nonprofit_id):
    nonprofit = get_object_or_404(Nonprofit, pk=nonprofit_id)
    nonprofit.website_url = none_check(request.POST['website_url'])
    nonprofit.facebook_url = none_check(request.POST['facebook_url'])
    nonprofit.needs_volunteers = request.POST.get('needs_volunteers', False) == 'on'
    nonprofit.needs_review = request.POST.get('needs_review', False) == 'on'
    nonprofit.review_comment = none_check(request.POST['review_comment'])
    nonprofit.complete = True
    nonprofit.save()
    messages.success(request, 'Review submitted. Thank you!')
    print(nonprofit.facebook_url)
    next_nonprofit = get_nonprofit()
    return HttpResponseRedirect(reverse('detail', args=(next_nonprofit.id,)))
