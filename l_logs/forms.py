from django import forms
from .models import TopicModel, AnnotationModel

class TopicForm(forms.ModelForm):
    class Meta:
        model = TopicModel
        fields = ['title']
        labels = {'title': ''}

class AnnotationForm(forms.ModelForm):
    class Meta:
        model = AnnotationModel
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
