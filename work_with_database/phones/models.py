from django.db import models
from django.utils.text import slugify

from autoslug import AutoSlugField




class Phone(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Модель телефона')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(max_length=100)
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = AutoSlugField(populate_from='name')
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)


