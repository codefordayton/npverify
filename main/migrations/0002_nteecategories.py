# Generated by Django 4.0.7 on 2022-09-03 13:26

from django.db import migrations
import csv

def import_ntee_categories(apps, schema_editor):
    NTEECategory = apps.get_model('main', 'NTEECategory')
    with open('main/data/nteecategories.csv') as csvfile:
        reader = csv.DictReader(csvfile,
            ['category', 'name', 'description'])
        for row in reader:
            print(row['category'], row['name'])
            nc = NTEECategory(
                category=row['category'],
                name=row['name'],
                description=row['description'])
            nc.save()

def remove_ntee_categories(apps, schema_editor):
    NTEECategory = apps.get_model('main', 'NTEECategory')
    NTEECategory.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_ntee_categories, remove_ntee_categories)
    ]