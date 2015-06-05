from django.db import models

class Target_Group(models.Model):
    group_name = models.CharField(max_length=50)
    group_desc = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')

class Target_Tags(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_desc = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')

class Target(models.Model):
    target_entry = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

