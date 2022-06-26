from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30) # 30자짜리 문자열을 저장할 수 있는 title이라는 속성을 선언
    content = models.TextField(null=True) # 문자열 길이 정하지 않고 긴 문자열 쓸 때 사용

    created_at = models.DateTimeField(auto_now_add=True) # 이 스키마를 따르는 게시글이 등록되면 자동으로 현재시간이 나옴
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때

    # num_stars = models.IntegerField() -> 숫자 필드는 이렇게 적용!

# content = models.TextField()