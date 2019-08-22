# Generated by Django 2.2.4 on 2019-08-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
