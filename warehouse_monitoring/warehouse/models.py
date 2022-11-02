from datetime import datetime

from django.db import models
import pandas as pd
from django.db.models import F


class EcxelFile(models.Model):
    file = models.FileField('Файл')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        record_parts_from_excel_to_db(self.file.path)


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


def record_parts_from_excel_to_db(path):
    df = read_excel(path)
    record_names_from_excel_to_db(df)
    record_count_from_excel_to_db(df)


def read_excel(excel_filename):
    df = pd.read_excel(excel_filename,
                       skiprows=8,
                       skipfooter=1,
                       header=None,
                       names=['name', 'count', 'sum'])
    df = df.fillna(0)
    return df


def record_names_from_excel_to_db(df):
    part = []
    part_name_1c = []

    for _, row in df.iterrows():
        part_name_1c.append(row['name'])

    part_name_bd = Part.objects.all().values_list('name', flat=True)
    part_name_add = set(part_name_1c) - set(part_name_bd)
    if part_name_add:
        for name in part_name_add:
            part.append(Part(name=name))
        objs = Part.objects.bulk_create(part)


def record_count_from_excel_to_db(df):
    part = []
    part_bd = Part.objects.all().values()
    for i in part_bd:
        for _, row in df.iterrows():
            if row['name'] == i['name']:
                part.append(Part(i['id'], i['name'], row['count']))
    objs = Part.objects.bulk_update(part, ['count'])


def create_order():
    return Order.objects.create(created_at=datetime.today())



def create_parts_order():
    tracking_part = TrackingPart.objects.all()
    part = Part.objects.all()
    order = create_order()

    for row_tracking_part in tracking_part:
        for row_part in part:
            if row_tracking_part.part_id == row_part.id and \
                    row_part.count < row_tracking_part.min_count:
                OrderItem.objects.create(part=row_part, count=row_tracking_part.order_count, order=order)

F
