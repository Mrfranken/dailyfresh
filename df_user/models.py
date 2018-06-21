from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=50)
    upassword = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uaddressee = models.CharField(max_length=30)
    ushipping_address = models.CharField(max_length=100)
    uzip_code = models.CharField(max_length=6)
    uphone_number = models.CharField(max_length=11)




