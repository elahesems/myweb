# Generated by Django 3.1.1 on 2020-09-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='catname',
            field=models.CharField(choices=[('book', 'book'), ('football', 'football'), ('science', 'science'), ('general', 'general')], default='general', max_length=50),
        ),
    ]