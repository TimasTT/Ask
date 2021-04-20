from django.contrib.auth.models import UserManager
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings


class User(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')
    birth_date = models.DateField()

    objects = UserManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class QuestionManager(models.Manager):
    def only_question(self, id):
        return self.filter(id = id)

class Qstion(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey('User', on_delete=models.CASCADE)

    tag = models.ManyToManyField('Tags')

    objects = QuestionManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class AnswerManager(models.Manager):
    def only_question(self, id):
        return self.filter(id = id)


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    question = models.ForeignKey('Qstion', on_delete=models.CASCADE)

    objects = AnswerManager()

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answer'


class Tags(models.Model):
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class LikeQuestions(models.Model):

    question = models.ForeignKey('Qstion', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)


