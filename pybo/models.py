from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    # 조회수를 의미하는 속성
    hits = models.PositiveIntegerField(default=0)

    # 질문 비추천 추가
    voter_negative = models.ManyToManyField(User, related_name='voter_question_nega')

    def __str__(self):
        return self.subject

    @property
    def increment_hit(self):
        self.hits += 1
        self.save()


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    # 답변 비추천 추가
    voter_negative = models.ManyToManyField(User, related_name='voter_answer_nega')