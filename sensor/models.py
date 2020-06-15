from django.db import models


class User(models.Model):
    user = models.ForeignKey('tmsuser.Account', on_delete=models.CASCADE)


class Product(models.Model):

    m3_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    temp_alarm_max = models.IntegerField(default=0)
    temp_alarm_min = models.IntegerField(default=0)
    hum_alarm_max = models.IntegerField(default=0)
    hum_alarm_min = models.IntegerField(default=0)
    vib_alarm_max = models.IntegerField(default=0)
    vib_alarm_min = models.IntegerField(default=0)


class SensorData(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    temp_me = models.FloatField()
    temp_avg = models.FloatField()
    hum_min = models.FloatField()
    hum_max = models.FloatField()
    hum_me = models.FloatField()
    hum_avg = models.FloatField()
    vib_min = models.FloatField()
    vib_max = models.FloatField()
    vib_me = models.FloatField()
    vib_avg = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status_desc = models.CharField(max_length=255)

    class Meta:
        ordering = ['timestamp']


# class Alert(models.Model):

#     ALERT_METHODS = [
#         ('email', 'email'),
#         ('sms', 'sms')
#     ]
#     SensorData = models.ForeignKey(SensorData, on_delete=models.CASCADE)

#     condition = models.CharField('조건', max_length=10)
#     alert_method = models.CharField(max_length=20, choices=ALERT_METHODS)
