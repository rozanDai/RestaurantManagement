# Generated by Django 4.1.7 on 2023-03-28 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ForkAndKnife", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="category_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ForkAndKnife.category"
            ),
        ),
    ]
