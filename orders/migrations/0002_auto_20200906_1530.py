# Generated by Django 3.1 on 2020-09-06 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meals', '0002_auto_20200829_1722'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='waiterid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='onemealtoorder',
            name='mealid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mealsid', to='meals.meal'),
        ),
        migrations.AddField(
            model_name='onemealtoorder',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='orders.order'),
        ),
        migrations.AddField(
            model_name='check',
            name='meals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.onemealtoorder'),
        ),
        migrations.AddField(
            model_name='check',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checks', to='orders.order'),
        ),
    ]
