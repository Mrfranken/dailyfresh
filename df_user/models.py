from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=50)
    upassword = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uaddressee = models.CharField(max_length=30, default='')
    ushipping_address = models.CharField(max_length=100, default='')
    uzip_code = models.CharField(max_length=6, default='')
    uphone_number = models.CharField(max_length=11, default='')

    def __str__(self):
        return self.uname.__repr__()




