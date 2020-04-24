# Generated by Django 3.0.4 on 2020-04-24 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        ('votes', '0003_auto_20200420_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='articles.Article'),
        ),
    ]
