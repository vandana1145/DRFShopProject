from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, default='None')
    slug = models.SlugField(max_length=255, unique=True, default='None')


    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['-id']


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("category_detail", kwargs={"pk": self.pk})

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    product = models.CharField(max_length=100, verbose_name='product', default='Nil')
    product_image = models.ImageField(upload_to="product_images", blank=True)
    description = models.TextField(blank=True, verbose_name='description')
    size = models.CharField(max_length=4, verbose_name='size', blank=True)
    price = models.FloatField(blank=True, verbose_name='price', default=0)
    slug = models.SlugField(max_length=255, default='None')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated =models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)


    def __str__(self):
        return (self.product)
        # return '%d: %s' %(self.product, self.description)

    def __str__(self):
        return str(self.price)
    

    # def get_absolute_url(self):
    #     return reverse("product_detail", kwargs={"pk": self.pk})
    