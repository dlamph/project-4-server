from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    STRINGS = 'Strings'
    WOODWIND = 'Woodwind'
    BRASS = 'Brass'
    PERCUSSION = 'Percussion'
    KEYBOARDS = 'Keyboards'
    INSTRUMENT_FAMILY = [
        (STRINGS, 'Strings'),
        (WOODWIND, 'Woodwind'),
        (BRASS, 'Brass'),
        (PERCUSSION, 'Percussion'),
        (KEYBOARDS, 'Keyboards'),
    ]
    instrument_family = models.CharField(
    max_length=50,
    choices=INSTRUMENT_FAMILY,
    )
    image = models.CharField(max_length=250)
    media = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.name}'
      