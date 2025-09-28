from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    roles = models.ManyToManyField('Role', blank=True, related_name='users')
    # 解决历史冲突问题
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permission_set',
        blank=True
    )

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='roles'
    )
    desc = models.TextField(null=True)


class Permission(models.Model):
    TYPE_CHOICES = [
        ('directory', '目录'),
        ('menu', '菜单'), 
        ('button', '按钮')
    ]
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
