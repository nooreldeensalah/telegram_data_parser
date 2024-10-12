from djongo import models

class Credentials(models.Model):
    url = models.CharField(max_length=255, db_column='URL')  # Custom MongoDB field name
    username = models.CharField(max_length=255, null=True, db_column='Username')  # Custom field
    password = models.CharField(max_length=255, null=True, db_column='Password')  # Custom field
    application = models.CharField(max_length=255, null=True, db_column='Application')  # Custom field

    class Meta:
        db_table = "credentials"
