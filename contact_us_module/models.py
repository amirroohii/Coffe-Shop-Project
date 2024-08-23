from django.db import models

# Create your models here.
class ContactUs(models.Model):
    fullname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    read_by_admin = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} {self.fullname} {self.created_date} '
