import random

import pandas as pd

from warehouse.models import Part
from warehouse.views import TrackedPartViewSet


# def create_random_part():
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     part_name = ''
#     for i in range(4):
#         n = random.randint(0, 25)
#         part_name += alphabet[n]
#     return PartBalance.objects.create(name=part_name, count=n)
#
#
# def set_zero_count(part):
#     part.count = 0
#     part.save()
#
#
# def get_by_id(part_id):
#     return PartBalance.objects.get(pk=part_id)
#
#
# def get_by_id_v2(part_id):
#     return PartBalance.objects.filter(pk=part_id)[0]
#
#
# def delete_part(updated_part):
#     updated_part.delete()

def record_parts_from_excel_to_db():
    df = read_excel('/home/evgeniy/Рабочий стол/Остатки товаров.xlsx')
    record_names_from_excel_to_db(df)
    record_count_from_excel_to_db(df)


def read_excel(excel_filename):
    df = pd.read_excel(excel_filename,
                       skiprows=8,
                       skipfooter=1,
                       header=None,
                       names=['name', '', 'count', 'sum'])
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
