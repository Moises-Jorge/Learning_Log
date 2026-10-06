from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .models import TopicModel, AnnotationModel
from .forms import TopicForm, AnnotationForm

class IndexView(View):
	def get(self, request):
		return render(request, 'l_logs/index.html')

class TopicsView(LoginRequiredMixin, View):
    def get(self, request):
        topics = TopicModel.objects.filter(owner=request.user).order_by('date_added')
        context = {
			'topics': topics,
		}
        return render(request, 'l_logs/topics.html', context)

class TopicView(LoginRequiredMixin, View):
    def get(self, request, topic_id):
        topic = TopicModel.objects.get(id = topic_id)
        if (topic.owner != request.user):
            raise Http404
        annotations = topic.annotations.order_by('-date_added')
        context = {
			'topic': topic,
			'annotations': annotations,
		}
        return render(request, 'l_logs/topic.html', context)

class NewTopicView(LoginRequiredMixin, View):
    def get(self, request):
        form = TopicForm()
        context = {
			'form': form,
		}
        return render(request, 'l_logs/new_topic.html', context)

    def post(self, request):
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('topics')
        context = {
			'form': form,
		}
        return render(request, 'l_logs/new_topic.html', context)

class NewAnnotationView(LoginRequiredMixin, View):
    def get(self, request, topic_id):
        topic = TopicModel.objects.get(id = topic_id)
        if (topic.owner != request.user):
            raise Http404
        form = AnnotationForm()
        context = {
            'topic': topic,
            'form': form,
        }
        return render(request, 'l_logs/new_annotation.html', context)

    def post(self, request, topic_id):
        topic = TopicModel.objects.get(id = topic_id)
        if (topic.owner != request.user):
            raise Http404
        form = AnnotationForm(data=request.POST)
        if form.is_valid():
            new_annotation = form.save(commit=False)
            new_annotation.topic_id = topic
            new_annotation.save()
            return redirect('topic', topic_id)
        context = {
            'topic': topic,
            'form': form,
        }
        return render(request, 'l_logs/annotation.html', context)


class EditAnnotation(LoginRequiredMixin, View):
    def get(self, request, annotation_id):
        annotation = AnnotationModel.objects.get(id = annotation_id)
        topic = annotation.topic_id
        if (topic.owner != request.user):
            raise Http404
        form = AnnotationForm(instance=annotation)
        context = {
            'annotation': annotation,
            'topic': topic,
            'form': form
        }
        return render(request, 'l_logs/edit_annotation.html', context)

    def post(self, request, annotation_id):
        annotation = AnnotationModel.objects.get(id = annotation_id)
        topic = annotation.topic_id
        if (topic.owner != request.user):
            raise Http404
        form = AnnotationForm(instance=annotation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('topic', topic.id)
        context = {
            'annotation': annotation,
            'topic': topic,
            'form': form,
        }
        return render(request, 'l_logs/edit_annotation.html', context)

