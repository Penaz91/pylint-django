"""
Checks that using save() or create() inside a for loop
raises complaints from PyLint
"""
# pylint: disable=missing-docstring,too-few-public-methods

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)  # [consider-using-bulk-create]

    class Meta:
        app_label = "test_app"


def for_create():
    for i in range(10):
        Book.objects.create(name=str(i))  # [consider-using-bulk-create]


def for_nested_if_create():
    for i in range(10):
        if i % 2 == 0:
            Book.objects.create(name=str(i))  # [consider-using-bulk-create]


def assigned_for_create():
    for i in range(10):
        _ = Book.objects.create(name=str(i))  # [consider-using-bulk-create]


def for_filter():
    for i in range(10):
        _ = Book.objects.filter(name=str(i))  # [consider-using-in-queries]
