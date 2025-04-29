from django.db import models
from django.utils import timezone
# Create your models here.

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    delete_at = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    internal = models.BooleanField(default=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    delete_at = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False,  unique=True)
    duration = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    delete_at = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Personnel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length= 100, null=False, blank=False,  unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    entry_date = models.DateField(null=False, blank=False)
    group= models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    delete_at = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class CourseReceived(models.Model):
    id = models.AutoField(primary_key=True)
    completion_date = models.DateField(null=False, blank=False)
    expiration_date = models.DateField(null=False, blank=False)
    enabled_from = models.DateField(null=False, blank=False)
    enabled_to = models.DateField(null=False, blank=False)
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    delete_at = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.personnel.name} - {self.course.name}"