from django.contrib.auth.models import Group


def new_user_handler(backend, user, response, *args, **kwargs):
    user.groups.add(Group.objects.get(name="read_only"))
