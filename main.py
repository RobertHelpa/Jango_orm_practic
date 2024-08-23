import django_setup

from user_and_roles.models import Role, User
from tasks

role_admin = Role.objects.create(role_type='admin')[0]
role_user = Role.objects.create(role_type='user')[0]

admin = User.objects.get_or_create(
    name = 'Johnny',
    email = 'bigjohn@gmail.com',
    role = role_admin
)[0]

user = User.objects.get_or_create(
    name = 'Billy',
    email = 'jsutbilly@gmail.com',
    role = role_admin
)[0]

status_in_progress = Status.objocts.get_or_create

task1 = Task.objects.get_or_create(
    title = "погодувати кота",
    description = "",
    user = admin
)