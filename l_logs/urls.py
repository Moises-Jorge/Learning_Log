from django.urls import path
from .views import IndexView, TopicsView, TopicView, NewTopicView, NewAnnotationView, EditAnnotation

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('topics', TopicsView.as_view(), name='topics'),
	path('topics/<topic_id>', TopicView.as_view(), name='topic'),
	path('new_topic', NewTopicView.as_view(), name='new_topic'),
	path('new_annotation/<topic_id>', NewAnnotationView.as_view(), name='new_annotation'),
	path('edit_annotation/<annotation_id>', EditAnnotation.as_view(), name='edit_annotation'),
]

