from django.db import models


class User(models.Model):

    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"<User> email: {self.email} \n username: {self.username} \n phone: {self.phone} "


class Service(models.Model):

    CHOICES = (
        ('DOG WALKER', 'DOG WALKER'),
        ('DOG SITTER', 'DOG SITTER'),
        ('CAT SITTER', 'CAT SITTER')
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    type = models.CharField(max_length=100, choices=CHOICES)

    def __str__(self):
        return f"<Service> name: {self.name} \n description: {self.description}" \
               f" \n price: {self.price} \n type: {self.type}"


class Order(models.Model):

    user_id = models.IntegerField()
    service_id = models.IntegerField()
    order_date = models.DateTimeField()

    def __str__(self):
        return f"<Order> user_id: {self.user_id} \n service_id: {self.service_id}"
