from django.db import models


# Create your models here.
# noinspection PyUnreachableCode
class Book(models.Model):
    title = models.CharField('Book_name', max_length=50, default=" ")
    price = models.DecimalField("price", max_digits=8, decimal_places=3)
    info = models.CharField("INFO", max_length=100, default="")
    market_price = models.DecimalField("mark_price", max_digits=8, decimal_places=3, default=0)
    pub = models.CharField('Public', max_length=50, default=" ")
    is_activate = models.BooleanField('is activate or not', default=True)

    class Meta:
        db_table = "book"
        verbose_name = "书名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%s_%s_%s' % (self.title, self.price, self.pub, self.market_price)


class Author(models.Model):
    name = models.CharField("Name", max_length=11, default="")
    age = models.IntegerField("Age", default=0)
    email = models.EmailField("Email", default=0)

    class Meta:
        db_table = "author"
        verbose_name = "作者名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Wife(models.Model):
    name = models.CharField("Wife", max_length=50)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = "Wife"
        verbose_name = "老婆"
        verbose_name_plural = verbose_name
