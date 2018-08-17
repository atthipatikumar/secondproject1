from django.db import models

class Register(models.Model):
    id = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Emailid = models.EmailField(max_length=250)
    Password = models.IntegerField(max_length=20)
    class Meta:
        db_table = 'register'
        app_label = 'secondproject'

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    order_item = models.TextField(max_length=250)
    order_date = models.DateTimeField(auto_now = False, auto_now_add = True)
    order_delivery = models.DateField(auto_now = False, auto_now_add = True)
    class Meta:
        db_table = 'orders'
        app_label = 'secondproject'
