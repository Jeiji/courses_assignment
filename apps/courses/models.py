from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    course_name = models.CharField( max_length = 50 )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )

class Description(models.Model):
    course = models.OneToOneField( Course, on_delete = models.CASCADE, primary_key = True )
    text = models.TextField( max_length = 1000 )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )

class Comment(models.Model):
    course = models.ForeignKey( Course, on_delete = models.CASCADE )
    text = models.TextField( max_length = 1000 )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
