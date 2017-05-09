# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 04:26
from __future__ import unicode_literals

from django.db import migrations


def convert_venuegroup_to_venuecategory(apps, schema_editor):
    """Creates a VenueCategory for each VenueGroup.
    VenueCategory instances derived from VenueGroup will have
    "display in venue name" set to "prefix", and "display in public tooltip"
    set to False."""

    VenueGroup = apps.get_model("venues", "VenueGroup")
    VenueCategory = apps.get_model("venues", "VenueCategory")

    for group in VenueGroup.objects.all():
        category = VenueCategory()
        category.name = group.short_name
        category.description = group.name
        category.display_in_venue_name = 'P'
        category.display_in_public_tooltip = False
        category.save()
        category.venues.set(group.venue_set.all())
        category.save()


def delete_all_venuecategories(apps, schema_editor):
    VenueCategory = apps.get_model("venues", "VenueCategory")
    VenueCategory.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0016_venuecategory'),
    ]

    operations = [
        migrations.RunPython(
            convert_venuegroup_to_venuecategory,
            reverse_code=delete_all_venuecategories,
        ),
    ]
