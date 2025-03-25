from django.db import models

class Origincard(models.Model):
    Card_number = models.IntegerField()
    National_code = models.CharField(max_length=11 , unique=True)
    phonenumber = models.CharField(max_length=12 , unique=True)
    name = models.CharField(max_length=50)
    inventory = models.PositiveBigIntegerField()


class Destinationcard(models.Model):
    Card_number = models.CharField(max_length=16)


class Moneytransfer(models.Model):
 
    class TransferType(models.TextChoices):
        Instant_transfer = 1 , 'Instant transfer'
        Interbank_transfer_pol = 2 , 'Interbank transfer(pol)'
        Interbank_transfer_paya = 3 , 'Interbank transfer(paya)'
        Satna = 4 , 'Satna'
        blu_to_blu = 5 , 'blu to blu'
        

    Origincard = models.ForeignKey(to=Origincard , on_delete=models.PROTECT , related_name="Origincard" )
    Destinationcard = models.ForeignKey (to=Destinationcard , on_delete=models.PROTECT , related_name="Destinationcard")
    Tarnsfer_type = models.CharField(max_length=1 , choices=TransferType.choices , default=TransferType.Instant_transfer)
    Amount = models.PositiveBigIntegerField()
    Date = models.DateTimeField(auto_now_add=True)
