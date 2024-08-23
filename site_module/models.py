from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=300)
    site_url = models.CharField(max_length=300)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=200, null=True, blank=True, default='info@gmail.com')
    day_of_week = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()
    address = models.CharField(max_length=300)
    about_us_content = models.CharField(max_length=300)
    about_us_title = models.CharField(max_length=250)
    service_title = models.CharField(max_length=200)
    service_content = models.CharField(max_length=300)
    site_logo = models.ImageField(upload_to='images/site-setting')
    is_main_setting = models.BooleanField()

    def __str__(self):
        return self.site_name

class SiteFooterLink(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500)
    copyright = models.TextField()
    follow_us_content = models.CharField(max_length=300)
    social_address = models.CharField(max_length=300)



