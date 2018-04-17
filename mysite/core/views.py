from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from mysite.core.forms import  createComment, createRequest,createShoppingCart
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mysite.core.models import Artwork, ShoppingCart, Request, Comments, Order, Profile, Complaint, Review
from django.contrib.auth.models import User

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView
from functools import reduce
from .forms import RequestForm
import operator
from django.contrib import messages
from django.db.models import Q
from django.db import connection, transaction



@login_required(login_url="/login/")
def home(request):
        join_obj = Artwork.objects.filter(owner=request.user)
        join_obj2 = Request.objects.filter(owner=request.user).count()
        join_obj3 = Comments.objects.all()
        join_obj4 = Review.objects.filter(owner=request.user)
        join_obj5 = Complaint.objects.filter(owner=request.user)

        context = {'art_list': join_obj,'count': join_obj2,'Comments_list':join_obj3,'Review_list': join_obj4,'Complaint_list': join_obj5}
        return render(request, 'home.html',context)




@login_required(login_url="/login/")
def Rev_Com(request):
        join_obj4 = Review.objects.filter(owner=request.user)
        join_obj5 = Complaint.objects.filter(owner=request.user)

        context = {'Review_list': join_obj4,'Complaint_list': join_obj5}
        return render(request, 'Rev_Com.html',context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class HomeView(generic.ListView):
    model = Artwork
    template_name = 'browse.html'
    context_object_name = 'art_list'
    # user = authenticate(User.pk)


    def get_queryset(self):
        return Artwork.objects.filter()


class createArtwork(CreateView):
    model = Artwork
    template_name = 'user-form.html'
    fields = ['artName', 'artSize', 'artPrice', 'owner','artImage']

class createComment(CreateView):
    model= Comments
    context_object_name = 'Comments_list'
    template_name = 'add_comment.html'
    fields = ['comment','artwork']


class CommentInfo(generic.ListView):
    model = Comments
    template_name = 'add_comment.html'
    context_object_name = 'Comments_list'

    def get_queryset(self):
        return Comments.objects.all()





class createProfile(CreateView):
    model = Profile
    context_object_name = 'Info_list'
    template_name = 'editProfile.html'
    fields = ['Email', 'First_Name', 'Last_Name', 'Country','CommissionStatus','Age','owner','gender','Profile']


class modifyProfile(CreateView):
    model = Profile
    context_object_name = 'Info_list'
    template_name = 'editProfile.html'
    fields = ['Email', 'First_Name', 'Last_Name', 'Country','CommissionStatus','Age','owner','gender','Profile']



# @login_required(login_url="/login/")



class createComplaint(CreateView):
    model = Complaint
    context_object_name = 'Complaint_list'
    template_name = 'editComplaint.html'
    fields = ['desc','owner','owner2' ]


class createReview(CreateView):
    model = Review
    context_object_name = 'Review_list'
    template_name = 'editReview.html'
    fields = ['desc','owner','owner2' ]



def profile(request):
        join_obj = Profile.objects.filter(owner=request.user)
        context = {'Info_list': join_obj,}
        return render(request, 'profile.html',context)




def profile2(request):
        join_obj = Profile.objects.filter(owner=request.user)
        context = {'Info_list': join_obj,}
        return render(request, 'profile2.html',context)



class modifiy(UpdateView):
    model = Artwork
    template_name = 'user-form.html'
    fields = ['artName', 'artSize', 'artPrice','owner', 'artImage']



class Delete(DeleteView):
    model = Artwork
    success_url = reverse_lazy('home')



def delete(request, id):
   art = Artwork.objects.get(pk = id)
   art.delete()
   return render(request, "home.html")

   # return HttpResponse('deleted')



@login_required(login_url="/login/")
def joinReq(request):
    join_obj = Artwork.objects.filter(owner=request.user)
    context = {'art_list': join_obj}
    return render(request, "specUser.html",context)
#

# @login_required(login_url="/login/")
def Shopping_Cart(request):
    join_obj = ShoppingCart.objects.filter(owner=request.user)
    # context = {'shopping_list': join_obj}
    count = ShoppingCart.objects.filter(owner=request.user).count()
    context = {'shopping_list': join_obj, 'count': count}

    return render(request, 'ShoppingCart.html',context)



def browse(request):
    return render(request, 'browse.html')


def displayThisBack(request):
    return HttpResponse('deleted')

    # success_url = reverse_lazy('displayThis')


def Shopping(request, pk):
    model = Artwork
    model = ShoppingCart

    context_object_name = 'shopping_list'


    art = Artwork.objects.get(id=pk)
    join_obj =  ShoppingCart.objects.create(artName=art.artName,artSize=art.artSize,artPrice=art.artPrice, owner=request.user,artImage=art.artImage, owner2=art.owner)
    Artwork.objects.filter(id = pk).delete()
    join_obj = ShoppingCart.objects.filter(owner=request.user)
    context = {'shopping_list': join_obj}

    return render(request, 'ShoppingCart.html',context)


#


def backToArt(request, pk):
    model = Artwork
    model = ShoppingCart

    context_object_name = 'shopping_list'


    art = ShoppingCart.objects.get(id=pk)

    join_obj =  Artwork.objects.create(artName=art.artName,artSize=art.artSize,artPrice=art.artPrice, owner=art.owner2,artImage=art.artImage)
    ShoppingCart.objects.filter(id = pk).delete()
    join_obj = ShoppingCart.objects.filter(owner=request.user)
    context = {'shopping_list': join_obj}

    return render(request, 'ShoppingCart.html',context)





class BlogSearchListView(ListView):

        model = Artwork
        template_name = 'browse.html'
        context_object_name = 'art_list'
        paginate_by = 10

        def get_queryset(self):
            result = super(BlogSearchListView, self).get_queryset()

            query = self.request.GET.get('q')
            if query:
                query_list = query.split()
                result = result.filter(
                    reduce(operator.and_,
                           (Q(artName__icontains=q) for q in query_list)))

            return result




class artistsInfo(generic.ListView):
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all()
    template_name = 'artistInfo.html'




@login_required(login_url="/login/")
def Commissions(request):
    join_obj = Request.objects.filter(owner=request.user)
    count = Request.objects.filter(owner=request.user).count()
    context = {'request_list': join_obj, 'count': count}
    # context = {'request_list': join_obj}
    return render(request, "commission.html",context)




def request(request):

    if request.method == 'POST': # If the form has been submitted...
        form = RequestForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            # print form.cleaned_data['my_form_field_name']

            return HttpResponseRedirect('artistInfo') # Redirect after POST
    else:
        form = RequestForm() # An unbound form

    return render(request, 'requesting.html', {'form': form})



def requesting(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
        else:
            return render(request, 'requesting.html')
    else:
        req = Request()
        req.username = request.GET['username']
        form = RequestForm(instance=req)
        return render(request, 'requesting.html', {'form': form})




@login_required(login_url="/login/")
def displayThis(request, pk):
    obj = Artwork.objects.filter(id=pk)
    obj2 = Comments.objects.filter(id=pk)

    context = {'art_list': obj, 'Comments_list': obj2}

    return render(request, "displayThis.html",context)



class DeleteAcc(DeleteView):
    model = User
    success_url = reverse_lazy('login')


class DeleteReq(DeleteView):
    model = Request
    success_url = reverse_lazy('Commissions')



def order(request):
    if request.method == 'POST':
        msg = ""
        if request.user.is_authenticated:
            order = Order(user=request.user, artwork=Artwork.objects.first())
            order.save()
            msg = "Order in progress"
        else:
            msg = "Unable to place order"
        context_object = {
            'success_message': msg
        }
        return render(request, 'shoppingCart.html', context_object)
    else:
        return render(request, 'order.html')



@login_required(login_url="/login/")
def displayArtist(request, pk):
    obj = User.objects.filter(id=pk)
    obj2 = Review.objects.filter(owner2=pk)
    obj3 = Complaint.objects.filter(owner2=pk)

    context = {'user_list': obj, 'Review_list': obj2, 'Complaint_list': obj3}

    return render(request, "displayArtist.html",context)



class image(generic.ListView):
    context_object_name = 'art_list'

    def get_queryset(self):
        return Artwork.objects.all()
    # return render(request, 'upload/images.html')
    template_name = 'images.html'
