from django.shortcuts import render, redirect
from django.views.generic import View
from .models import TopicModel, AnnotationModel
from .forms import TopicForm, AnnotationForm

class IndexView(View):
	def get(self, request):
		return render(request, 'l_logs/index.html')

class TopicsView(View):
    def get(self, request):
        topics = TopicModel.objects.order_by('date_added')
        context = {
			'topics': topics,
		}
        return render(request, 'l_logs/topics.html', context)

class TopicView(View):
    def get(self, request, topic_id):
        topic = TopicModel.objects.get(id = topic_id)
        annotations = topic.annotations.order_by('-date_added')
        context = {
			'topic': topic,
			'annotations': annotations,
		}
        return render(request, 'l_logs/topic.html', context)

class NewTopicView(View):
    def get(self, request):
        form = TopicForm()
        context = {
			'form': form,
		}
        return render(request, 'l_logs/new_topic.html', context)

    def post(self, request):
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')
        context = {
			'form': form,
		}
        return render(request, 'l_logs/new_topic.html', context)
