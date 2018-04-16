# from django.contrib.auth.models import User
# from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
# from django.urls import reverse
# from django.utils.timezone import now
#
#
# # not the right models !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!S
#
# @python_2_unicode_compatible
# class Artwork(models.Model):
#     artName = models.CharField(max_length=50, default="")
#     artSize = models.CharField(max_length=200, default="")
#     artPrice = models.CharField(max_length=500)
#     owner = models.ForeignKey(User, related_name="owner",on_delete=models.CASCADE)
#     artImage = models.ImageField(upload_to = 'media', blank=False)
#
#
#     # on submit click on the user entry page, it redirects to the url below.
#     def get_absolute_url(self):
#         return reverse('home')
#
#
#     def __unicode__(self):
#         return unicode(self.user)
#
#
#
# @python_2_unicode_compatible
# class Comments(models.Model):
#     comment = models.TextField(null=True, blank=True)
#
#     def get_absolute_url(self):
#         return reverse('Comments')
#
#
# @python_2_unicode_compatible
# class Order(models.Model):
#     user = models.ForeignKey(User, models.CASCADE)
#     artwork = models.ForeignKey(Artwork, models.CASCADE, default=1)
#
#
#
#
# @python_2_unicode_compatible
# class Request(models.Model):
#     name = models.CharField('Request Name', max_length=100)
#     desc = models.CharField('Request Description', max_length=500)
#     time = models.DateTimeField('Request Time', default=now())
#     owner = models.ForeignKey(User, related_name="owner",on_delete=models.CASCADE)
#
#
#
# @python_2_unicode_compatible
# class ShoppingCart(models.Model):
#     artName = models.CharField(max_length=50, default="")
#     artSize = models.CharField(max_length=200, default="")
#     artPrice = models.CharField(max_length=500)
#     owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
#     artImage = models.ImageField(upload_to='media', blank=False)