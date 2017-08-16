from testsite.baseModel import BaseModel
from django.db import models
# from catalog.models import CatalogProduct
from django.utils.crypto import get_random_string


def set_file_name(instance, filename):
    name = get_random_string(40)
    ext = filename.split('.')[-1]
    path = 'files/{}.{}'.format(name, ext)
    return path


class Provider(BaseModel):
    title = models.CharField(max_length=200, verbose_name='Поставщик')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Condition(BaseModel):
    title = models.CharField(max_length=250, verbose_name='Условие')
    desc = models.TextField(verbose_name='Описаение')
    provider = models.ForeignKey(Provider, verbose_name='Поставщик', default=None, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.provider.title, self.title)

    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условия'


class ProviderFile(BaseModel):
    provider = models.ForeignKey(Provider, verbose_name='Поставщик')
    title = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(verbose_name='Файл', upload_to=set_file_name)

    def __str__(self):
        return '{} - {}'.format(self.provider.title, self.title)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


