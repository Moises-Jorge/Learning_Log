from django.urls import path
from .views import IndexView, TopicsView, NewTopicView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('topics', TopicsView.as_view(), name='topics'),
	path('new_topic', NewTopicView.as_view(), name='new_topic'),
]

