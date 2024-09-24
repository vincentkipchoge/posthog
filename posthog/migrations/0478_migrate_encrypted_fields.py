# Generated by Django 4.2.15 on 2024-09-16 12:46

from django.db import migrations


def re_encrypt_models(apps, schema_editor):
    for model in ["ExternalDataSource", "DataWarehouseCredential", "Integration"]:
        Model = apps.get_model("posthog", model)

        items = Model.objects.all()
        for item in items:
            item.save()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0477_datawarehouse_salesforce_order"),
    ]

    operations = [
        migrations.RunPython(re_encrypt_models, reverse_code=backwards, elidable=True),
    ]