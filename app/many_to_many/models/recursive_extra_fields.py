"""
인스타그램 사용자
"""

from django.db import models

class FaceBookUser(models.Model):
    name = models.CharField(max_length=20)
    friends = models.ManyToManyField('self')

    def __str__(self):
        return self.name

class InstagramUser(models.Model):
    name = models.CharField(max_length=20)
    following = models.ManyToManyField(
        'self',
        through='Relation',
        related_name='followers',
        symmetrical=False,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Relation(models.Model):
    me = models.ForeignKey(
        InstagramUser, related_name='me_relation_set', on_delete=models.CASCADE)
    counterpart = models.ForeignKey(
        InstagramUser, related_name='counterpart_relation_set', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Relation (me: {self.me.name}, counterpart: {self.counterpart.name})'