from django.db import models

class BaseUser(models.Model):
    is_superuser = models.BooleanField(default=False)

    objects = models.Manager()

    def show_pk(self):
        print(self.pk)


class NormalUser(BaseUser):
    class Meta:
        proxy = True

# SuperUser모델에서 사용할 Manager
class SuperUserManager(models.Manager):
    def get_queryset(self):
        # 기본 Queryset을 제한
        return super().get_queryset().filter(is_superuser=True)

class SuperUser(BaseUser):
    # 프록시 모델에 Manager를 지정
    objects = SuperUserManager

    class Meta:
        proxy = True

    def delete_user(self,pk):
        BaseUser.objects.get(pk=pk).delete()