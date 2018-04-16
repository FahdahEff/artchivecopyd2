from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from django.utils.timezone import now

from django.db.models.signals import post_save
from django.dispatch import receiver






@python_2_unicode_compatible
class Artwork(models.Model):
    artName = models.CharField(max_length=50, default="")
    artSize = models.CharField(max_length=200, default="")
    artPrice = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name="Artwork_owner",on_delete=models.CASCADE)
    artImage = models.ImageField(upload_to = 'media', blank=False)


    # on submit click on the user entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('home')

    def __unicode__(self):
        return unicode(self.user)



@python_2_unicode_compatible
class Comments(models.Model):
    comment = models.TextField(null=True)
    artwork = models.ForeignKey(Artwork,related_name="Artwork_ID",on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')


@python_2_unicode_compatible
class Order(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    artwork = models.ForeignKey(Artwork, models.CASCADE)





@python_2_unicode_compatible
class Request(models.Model):
    name = models.CharField('Request Name', max_length=100)
    desc = models.CharField('Request Description', max_length=500)
    time = models.DateTimeField('Request Time', default=now())
    owner = models.ForeignKey(User, related_name="Request_owner",on_delete=models.CASCADE)
    owner2 = models.ForeignKey(User, related_name="Request_owner2",on_delete=models.CASCADE, default=0)




@python_2_unicode_compatible
class ShoppingCart(models.Model):
    artName = models.CharField(max_length=50, default="")
    artSize = models.CharField(max_length=200, default="")
    artPrice = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name="ShoppingCart_owner", on_delete=models.CASCADE)
    artImage = models.ImageField(upload_to='media', blank=False)
    owner2 = models.ForeignKey(User, related_name="ArtWork_owner2",on_delete=models.CASCADE, default=0)



@python_2_unicode_compatible
class Review(models.Model):
    desc = models.CharField('Request Description', max_length=500)
    owner = models.ForeignKey(User, related_name="Review_owner",on_delete=models.CASCADE)
    owner2 = models.ForeignKey(User, related_name="Review_owner2",on_delete=models.CASCADE, default=0)

    def get_absolute_url(self):
        return reverse('artistInfo')





@python_2_unicode_compatible
class Complaint(models.Model):
    desc = models.CharField('Request Description', max_length=500)
    owner = models.ForeignKey(User, related_name="Complaint_owner",on_delete=models.CASCADE)
    owner2 = models.ForeignKey(User, related_name="Complaint_owner2",on_delete=models.CASCADE, default=0)

    def get_absolute_url(self):
        return reverse('artistInfo')




@python_2_unicode_compatible
class Profile(models.Model):
    Email = models.EmailField(max_length=50, default="")
    First_Name = models.CharField(max_length=50, default="")
    Last_Name = models.CharField(max_length=50, default="")
    Country = models.CharField(max_length=200, default="")
    CommissionStatus = models.CharField(max_length=200, default="")
    Age = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name="Info_owner",on_delete=models.CASCADE, default=0)
    gender = models.CharField(max_length=50, default="")
    Profile = models.ImageField(upload_to='media', blank=False)

    def get_absolute_url(self):
        return reverse('profile2')
