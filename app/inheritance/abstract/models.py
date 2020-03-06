"""
1. AbstractBaseClasses
    부모는 테이블이 없고, 자식은 테이블이 있음
2. Multitable inheritance
    부모와 자식 모두 테이블이 있음
3. Proxy model
    부모는 테이블이 있고, 자식은 테이블이 없음
"""

from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    school = models.CharField(max_length=30)

    class Meta(CommonInfo.Meta):
        verbose_name = '학생'
        verbose_name_plural = '학생목록'
        db_table = 'Abstract_Student_Table'

    def __str__(self):
        return f'{self.name} (학교: {self.school})'

class Instructor(CommonInfo):
    academy = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} (학원: {self.academy})'

class Base(models.Model):
    m2m = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_set')

    class Meta:
        abstract = True

class ChildA(Base):
    pass

class ChildB(Base):
    pass

