from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from .models import futureblog, Comment

def index(request):
    latest_futureblog_list = futureblog.objects.order_by('-pub_date')[:10]
    return render(request, 'futureblog/list.html', {'latest_futureblog_list': latest_futureblog_list})

def detail(request, futureblog_id):
    try:
        a = futureblog.object.get( id = futureblog_id )
    except:
        raise Http404('Статья не найдена!')

    return render(request, 'futureblog/detail.html', {'futureblog': a})

def leave_comment(request, futureblog_id):
    try:
        a = futureblog.object.get( id = futureblog_id )
    except:
        raise Http404('Статья не найдена!')
    a.comment_set.create(autor_name = request.POST['name'], comment_text = reauest.POST['text'])
    return HttpResponseRedirect( reverse('futureblog:detail', args = (a.id,)))