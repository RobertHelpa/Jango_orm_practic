import django_setup

from user_and_roles.models import Role, User

role_admin = Role(role_type = "admin")
role_admin.save()

role_admin = Role.objects.create(role_type='user')

admin = User.objects.get_or_create(
    name = 'Johnny',
    email = 'bigjohn@gmail.com',
    role = role_admin
)

user = User.objects.get_or_create(
    name = 'Billy',
    email = 'jsutbilly@gmail.com',
    role = role_admin
)