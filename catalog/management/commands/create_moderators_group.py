from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создание группы "Модератор продуктов" с разрешениями'

    def handle(self, *args, **kwargs):
        Group.objects.all().delete()

        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        delete_permission = Permission.objects.get(codename='delete_product')
        can_unpublish_product = Permission.objects.get(codename='can_unpublish_product')

        group.permissions.add(can_unpublish_product, delete_permission)

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана'))
        else:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" уже существует'))
