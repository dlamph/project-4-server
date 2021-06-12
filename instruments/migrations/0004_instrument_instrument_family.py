# Generated by Django 3.2.4 on 2021-06-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0003_remove_instrument_instrument_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='instrument_family',
            field=models.CharField(choices=[('Strings', 'Strings'), ('Woodwind', 'Woodwind'), ('Brass', 'Brass'), ('Percussion', 'Percussion'), ('Keyboards', 'Keyboards')], default='brass', max_length=50),
            preserve_default=False,
        ),
    ]
