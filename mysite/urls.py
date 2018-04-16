from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from mysite.core import views as core_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^home$', core_views.home, name='home'),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^upload/$', core_views.createArtwork.as_view(), name='upload'),
    url(r'^Shopping_Cart/$', core_views.Shopping_Cart, name='Shopping_Cart'),
    url(r'^(?P<user_id>[0-9]+)/$', core_views.HomeView.as_view(), name='HomeView'),
    url(r'^HomeView/$', core_views.HomeView.as_view(), name='HomeView'),
    url(r'^home/(?P<pk>[0-9]+)/Shopping/$', core_views.Shopping, name='Shopping'),

    url(r'^home/(?P<pk>[0-9]+)/createComment/$', core_views.createComment.as_view(), name='createComment'),
    # url(r'^request/$', core_views.createRequest, name='request'),
    url(r'^order/$', core_views.order, name='order'),
    # url(r'^home/(?P<pk>[0-9]+)/delete/$', core_views.Delete.as_view(), name='Delete'),
    url(r'^delete/(\d+)/$',core_views.delete ,name='Delete'),
    url(r'^home/(?P<pk>[0-9]+)/modify/$', core_views.Delete.as_view(), name='modify'),
    url(r'^home/(?P<pk>[0-9]+)/modify2/$', core_views.modifiy.as_view(), name='modify2'),
    url(r'^request/$', core_views.joinReq,name="request"),
    url(r'^profile/$', core_views.profile, name='profile'),
    url(r'^browse/$', core_views.HomeView.as_view(), name='browse'),
    url(r'^blog_search_list_view/$', core_views.BlogSearchListView.as_view(), name='blog_search_list_view'),
    url(r'^artist/$', core_views.artistsInfo.as_view(), name='artistInfo'),
    url(r'^requesting/$', core_views.requesting, name='requesting'),
    url(r'^requesting/artistInfo/$', core_views.artistsInfo.as_view(), name='requesting/artistInfo'),
    url(r'^Commissions/$', core_views.Commissions, name='Commissions'),
    url(r'^createProfile/$', core_views.createProfile.as_view(), name='createProfile'),
    url(r'^browse/(?P<pk>[0-9]+)/displayThis$', core_views.displayThis, name='displayThis'),
    url(r'^home/(?P<pk>[0-9]+)/DeleteAcc/$', core_views.DeleteAcc.as_view(), name='DeleteAcc'),
    url(r'^requesting/(?P<pk>[0-9]+)/DeleteReq/$', core_views.DeleteReq.as_view(), name='DeleteReq'),
    url(r'^displayThisBack/$', core_views.displayThisBack, name='displayThisBack'),
    url(r'^CommentInfo/$', core_views.CommentInfo.as_view(), name='CommentInfo'),
    url(r'^createComplaint/$', core_views.createComplaint.as_view(), name='createComplaint'),
    url(r'^createReview/$', core_views.createReview.as_view(), name='createReview'),
    url(r'^profile2/$', core_views.profile2, name='profile2'),
    url(r'^profile/(?P<pk>[0-9]+)/modifyProfile/$', core_views.modifyProfile.as_view(), name='modifyProfile'),
    url(r'^Shopping_Cart/(?P<pk>[0-9]+)/backToArt/$', core_views.backToArt, name='backToArt'),
    url(r'^artistInfo/(?P<pk>[0-9]+)/displayArtist$', core_views.displayArtist, name='displayArtist'),
    url(r'^Rev&Com$', core_views.Rev_Com, name='Rev&Com'),
    url(r'^images/$', core_views.image.as_view(), name='image'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

