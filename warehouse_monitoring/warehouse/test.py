import random

from warehouse.models import TrackedPart


def create_random_part():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    part_name = ''
    for i in range(4):
        n = random.randint(0, 25)
        part_name += alphabet[n]
    return TrackedPart.objects.create(name=part_name, count=n)


def set_zero_count(part):
    part.count = 0
    part.save()


def get_by_id(part_id):
    return TrackedPart.objects.get(pk=part_id)


def get_by_id_v2(part_id):
    return TrackedPart.objects.filter(pk=part_id)[0]


def delete_part(updated_part):
    updated_part.delete()
