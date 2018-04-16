from django import forms
from django.contrib.auth.models import User, Group
from mysite.core.models import Artwork, Comments, Order, Request, ShoppingCart
#
from django.forms import ModelForm



# class createArtwork(forms.ModelForm):
#     class Meta:
#         model = Artwork
#         fields =['artName','artSize','artPrice','artImage']


class createComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

#
# class createOrder(forms.ModelForm):
#     class Meta:
#         model = Artwork
#         fields = ['artName', 'artSize', 'artPrice', 'artImage']


class createRequest(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'desc', 'time']


class createShoppingCart(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = ['artName', 'artSize', 'artPrice', 'artImage']



class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'desc', 'time', 'owner','owner2']

#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = MoreInfo
#         fields = ('Email', 'First_Name', 'Last_Name','Country','Age','gender')
