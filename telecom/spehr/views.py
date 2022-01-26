from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView,FormView,
                                    CreateView,UpdateView,DeleteView)
from .models import *
from . forms import *
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
import csv
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.


class OrginizationListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    context_object_name = 'orginization'
    model = Orginization
    template_name = 'spehr/orginization_list_view.html'
    permission_required = ""




class OrginizationDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    context_object_name = 'orgin'
    model = Orginization
    template_name = 'spehr/orginization_detail_view.html'
    permission_required = ""
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class OrginizationCreateView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    form_class = OrginizationForm
    context_object_name = 'orini'
    template_name = 'spehr/orginization_create.html'
    model = Orginization
    success_url = '/spehr/create/'
    permission_required = ""
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
#
    # def get_success_url(self):
    #     self.object = self.get_object()
    #     orginization = self.object.orginization
    #     return reverse_lazy('spehr:empolyee_detail_view',kwargs={'orginization':orginization.slug,
    #                                                                 'slug':self.object.slug})
    #
    # def form_valid(self,form,*args,**kwargs):
    #     self.object = self.get_object()
    #     fm = form.save(commit=False)
    #     fm.created_by = self.request.user
    #     fm.empolyee = self.object.empolyee
    #
    #     fm.orginization = self.object
    #     fm.save()
    #     return HttpResponseRedirect(self.get_success_url())


class EmpolyeeListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    context_object_name = 'em'
    model = Empolyee
    template_name = 'spehr/empolyee_list_view.html'
    permission_required = ""


class EmpolyeeDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    context_object_name = 'empo'
    model = Empolyee
    template_name = 'spehr/empolyee_detail_view.html'
    permission_required = ""


class EmpolyeeCreateView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    form_class = EmpolyeeForm
    context_object_name = 'empl'
    template_name = 'spehr/empolyee_form.html'
    model = Empolyee
    success_url = '/spehr/spehr/create_emp/'
    permission_required = ""

class EmpolyeeUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    fields = ('full_name','father_name','designation')
    model = Empolyee
    permission_required = ""

class EmpolyeeDeleteView(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Empolyee
    success_url = reverse_lazy("spehr:orgin_list",)
    permission_required = ""


class EmpolyeeSearchView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Empolyee
    template_name = "spehr/search.html"
    permission_required = ""
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Empolyee.objects.filter(
            Q(full_name__icontains=query) | Q(father_name__icontains=query)
        )
        return object_list






def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['emp_id','Orginization_name','full_name','father_name', 'designation', 'create_at','id_card_NO','volume_NO','page_NO','id_card_pic','all_contacts','emp_pic'])

    users = Empolyee.objects.all().values_list('emp_id','Orginization_name','full_name','father_name', 'designation', 'create_at','id_card_NO','volume_NO','page_NO','id_card_pic','all_contacts','emp_pic')
    for user in users:
        writer.writerow(user)

    return response

class IdentifyListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    context_object_name = 'identify'
    model = Identify
    template_name = "spehr/identify_list_view.html"
    permission_required = ""

class IdentifyDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    context_object_name = 'iden'
    model = Identify
    template_name = "spehr/identify_detail_view.html"
    permission_required = ""

class IdentifyCreateView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    form_class = IdentifyCreateForm
    context_object_name = 'identifycreate'
    model = Identify
    # fields = ('empoly','gsm','full_ismi')
    template_name = "spehr/identify_create_view.html"
    success_url = '/spehr/identify/'
    permission_required = ""
