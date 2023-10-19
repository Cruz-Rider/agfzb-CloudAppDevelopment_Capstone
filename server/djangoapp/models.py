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
                "Year: " + self.estd_year + ", " \
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
                "Price: " + self.price + ", " \
                "Features: " + self.features

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
