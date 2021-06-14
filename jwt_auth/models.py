from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     is_student = models.BooleanField('student status', default=False)
#     is_teacher = models.BooleanField('teacher status', default=False)


class User(AbstractUser):
    
    email = models.CharField(max_length=50)
    profile_image = models.CharField(max_length= 250 , default=" https://www.clipartkey.com/mpngs/m/152-1520367_user-profile-default-image-png-clipart-png-download.png")
    STUDENT='Student'
    TEACHER ='Teacher'
    USER_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
    )
    PIANO='Piano'
    DRUMS ='Drums'
    TIMPANI ='Timpani'
    XYLOPHONE ='Xylophone'
    CORNET = 'Cornet'
    TUBA ='Tuba'
    TROMBONE ='Trombone'
    FRENCH_HORN ='French Horn'
    TRUMPET ='Trumpet'
    SAXOPHONE ='Saxophone'
    BASSOON ='Bassoon'
    CLARINET ='Clarinet'
    OBOE ='Oboe'
    FLUTE ='Flute'
    GUITAR ='Guitar'
    HARP ='Harp'
    DOUBLE_BASS ='Double Bass'
    CELLO ='Cello'
    VIOLA ='Viola'
    VIOLIN ='Violin'
    INSTRUMENT_TYPE_CHOICES = [
        (PIANO, 'Piano'),
        (DRUMS, 'Drums'),
        (TIMPANI, 'Timpani'),
        (XYLOPHONE, 'Xylophone'),
        (CORNET,  'Cornet'),
        (TUBA, 'Tuba'),
        (TROMBONE, 'Trombone'),
        (FRENCH_HORN, 'French Horn'),
        (TRUMPET, 'Trumpet'),
        (SAXOPHONE, 'Saxophone'),
        (BASSOON, 'Bassoon'),
        (CLARINET, 'Clarinet'),
        (OBOE, 'Oboe'),
        (FLUTE, 'Flute'),
        (GUITAR, 'Guitar'),
        (HARP, 'Harp'),
        (DOUBLE_BASS, 'Double Bass'),
        (CELLO, 'Cello'),
        (VIOLA, 'Viola'),
        (VIOLIN, 'Violin'),
    ]
    instrument_type = models.CharField(
        max_length=15,
        choices=INSTRUMENT_TYPE_CHOICES,
    )
    LONDON = 'London'
    MANCHESTER= 'Manchester'
    BIRMINGHAM = 'Birmingham'
    LIVERPOOL = 'Liverpool'
    LEEDS = 'Leeds'
    NEWCASTLE = 'Newcastle'
    EDINBURGH = 'Edinburgh'
    GLASGOW = 'Glasgow'
    CAMBRIDGE = 'Cambridge'
    BRISTOL = 'Bristol'
    CARDIFF = 'Cardiff'
    BELFAST = 'Belfast'
    YORK = 'York'
    SHEFFIELD = 'Sheffield'
    LOCATION_TYPE_CHOICES = [
        (LONDON, 'London'),
        (MANCHESTER, 'Manchester'),
        (BIRMINGHAM, 'Birmingham'),
        (LIVERPOOL, 'Liverpool'),
        (LEEDS, 'Leeds'),
        (NEWCASTLE, 'Newcastle'),
        (EDINBURGH, 'Edinburgh'),
        (GLASGOW, 'Glasgow'),
        (CAMBRIDGE, 'Cambridge'),
        (BRISTOL, 'Bristol'),
        (CARDIFF, 'Cardiff'),
        (BELFAST, 'Belfast'),
        (YORK, 'York'),
        (SHEFFIELD, 'Sheffield')
    ]
    location_type_choices = models.CharField(
        max_length=15,
        choices=LOCATION_TYPE_CHOICES
        )
