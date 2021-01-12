# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=150)
    mail = models.EmailField(max_length=250)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)

    def __str__(self):
        return self.name
