from django.urls import path
from .views import IndexView, TopicsView, TopicView, NewTopicView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('topics', TopicsView.as_view(), name='topics'),
	path('topics/<topic_id>', TopicView.as_view(), name='topic'),
	path('new_topic', NewTopicView.as_view(), name='new_topic'),
]

