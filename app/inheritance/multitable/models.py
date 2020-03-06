from django.db import models

class Place1(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80, blank=True)

    class Meta:
        verbose_name = '장소1'
        verbose_name_plural = '장소1 목록'
        ordering = ['name']

    def __str__(self):
        return self.name


class Restaurant1(Place1):
    # 명시적으로 Multi-table inheritance를 구성하는 OneToOneField를 지정
    place1_ptr = models.OneToOneField(
        Place1,
        parent_link=True,
        related_name='restaurant1',
        related_query_name='restaurant1_by_oto', on_delete=models.CASCADE
    )

    # 기본값을 사용할 경우, Place의 related_query_name이 겹칠 수 있는 ManyToManyField를 선언
    near_places = models.ManyToManyField(
        Place1,
        related_name='restaurant1_set',
        related_query_name='restaurant1_by_near_places'
    )

    hot_dogs = models.BooleanField(default=False)
    pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} (핫도그: {self.hot_dogs}, 피자: {self.pizza})'