from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from opsadmin.models import Cloudhost
from django.template import RequestContext, loader
# Create your views here.
def index(request):
    latest_question_list = Cloudhost.objects.order_by('-date')
 #   template = loader.get_template('opsadmin/index.html')
 #   context = RequestContext(request, {'latest_question_list':latest_question_list,})
 #   return HttpResponse(template.render(context))
    context = {'latest_question_list': latest_question_list}
    return render(request, 'opsadmin/index.html', context)


def detail(request, name_id):
#    try:
#        name = Cloudhost.objects.get(name = name_id)
#    except Cloudhost.DoesNotExist:
#        raise Http404("Name does not exist")
#    return render(request, 'opsamdin/detail.html', {'name': name})
    name = get_object_or_404(Cloudhost, pk=name_id)
    return render(request, 'opsadmin/detail.html', {'name': name})

