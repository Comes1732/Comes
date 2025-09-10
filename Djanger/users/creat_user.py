import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from users.models import User, Role, Permission
from Djanger.users.models import User, Role, Permission

from django.contrib.auth.hashers import make_password

def create_superuser():
    # 1. 创建超级管理员角色
    admin_role, created = Role.objects.get_or_create(
        name='超级管理员',
        defaults={'desc': '拥有系统所有权限'}
    )

    # 2. 创建管理员用户
    admin_user = User.objects.create(
        username='admin',
        password=make_password('admin123'),  # 密码需加密
        email='admin@example.com',
        is_staff=True,
        is_superuser=True
    )

    # 3. 关联角色
    admin_user.roles.add(admin_role)
    print(f"管理员创建成功!\n用户名: admin\n密码: admin123")

if __name__ == '__main__':
    create_superuser()
