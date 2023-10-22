from django.db import models
from jalali_date import date2jalali, datetime2jalali
from account_module.models import User


# Create your models here.


class ArticleCategory(models.Model):
    parent = models.ForeignKey(to='ArticleCategory', on_delete=models.CASCADE, null=True ,blank=True ,verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله '
        verbose_name_plural = 'دسته بندی های مقاله'


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/article', verbose_name='تصویر مقاله')
    short_description = models.TextField(verbose_name='توضیحات مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    selected_categories = models.ManyToManyField(to='ArticleCategory', verbose_name='دسته بندی ها')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
