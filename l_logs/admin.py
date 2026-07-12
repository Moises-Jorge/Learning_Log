from django.contrib import admin
from .models import TopicModel, AnnotationModel

admin.site.register(TopicModel)
admin.site.register(AnnotationModel)
