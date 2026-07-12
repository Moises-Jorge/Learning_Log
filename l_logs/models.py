from django.db import models

class TopicModel(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topics'

    def __str__(self)->str:
        return self.title

class AnnotationModel(models.Model):
    topic_id = models.ForeignKey(TopicModel, on_delete=models.CASCADE, related_name='annotations')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'annotations'

    def __str__(self)->str:
        return self.text[:50] + '...'
