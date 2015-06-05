from django.db import models

class Scan(models.Model):
    scan_string = models.CharField(max_length=300)
    def __str__(self):
        return self.scan_string

class Scan_results(models.Model):
    scan_string = models.ForeignKey(Scan)
    scan_live_hosts = models.IntegerField(default=0)
    scan_output = models.CharField(max_length=10000)
    def __str__(self):
        return self.scan_string
