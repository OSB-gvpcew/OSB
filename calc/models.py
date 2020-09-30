from django.db import models
from django.contrib.auth.models import User, auth
from django.conf import settings
import datetime


# Create your models here.
class suggestion(models.Model):
    title=text = models.CharField(max_length=300,default="abc")
    text = models.CharField(max_length=300,default="abc")
    User= settings.AUTH_USER_MODEL
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
        return self.created_at

    class Meta:
        ordering=['-date']

    