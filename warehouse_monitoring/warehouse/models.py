from django.db import models


class EcxelFiles(models.Model):
    path = models.FileField('путь')


class Part(models.Model):
    """Описание"""
    name = models.CharField("Название детали", max_length=255, unique=True, db_index=True)
    count = models.IntegerField("Кол-во", default=0)

    def __str__(self):
        return self.name


class TrackingPart(models.Model):
    part = models.OneToOneField(Part, on_delete=models.CASCADE, primary_key=True)
    min_count = models.IntegerField("Мин. кол-во", default=0)
    order_count = models.IntegerField("Кол-во для заказа", default=0)


class Order(models.Model):
    """Описание"""  # TODO:
    created_at = models.DateField("дата заказа")


class OrderItem(models.Model):
    count = models.IntegerField("количество деталей для заказа", default=0)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)



