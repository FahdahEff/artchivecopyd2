
from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from mysite.core.models import Artwork, Comments, Order, Request, ShoppingCart, Profile, Complaint, Review

class UserArt(admin.StackedInline):
    model =Artwork
    can_delete =False


class UserAdmin(UserAdmin):
    inlines = (UserArt,)


admin.site.unregister(User)
admin.site.register(User,UserAdmin)

admin.site.register(Artwork)
admin.site.register(Comments)
admin.site.register(Order)
admin.site.register(Request)
admin.site.register(ShoppingCart)
admin.site.register(Profile)
admin.site.register(Complaint)
admin.site.register(Review)
