from django.shortcuts import render
from .models import Canhoto

def canhoto_list(request):
    template_name = 'canhoto_list.html'
    objects = Canhoto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)


def canhoto_detail(request, pk):
    template_name = 'canhoto_detail.html'
    obj = Canhoto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def canhoto_add(request):
    template_name = 'canhoto_form.html'
    return render(request, template_name)