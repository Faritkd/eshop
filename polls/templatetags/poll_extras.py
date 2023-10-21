from django import template
from jalali_date import date2jalali, datetime2jalali

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


# @register.filter(name='show_jalali_date')
# def show_jalali_date(value):
#     return date2jalali(value)


@register.filter(name='show_jalali_time')
def show_jalali_time(value):
    return datetime2jalali(value)