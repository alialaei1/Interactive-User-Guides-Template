from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    link = models.IntegerField(unique=True)
    image = models.ImageField(upload_to ='uploads')
    def __str__(self):
        return f"{self.topic_name}"


class Question(models.Model):
    topic_name = models.ForeignKey(
            Topic,
            related_name='questions',
            on_delete=models.CASCADE,
        )
    Question = models.CharField(max_length=255)
    Qdescription = models.TextField( blank=True)
    Qimage = models.ImageField(upload_to ='uploads')

    class Meta:
        unique_together = ('topic_name', 'Question')

    def __str__(self):
        return f" {self.topic_name} Topics - {self.Question}"


class Answer(models.Model):
    questionname = models.ForeignKey(
            Question,
            related_name='answer',
            on_delete=models.CASCADE,
        )
    Qcontent = RichTextUploadingField()
    def __str__(self):
        return f"{self.questionname}'s Answer"
