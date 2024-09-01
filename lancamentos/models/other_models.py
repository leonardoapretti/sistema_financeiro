from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Type(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Modality(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
