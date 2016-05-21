from django.db import models

class Institute(models.Model):
    title = models.CharField('Nome', max_length=140)
    description = models.TextField('Descrição', blank=True)
    parent = models.ForeignKey('self', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Instituto'
        verbose_name_plural = 'Institutos'

class Document(models.Model):
    title = models.CharField('Nome', max_length=140)
    description = models.TextField('Descrição', blank=True)
    institute = models.ForeignKey('Institute')
    category = models.ForeignKey('Category')
    month = models.IntegerField('Mês')
    year = models.IntegerField('Ano')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class Category(models.Model):
    title = models.CharField('Nome', max_length=140)
    description = models.TextField('Descrição', blank=True)
    parent = models.ForeignKey('self', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Item(models.Model):
    title = models.CharField('Nome', max_length=140)
    description = models.TextField('Descrição', blank=True)
    category = models.ForeignKey('Category')
    value = models.FloatField('Valor')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'


class Transaction(models.Model):
    credit = models.ForeignKey('Item', verbose_name='Crédito', related_name='credit')
    debt = models.ForeignKey('Item', verbose_name='Débito', related_name='debt')

    def __str__(self):
        return '{} - {}'.format(str(self.credit), str(self.debt))

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
