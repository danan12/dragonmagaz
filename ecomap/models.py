from django.db import models
from django.db.models.signals import pre_save
from  django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


def pre_save_category_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        slug = slugify(instance.name, reversed=True)
        instance.slug = slug
pre_save.connect(pre_save_category_slug,sender=Category)

def image_folder(instance,filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)
class Product(models.Model):
    category = models.ForeignKey('Category',on_delete=models.PROTECT)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    avalible = models.BooleanField(default=True)
    popular = models.IntegerField(default=3)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Продукты'
        verbose_name = 'Продукт'
