# Generated by Django 4.2.1 on 2024-05-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_payment_payment_link_payment_session_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="Сумма"),
        ),
    ]
