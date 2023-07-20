from django.shortcuts import render, get_object_or_404
from .models import Topic,Question

def topic_view(request):
    topicsdata = Topic.objects.all()
    context = {'topicsdata': topicsdata}
    template_name = 'topicsdata.html'
    return render(request, template_name, context)

def question_view(request, pk):
    topicdata = get_object_or_404(Topic, link = pk)
    #print(topicdata)
    return render(request, 'questiondata.html', {'topicdata':topicdata})

def answer_view(request, pk,ck):
    #topicdata = get_object_or_404(Topics, pk = pk)
    questiondata = get_object_or_404(Question, pk = ck)
    return render(request, 'answerdata.html', {'questiondata':questiondata})
#    return render(request, template_name, context)