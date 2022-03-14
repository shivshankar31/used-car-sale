from random import choices
from django.db import models
from datetime import datetime
# import datetime

# Create your models here.

class Car(models.Model):

    city_choice = (
        ('Chennai', 'Chennai'),
        ('Coimbatore', 'Coimbatore' ),
        ('Madurai', 'Madurai'),
        ('Salem', 'Salem'),
        ('Tiruppur', 'Tiruppur'),
        ('Tiruchirappalli', 'Tiruchirappalli'),
        ('Vellore', 'Vellore' ),
        ('Tirunelveli', 'Tirunelveli' ),
        ('Erode','Erode' ),
        ('Thoothukkudi', 'Thoothukkudi' ),
        ('Dindigul', 'Dindigul'),
        ('Thanjavur', 'Thanjavur'),
        ('Hosur', 'Hosur'),
        ('Sivakasi', 'Sivakasi'),
        ('Karur', 'Karur'),
        ('Udhagamandalam', 'Udhagamandalam'),
        ('Ranipet', 'Ranipet'),
        ('Nagercoil', 'Nagercoil'),

    )

    state_choice = (
        ('TN', 'TAMIL NADU'),
        ('other state', 'other state')
        
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    body_choice =(
        ('Hatchback','Hatchback'),
        ('Sedan', 'Sedan'),
        ('MUV/SUV', 'MUV/SUV'),
        ('Coupe','Coupe'),
        ('Convertible', 'Convertible'),
        ('Wagon', 'Wagon'),
        ('Van', 'Van'),
        ('Jeep','Jeep'),
    )

    trasmission_choice = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    fuel_choice = ( 
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'), 
        ('Electric', 'Electric')
        )
   

    car_title = models.CharField(max_length=50)
    city = models.CharField(choices=city_choice, max_length=50)
    state = models.CharField(choices=state_choice,max_length=50)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(choices=year_choice)
    congition = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    car_photo = models.ImageField(upload_to= 'photo/%Y/%M/%D')
    car_photo1 = models.ImageField(upload_to= 'photo/%Y/%M/%D', blank=True)
    car_photo2 = models.ImageField(upload_to= 'photo/%Y/%M/%D', blank=True)
    car_photo3 = models.ImageField(upload_to= 'photo/%Y/%M/%D', blank=True)
    car_photo4 = models.ImageField(upload_to= 'photo/%Y/%M/%D', blank=True)
    car_photo5 = models.ImageField(upload_to= 'photo/%Y/%M/%D', blank=True)
    features = models.CharField(choices=features_choices,max_length=50)
    body_style = models.CharField(choices= body_choice ,max_length=50)
    engine = models.CharField(max_length=50)
    trasmission = models.CharField(choices=trasmission_choice, max_length=50)
    interior = models.CharField(max_length=50)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices,max_length=10)
    passenger = models.IntegerField()
    vin_no = models.CharField(max_length=50)
    millage = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_choice,max_length=20)
    no_of_owners = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    

