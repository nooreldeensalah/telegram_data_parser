from djongo import models

class Credential(models.Model):
    id = models.CharField(max_length=255,primary_key=True ,db_column='_id')
    url = models.CharField(max_length=255, db_column='URL')
    username = models.CharField(max_length=255, db_column='Username')
    password = models.CharField(max_length=255, db_column='Password')
    application = models.CharField(max_length=255, db_column='Application')
    class Meta:
        db_table = "credentials"

    def __str__(self):
        return self.username
