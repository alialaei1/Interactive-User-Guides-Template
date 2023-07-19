from django.shortcuts import render, get_object_or_404
from .models import Devices,Question

def device_view(request):
    devicesdata = Devices.objects.all()
    context = {'devicesdata': devicesdata}
    template_name = 'devicedata.html'
    return render(request, template_name, context)

def question_view(request, pk):
    devicedata = get_object_or_404(Devices, link = pk)
    #print(devicedata)
    return render(request, 'questiondata.html', {'devicedata':devicedata})

def answer_view(request, pk,ck):
    #devicedata = get_object_or_404(Devices, pk = pk)
    questiondata = get_object_or_404(Question, pk = ck)
    return render(request, 'answerdata.html', {'questiondata':questiondata})
#    return render(request, template_name, context)