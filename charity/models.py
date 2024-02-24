from django.db import models

class Charity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return 'Charity: {}'.format(self.name)


class Event(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    img_url = models.CharField(max_length=200)
    start_date = models.DateTimeField("start date")
    end_date = models.DateTimeField("end date")
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return 'Event: {}'.format(self.name)

class Donation(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField("date donated")
    donor_name = models.CharField(max_length=200)
    donor_email = models.EmailField(max_length=200)
    donor_phone = models.CharField(max_length=20)
    pay_method = models.CharField(max_length=10, default='bkash')
    trx_id = models.CharField(max_length=50, default='')
    donor_address = models.TextField()
    def __str__(self):
        return 'Donation: {}'.format(self.donor_name)
