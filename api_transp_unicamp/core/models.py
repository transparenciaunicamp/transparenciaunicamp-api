from django.db import models


class Category(models.Model):
    title = models.CharField('Nome', max_length=140)
    description = models.TextField('Descrição', blank=True)
    parent = models.ForeignKey('self', null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Item(models.Model):
    title = models.CharField('Nome', max_length=140)
    description = models.TextField('Descrição', blank=True)
    category = models.ForeignKey('Category')
    value = models.FloatField('Valor')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
