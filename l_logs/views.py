from django.shortcuts import render
from django.views.generic import View
from .models import TopicModel, AnnotationModel

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
