from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Type"
        verbose_name_plural = "User Types"
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user_type = models.ForeignKey(UserTypes, on_delete=models.CASCADE, related_name="users")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Milestones(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    next_milestone = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_milestones'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Milestone"
        verbose_name_plural = "Milestones"
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class RoadTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Road Type"
        verbose_name_plural = "Road Types"
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Roads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    road_type = models.ForeignKey(RoadTypes, on_delete=models.CASCADE, related_name="roads")
    contractor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="contracted_roads")
    engineer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="engineered_roads")
    milestone = models.ForeignKey(Milestones, on_delete=models.CASCADE, related_name="roads",null=True, blank=True)
    isUploadedProof = models.BooleanField(default=False)
    engineerMessage = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Road"
        verbose_name_plural = "Roads"
        ordering = ['-date_created']

    def __str__(self):
        return self.name
