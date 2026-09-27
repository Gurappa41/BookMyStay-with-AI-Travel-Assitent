from django.db import models

class CustomerDetails(models.Model):
    name=models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    class Meta:
        db_table='Customerdetails'

class HotelProviders(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    HotelName=models.CharField(max_length=100)
    HotelType=models.IntegerField()
    Price=models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    msg=models.CharField(max_length=355)
    class Meta:
        db_table='HotelProviders'


class HotelImages(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(
        HotelProviders,
        on_delete=models.CASCADE
    )
    image = models.BinaryField()
    class Meta:
        db_table = 'HotelImages'


class requestData(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    hotel_id=models.IntegerField(null=True, blank=True)
    checkin = models.DateField()
    checkout = models.DateField()
    class Meta:
        db_table = 'requestData'

class history_data(models.Model):
    id = models.AutoField(primary_key=True)
    hotelId=models.IntegerField()
    cName=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    checkin=models.DateField()
    checkout=models.DateField()
    alloted_rooms=models.IntegerField()
    accepted_date=models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'history_data'
