from djongo import models

class Credentials(models.Model):
    url = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    application = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = "credentials"
