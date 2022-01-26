from django.urls import path
from . import views
from django.conf.urls import url
from .views import export_users_csv


app_name = 'spehr'
urlpatterns = [
        # url(r'^$',views.OrginizationListView.as_view(),name='orgin_list'),

        path('',views.OrginizationListView.as_view(),name='orgin_list'),

        # url(r'^(?P<pk>\d+)/$',views.EmpolyeeDetailView.as_view(),name='detail'),

        path('create/',views.OrginizationCreateView.as_view(),name='create'),
        path('detail/<slug:slug>/',views.OrginizationDetailView.as_view(),name='detail'),

        path('spehr/emp_list/',views.EmpolyeeListView.as_view(),name='emp_list'),
        # url(r'^create_emp/',views.EmpolyeeCreateView.as_view(),name='create_emp'),

        path('spehr/create_emp/',views.EmpolyeeCreateView.as_view(),name='create_emp'),
        path('spehr/emp_detail/<slug:slug>/',views.EmpolyeeDetailView.as_view(),name='emp_detail'),
        path('spehr/update/<slug:slug>/',views.EmpolyeeUpdateView.as_view(),name='update'),
        path('spehr/delete/<slug:slug>/',views.EmpolyeeDeleteView.as_view(),name='delete'),
        path('spehr/search/',views.EmpolyeeSearchView.as_view(), name="search"),
        path('export', export_users_csv, name='export_users_csv'),
        path('identify/',views.IdentifyListView.as_view(),name='identify'),
        path('identifydetail/<slug:slug>/',views.IdentifyDetailView.as_view(),name='identifydetail'),
        path('createiden/',views.IdentifyCreateView.as_view(),name='createiden'),













]
