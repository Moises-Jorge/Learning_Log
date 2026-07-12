from django.urls import path
from .views import IndexView, TopicsView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('topics', TopicsView.as_view(), name='topics'),
]

