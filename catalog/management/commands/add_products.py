from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур (с очисткой базы)'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'categories_fixture.json')
        self.stdout.write(self.style.SUCCESS('Категории успешно загружены из фикстуры'))

        call_command('loaddata', 'products_fixture.json')
        self.stdout.write(self.style.SUCCESS('Продукты успешно загружены из фикстуры'))