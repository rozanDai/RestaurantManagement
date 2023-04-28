# Generated by Django 4.1.7 on 2023-04-28 16:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ForkAndKnife", "0009_remove_order_bill_remove_order_order_items_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Billing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_method", models.CharField(max_length=50)),
                ("payment_status", models.CharField(max_length=50)),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("billed_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_address", models.CharField(max_length=100)),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "order_date",
                    models.DateField(default="", verbose_name=datetime.date),
                ),
                (
                    "bill",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ForkAndKnife.billing",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                ("item_price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ForkAndKnife.menu",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ForkAndKnife.order",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="order_items",
            field=models.ManyToManyField(
                through="ForkAndKnife.OrderItem", to="ForkAndKnife.menu"
            ),
        ),
        migrations.AddField(
            model_name="billing",
            name="orderr",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="ForkAndKnife.order",
            ),
        ),
    ]
