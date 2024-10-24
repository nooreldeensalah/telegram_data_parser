from djongo import models

class Credentials(models.Model):
    id = models.CharField(max_length=255,primary_key=True ,db_column='_id')
    url = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    application = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = "credentials"

    def __str__(self):
        return self.username