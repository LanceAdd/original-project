from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$',views.Index,name='index'),
    url(r'^index/(?P<bookuser_id>[0-9]+)$',views.Index2,name='index2'),
    url(r'^login/$',views.Login,name='login'),
    url(r'^reach_login/$',views.Reach_login,name='reach_login'),
    url(r'^reach_register/$',views.Reach_register,name='reach_register'),
    url(r'^register/$',views.Register,name='register'),
    url(r'^namesearch/$',views.Namesearch,name='namesearch'),
    url(r'^authorserach/$',views.Authorsearch,name='authorsearch'),
    url(r'^show/(?P<book_id>[0-9]+)/(?P<bookuser_id>[0-9]+)/$',views.Show,name='show'),
    url(r'^borrow/(?P<book_id>[0-9]+)/(?P<bookuser_id>[0-9]+)/$',views.Borrow_book,name='borrow_book'),
    url(r'^borrow_confirm/$',views.Borrow_confirm,name='borrow_confirm'),
    url(r'^back/(?P<book_id>[0-9]+)/(?P<bookuser_id>[0-9]+)/$',views.Back_book,name='back_book'),
    url(r'^back_confirm/$',views.Back_confirm,name='back_confirm'),
    url(r'^showhistory/(?P<bookuser_id>[0-9]+)$',views.Showhistory,name='showhistory'),
    url(r'loginout/$',views.Loginout,name='loginout'),
]