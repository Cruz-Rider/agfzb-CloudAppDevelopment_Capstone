from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.CharField(max_length=30)
    country_origin = models.CharField(max_length=50)
    estd_year = models.DateField()
    website = models.URLField(max_length=200, unique=True)
    logo = models.ImageField()
    description = models.CharField(max_length=200)
    contact = models.EmailField(max_length=200, unique=True)
    def __str__(self):
        return "Name: " + self.name + ", " \
                "Country: " + self.country_origin + ", " \
                "Description: " + self.description + ", " \
                "Website: " + self.website + ", " \
                "Contact: " + self.contact

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    dealer_id = models.IntegerField(unique=True)
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Hatchback', 'Hatchback'),
        ('Wagon', 'Wagon'),
        ('Truck', 'Truck'),
        ('Van', 'Van'),
        ('Sports Car', 'Sports Car'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('Luxury', 'Luxury'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES)
    year = models.DateField()
    price = models.FloatField()
    features = models.CharField(max_length=200)
    def __str__(self):
        return "Name: " + self.name + ", " \
                "Type: " + self.type + ", " \
                "Features: " + self.features

class CarDealer:
    def __init__(self, address, city, state, full_name, id, lat, long, short_name, st, zip):
        self.id = id
        self.city = city
        self.state = state
        self.st = st
        self.address = address
        self.zip = zip
        self.lat = lat
        self.long = long
        self.full_name = full_name
        self.short_name = short_name

    def __str__(self):
        return "Dealer name: " + self.full_name

class DealerReview:
    def __init__(self, id, name, deaership, review, purchase, purchase_date, car_make, car_model, car_year, sentiment):
        self.id = id
        self.name = name
        self.dealership = dealership
        self.review = review
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment

    def __str__(self):
        return "Review: " + self.review
        