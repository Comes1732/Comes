
from django.db import models
from django.contrib.auth.models import AbstractUser

class Menu(models.Model):
    """一级菜单表(数据库备注：存储系统一级导航菜单)"""
    title = models.CharField(max_length=32, verbose_name='菜单名称', help_text='显示的一级菜单名称')
    icon = models.CharField(max_length=64, null=True, blank=True, verbose_name='图标类名', 
                          help_text='FontAwesome图标类名，如fa-user')
    order = models.IntegerField(default=0, verbose_name='排序权重', 
                              help_text='菜单显示顺序，数字越大越靠前')

    class Meta:
        db_table = 'rbac_menu'
        verbose_name = '菜单管理'
        verbose_name_plural = verbose_name
        ordering = ['-order']

    def __str__(self):
        return self.title

class PermissionGroup(models.Model):
    """权限分组表(数据库备注：权限功能分组，用于界面展示)"""
    name = models.CharField(max_length=32, verbose_name='组名称')
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, 
                           verbose_name='所属菜单', db_constraint=False,  # 逻辑外键
                           help_text='关联的一级菜单ID')
    
    class Meta:
        db_table = 'rbac_permission_group'
        verbose_name = '权限分组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Permission(models.Model):
    """权限表(数据库备注：存储系统所有权限点)"""
    title = models.CharField(max_length=32, verbose_name='权限名称')
    url = models.CharField(max_length=255, verbose_name='URL路径', 
                         help_text='含正则的URL路径，如^/user/list/$')
    code = models.CharField(max_length=32, verbose_name='权限编码', 
                          help_text='权限唯一标识，如user_add')
    group = models.ForeignKey(PermissionGroup, on_delete=models.SET_NULL, null=True,
                            verbose_name='权限分组', db_constraint=False)  # 逻辑外键
    pid = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                          verbose_name='父权限', db_constraint=False,  # 逻辑自关联
                          help_text='非空表示二级菜单权限')

    class Meta:
        db_table = 'rbac_permission'
        verbose_name = '权限管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Role(models.Model):
    """角色表(数据库备注：角色与权限多对多关系)"""
    name = models.CharField(max_length=32, verbose_name='角色名称')
    desc = models.TextField(null=True, blank=True, verbose_name='角色描述')
    permissions = models.ManyToManyField(Permission, blank=True, 
                                       verbose_name='拥有权限',
                                       through='RolePermissionRelation',  # 自定义中间表
                                       through_fields=('role', 'permission'))

    class Meta:
        db_table = 'rbac_role'
        verbose_name = '角色管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class RolePermissionRelation(models.Model):
    """角色-权限中间表(数据库备注：解决逻辑外键的中间关系)"""
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_constraint=False)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, db_constraint=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rbac_role_permission_relation'
        unique_together = (('role', 'permission'),)

class User(AbstractUser):
    """用户表(继承Django原生用户表)"""
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    roles = models.ManyToManyField(Role, blank=True, verbose_name='拥有角色',
                                 through='UserRoleRelation',  # 自定义中间表
                                 through_fields=('user', 'role'))

    class Meta:
        db_table = 'rbac_user'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

class UserRoleRelation(models.Model):
    """用户-角色中间表(数据库备注：解决逻辑外键的中间关系)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_constraint=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rbac_user_role_relation'
        unique_together = (('user', 'role'),)
